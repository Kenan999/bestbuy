from typing import List, Tuple
import products

class Store:
    def __init__(self, products_list: List[products.Product]):
        self.products = products_list

    def add_product(self, product: products.Product):
        self.products.append(product)

    def remove_product(self, product: products.Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                   ]

    best_buy = Store(product_list)
    products_obj = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products_obj[0], 1), (products_obj[1], 2)]))
