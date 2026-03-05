"""
This module contains the Product class which represents a product in the store.
"""

class Product:
    """Represents a product in the store."""
    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a new product with a name, price, and quantity."""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid name, price, or quantity")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets the quantity of the product. Deactivates if 0 or less."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints the details of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buys a certain quantity of the product and returns the total cost."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be strictly positive")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock")
        if not self.active:
            raise ValueError("Product is not active")

        self.set_quantity(self.quantity - quantity)
        return float(self.price * quantity)

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
