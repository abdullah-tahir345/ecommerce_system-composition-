
class Product:
    def __init__(self, product_id, name, quantity_in_stock, price):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock
        self.price = price
        
    def display_info(self):
        print('===================')
        print('Product Information')
        print('===================')
        print(f'Product ID : {self.product_id}')
        print(f'Product Name : {self.name}')
        print(f'Product Available Quantity : {self.quantity_in_stock}')
        print(f'Product Price : {self.price}')
        print('===================')
        print()
        
        
