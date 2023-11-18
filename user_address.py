# contacts.py

# Class representing an address
class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # Method to convert the address to a string
    def __str__(self):
        return f'{self.street} {self.city}, {self.state} {self.zipcode}'
