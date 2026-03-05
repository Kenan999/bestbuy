"""
This module contains the main user interface for the store.
"""
import products
import store

def display_menu():
    """Displays the main store menu."""
    print("\nStore Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def handle_list_products(store_obj):
    """Lists all active products in the store."""
    print("------")
    active_products = store_obj.get_all_products()
    for i, product in enumerate(active_products, start=1):
        print(f"{i}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    print("------")
    return active_products

def handle_order(store_obj, active_products):
    """Handles creating and processing an order."""
    if not active_products:
        print("No products available.")
        return

    print("------")
    for i, product in enumerate(active_products, start=1):
        print(f"{i}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    print("------")

    shopping_list = []
    while True:
        print("When you want to finish order, enter empty text.")
        prod_choice = input("What product # do you want? ")

        if not prod_choice:
            break

        try:
            prod_idx = int(prod_choice) - 1
            if prod_idx < 0 or prod_idx >= len(active_products):
                print("Error adding product!")
                continue

            selected_product = active_products[prod_idx]
            qty_choice = input("What amount do you want? ")
            qty = int(qty_choice)

            shopping_list.append((selected_product, qty))
            print("Product added to list!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    try:
        if shopping_list:
            total_cost = store_obj.order(shopping_list)
            print(f"Order made! Total payment: ${total_cost}")
        else:
            print("No order made.")
    except ValueError as error:
        print(f"Error during order: {error}")
    except Exception as error: # pylint: disable=broad-except
        print(f"Error during order: {error}")

def start(store_obj):
    """Starts the interactive menu for the store."""
    while True:
        display_menu()
        choice = input("Please choose a number: ")

        if choice == '1':
            handle_list_products(store_obj)

        elif choice == '2':
            total_qty = store_obj.get_total_quantity()
            print(f"Total of {total_qty} items in store")

        elif choice == '3':
            active = store_obj.get_all_products()
            handle_order(store_obj, active)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

def main():
    """Main entry point for setting up the store and starting the UI."""
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
