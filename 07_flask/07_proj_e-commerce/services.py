from db import Product, Invoice, InvoiceProduct
from db_engine import engine
from sqlalchemy.orm import Session


class Transaction:
    def purchase(self, user_id, purchase_date, invoice_products):
        with Session(engine) as session:
            try:
                available_stock_list = []

                # Verifico stock:
                for product in invoice_products:
                    product_id = product.get('product_id')
                    purchase_quantity = product.get('quantity')
                    got_product = session.get(Product, product_id)

                    if got_product is None:
                        return f"Product ID {product_id} not found", 404

                    available_stock = got_product.stock

                    if available_stock < purchase_quantity:
                        return f"Insufficient stock for product ID {product_id} (Desired purchase quantity: {purchase_quantity} - Available stock: {available_stock}).", 400

                    available_stock_list.append(available_stock)

                # Si todo el stock está bien, creo el invoice:
                new_invoice = Invoice(user_id=user_id, purchase_date=purchase_date)
                session.add(new_invoice)
                session.flush()

                # Insert en loop en tabla invoice_products:
                for i, product in enumerate(invoice_products):
                    product_id = product.get('product_id')
                    product_quantity = product.get('quantity')
                    total_product_price = product.get('total_price')
                    
                    new_invoice_product = InvoiceProduct(invoice_id=new_invoice.id, product_id=product_id, quantity=product_quantity, total_price=total_product_price)
                    available_stock = available_stock_list[i]
                    stock_product = session.get(Product, product_id)

                    if stock_product is None:
                        session.rollback()
                        return f"Error updating stock for product ID {product_id}", 404

                    stock_product.stock = available_stock - product_quantity
                    session.add(new_invoice_product)

                session.commit()
                print("Purchase successful")
                return True, 201

            except Exception as error:
                session.rollback()
                print(error)
                return f"Error adding purchase to the database: {error}", 500