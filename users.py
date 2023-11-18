
class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
class User(Person):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.carts = []
        self.address = None
        
    def add_cart(self, cart):
        self.carts.append(cart)
        
    def display_cart_info(self):
        if len(self.carts) > 0:
            cart_info = self.carts[-1]
            print('===================')
            print(f'User Name : {self.name.title()}')
            print(f'User Email : {self.email}')
            print(f'User Address : {self.address}')
            print()
            print('--Your Cart Items--')
            print('===================')
            cart_info.cart_product_info()
        else:
            print(f"User {self.name} don't have any cart.")
        
        
