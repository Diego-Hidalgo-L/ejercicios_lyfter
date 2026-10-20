from db import User, Product, BillingAddress, UserPaymentMethod, Cart, Invoice, InvoiceProduct
from db_engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from flask import jsonify
from datetime import date


class Transaction:
    def purchase(self, user_id, cart_id, billing_address_id, user_payment_method_id, purchase_date):
        with Session(engine) as session:
            try:
                # Data validation:
                my_cart = session.get(Cart, cart_id)
                if my_cart is None:
                    return f"Cart not found", 404
                elif my_cart is False:
                    raise Exception(f"Error getting cart ID {cart_id}")
                elif my_cart.user_id != user_id:
                    return f"Invalid cart", 401
                elif my_cart.status != 'Active':
                    return f"Inactive cart", 400

                my_billing_address = BillingAddress.get_by_id(billing_address_id)
                if my_billing_address is None:
                    return f"Billing address not found", 404
                elif my_billing_address is False:
                    raise Exception(f"Error getting billing address ID {billing_address_id}")
                elif my_billing_address.user_id != user_id:
                    return f"Invalid billing address", 401

                my_payment_method = UserPaymentMethod.get_by_id(user_payment_method_id)
                if my_payment_method is None:
                    return "Payment method not found", 404
                elif my_payment_method is False:
                    raise Exception(f"Error getting payment method ID {user_payment_method_id}")
                elif my_payment_method.user_id != user_id:
                    return "Invalid payment method", 401

                if purchase_date is None:
                    purchase_date = date.today()

                # Verifico stock:
                cart_products = my_cart.cart_products
                available_stock_list = []

                for product in cart_products: # lista de diccionarios
                    product_id = product.product_id
                    purchase_quantity = product.quantity
                    got_product = session.get(Product, product_id)

                    if got_product is None:
                        return f"Product ID {product_id} not found", 404

                    available_stock = got_product.stock

                    if available_stock < purchase_quantity:
                        return f"Insufficient stock for product ID {product_id} (Desired purchase quantity: {purchase_quantity} - Available stock: {available_stock}).", 400

                    available_stock_list.append(available_stock)

                # Si todo el stock está bien, creo el invoice:
                new_invoice = Invoice(user_id=user_id, purchase_date=purchase_date, billing_address_id=billing_address_id, user_payment_method_id=user_payment_method_id, status='Completed')
                session.add(new_invoice)
                session.flush()

                # Insert en loop en tabla invoice_products:
                for i, product in enumerate(cart_products):
                    product_id = product.product_id
                    product_quantity = product.quantity
                    total_product_price = product.total_price
                    
                    new_invoice_product = InvoiceProduct(invoice_id=new_invoice.id, product_id=product_id, quantity=product_quantity, total_price=total_product_price)
                    available_stock = available_stock_list[i]
                    stock_product = session.get(Product, product_id)

                    if stock_product is None:
                        session.rollback()
                        return f"Error updating stock for product ID {product_id}", 404

                    stock_product.stock = available_stock - product_quantity
                    session.add(new_invoice_product)

                # Modificar cart status:
                my_cart.status = 'Completed'

                # Commit:
                session.commit()
                print("Purchase successful")
                return True, 201

            except Exception as error:
                session.rollback()
                print(error)
                return f"Error adding purchase to the database: {error}", 500

    def return_purchase(self, invoice_id, user_id):
        with Session(engine) as session:
            try:
                # Verifico si la factura existe en la DB:
                invoice = session.get(Invoice, invoice_id)
                user = session.get(User, user_id)

                if invoice is None:
                    return f"Invoice ID {invoice_id} not found", 404
                elif invoice is False:
                    raise Exception("Error getting invoice from the database")
                elif invoice.user_id != user.id and user.role != 'Administrator':       # Debería dejar que un Administrator haga una devolución por un cliente?
                    return f"Invalid return", 401

                # Aumentar el stock de los productos en la cantidad que se registró en la compra:
                for invoice_product in invoice.products:
                    print("invoice_product_id:", invoice_product.product_id)
                    product = session.get(Product, invoice_product.product_id)
                    product.stock += invoice_product.quantity

                # Modifico la factura original para marcarla con el estado de 'Returned':
                invoice.status = 'Returned'

                # Commit:
                session.commit()
                print("Invoice returned successfully")
                return True, 200

            except Exception as error:
                session.rollback()
                print(error)
                return f"Error returning invoice in the database: {error}", 500