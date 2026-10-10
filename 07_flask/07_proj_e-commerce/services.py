from db import Product, Invoice, InvoiceProduct


class Transaction:      # Deberría hacerlo un método en db.py con un session para hacer rollback si algo sale mal. Usar comandos directos de ORMs, no los métodos que yo escribí.
    def purchase(self, user_id, purchase_date, invoice_products):
        try:
            available_stock_list = []

            # Verifico stock:
            for product in invoice_products:
                product_id = product.get('product_id')
                purchase_quantity = product.get('quantity')
                got_product = Product.get_by_id(product_id)
                available_stock = got_product.stock

                if available_stock < purchase_quantity:
                    return f"Insufficient stock for product ID {product_id} (Desired purchase quantity: {purchase_quantity} - Available stock: {available_stock}).", 400

                available_stock_list.append(available_stock)

            # Si todo el stock está bien, creo el invoice:
            new_invoice = Invoice(user_id=user_id, purchase_date=purchase_date).add()

            if new_invoice is None:
                return "Error creating invoice", 500

            # Insert en loop en tabla invoice_products:
            for i, product in enumerate(invoice_products):
                new_invoice_product = InvoiceProduct(invoice_id=new_invoice.id, product_id=product.get('product_id'), quantity=product.get('quantity'), total_price=product.get('total_price')).add()

                if new_invoice_product is None:
                    return f"Error inserting product ID {product.product_id} into invoice", 500

                available_stock = available_stock_list[i]
                stock_product = Product.get_by_id(new_invoice_product.product_id)
                stock_result = stock_product.update(stock=(available_stock-product.get('quantity')))

                if stock_result is None:
                    return "Error subtracting purchased quantity from available stock", 500

            return True, 201

        except Exception as error:
            print(error)
            return f"Error adding purchase to the database: {error}", 500