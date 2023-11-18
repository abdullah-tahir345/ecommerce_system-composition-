

class ShoppingCart:
    def __init__(self, store_products):
        self.store_products = store_products
        super().__init__()
        self.products = []
        self.quantity = []
        
    def add_product(self, product_title, quantity):
        product_title = product_title.title()
        if quantity > 0:
            for product in self.store_products.store_products:
                if product.name == product_title:
                    if product.quantity_in_stock > 0:
                        if product.quantity_in_stock > quantity:
                            quantity_cart = {product.name:quantity}
                            self.quantity.append(quantity_cart)
                            product.quantity_in_stock -= quantity
                            self.products.append(product)
                        else:
                            print('Product is available in less quantity.')
                    else:
                        print('Product Unavailable.')
                    break
            else:
                print('Enter a correct product name.')
        else:
            print('Invalid Quantity.')
        
    def remove_product(self, product_title, quantity_needed):
        product_title = product_title.title()
        if quantity_needed >= 0:
            for product in self.store_products.store_products:
                if product.name == product_title:
                    if self.quantity[0][product.name] > quantity_needed and quantity_needed > 0:
                        self.quantity[0][product.name] -= quantity_needed
                        product.quantity_in_stock += quantity_needed
                    elif quantity_needed == 0:
                        product.quantity_in_stock += self.quantity[0][product.name]
                        for item in self.quantity:
                            if product.name:
                                self.quantity.remove(item)
                        self.products.remove(product)
                    break    
        else:
            print('Invalid Number.')
        
    def cart_product_info(self):
        for i in self.quantity:
            print(f'Product Name : {list(i.keys())[0]}')
            print(f'Product Quantity : {list(i.values())[0]}')
            print()
            
    def calculate_total(self):
        total = 0
        for product in self.products:
            for quantity_items in self.quantity:
                if list(quantity_items.keys())[0] == product.name:
                    total += product.price * list(quantity_items.values())[0]
        return total