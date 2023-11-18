from product import Product
from prettytable import PrettyTable

class Ecommerce:
    def __init__(self):
        self.store_products = []
        
    def add_product_in_store(self, name, quantity_in_stock, price):
        product_id = len(self.store_products) + 1
        product = Product(product_id, name.title(), quantity_in_stock, price)
        self.store_products.append(product)
        
    def disp_product_info(self):
        products = PrettyTable(["Product ID.", "Product Name", "Available Quantity", "Product Price"])
        
        print('==================================================================')
        print('=====================WELCOME TO XYZ COMPANY=======================')
        print('==================================================================')        
        
        for product in self.store_products:
            products.add_row([product.product_id, product.name, product.quantity_in_stock, product.price])
        
        print(products)

