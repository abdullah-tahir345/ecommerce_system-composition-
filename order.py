from prettytable import PrettyTable

class Order:
    def __init__(self):
        self.orders = []
    
    def create_receipt(self, user, cart):
        receipt = PrettyTable(["S NO.", "Product Name", "Quantity", "Product Price", "Total"])
        
        print('==========================================================')
        print('=================WELCOME TO XYZ COMPANY===================')
        print('==========================================================')
        print(f'Customer Name : {user.name}')
        print(f'Customer Email : {user.email}')
        if user.address:
            print(f'Customer Email : {user.address}')
        print('==========================================================')
        
        
        for items in cart.quantity:
            for n, product in enumerate(cart.products):
                if list(items.keys())[0] == product.name:
                    receipt.add_row([n+1, list(items.keys())[0], list(items.values())[0], product.price, list(items.values())[0]*product.price])
        receipt.add_row([' ',' ', ' ',' ',' '])
        receipt.add_row(['', '', '','YOUR TOTAL...',cart.calculate_total()])
        
        print(receipt)
        print('=================Thankyou for visiting us=================')
        print(f'==========================Your Total Ammount: Rs={cart.calculate_total()}/-')