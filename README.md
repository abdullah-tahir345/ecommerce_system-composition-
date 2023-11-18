# ecommerce_system-composition-

This is a simple e-commerce system implemented in Python that simulates the functionality of an online store. The project employs various programming techniques and concepts to create a functional and interactive system. Below is an overview of the main components and techniques used in the project:<hr>

<li><b>Classes and Object-Oriented Programming (OOP)</b></li><br>
    The project extensively utilizes Object-Oriented Programming principles with several classes representing different aspects of the e-commerce system:

<b>Product Class:</b> Represents a product with attributes such as product ID, name, quantity in stock, and price. It includes a method to display product information.

<b>ShoppingCart Class:</b> Manages the shopping cart, allowing users to add and remove products, calculate the total cost, and display the cart's contents.

<b>Ecommerce Class:</b> Represents the online store and contains methods to add products to the store, display product information, and update product details.

<b>Order Class:</b> Generates a receipt for a user's order, displaying details such as product name, quantity, price, and total cost.

<b>Address Class:</b> Represents a user's address and includes a method to convert the address to a string.

<b>User Class:</b> Inherits from the Person class and represents a user with attributes like user ID, name, email, carts, and address. It includes methods to add a cart and display cart information.
<hr>

<b>PrettyTable for Tabular Display</b><br>
The PrettyTable library is employed to create visually appealing tables for displaying product information, cart contents, and order receipts. This enhances the user experience and readability of the information presented.

<b>Error Handling</b><br>
The code incorporates error handling to manage scenarios such as invalid product names, quantities, and numbers. This ensures that the system responds appropriately to user inputs and provides informative error messages.

<b>Project Execution</b><br>
The program.py file demonstrates the functionality of the e-commerce system. It creates an instance of the Ecommerce class, adds products to the store, performs operations with the shopping cart, and generates an order receipt for a user.

This e-commerce system serves as a foundational example, and further enhancements and features can be added based on specific requirements and business logic.

<hr>

In the provided project, several Object-Oriented Programming (OOP) techniques have been employed to structure the code and model the entities within the e-commerce system. Here's a list of OOP techniques used in the project:

<b>Encapsulation:</b>
Each class encapsulates its attributes and methods, keeping the internal implementation details hidden from the external code.

<b>Abstraction:</b>
Classes like Product, ShoppingCart, Ecommerce, etc., provide a high-level abstraction of the entities and their interactions within the e-commerce system.

<b>Inheritance:</b>
The User class inherits from the Person class, showcasing the concept of inheritance to reuse common attributes and methods.

<b>Polymorphism:</b>
Polymorphism is demonstrated through method overloading, where the add_product method in the ShoppingCart class handles different scenarios based on the input parameters.

<b>Composition:</b>
The User class contains a composition relationship with the ShoppingCart class, as a user has a cart. Similarly, the Ecommerce class contains a composition relationship with the Product class.

<b>Method Overriding:</b>
The __str__ method is overridden in the Address class to provide a custom string representation of the address.

<b>Constructor Overloading:</b>
The constructors of various classes, such as Product, User, and ShoppingCart, showcase constructor overloading to initialize objects with different sets of parameters.

<b>Encapsulation:</b>
Access modifiers like private and public are used to control the visibility of attributes and methods within the classes.

<b>Dependency Injection:</b>
The ShoppingCart class depends on the Ecommerce class to access store products. This is a form of dependency injection, where dependencies are provided from the outside.

<b>Class Instantiation:</b>
Instances of classes are created throughout the code, demonstrating the concept of class instantiation.

<b>Single Responsibility Principle (SRP):</b>
Each class has a single responsibility. For example, the Product class is responsible for representing a product, and the ShoppingCart class is responsible for managing the shopping cart.
