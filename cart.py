import json
from pprint import pprint


class Cart:

    def __init__(self, id):
        self.id = id
        self.db_varor_file = 'db/varor.json'
        self.cart_file = 'db/cart.json'
        self.cart_history_file = 'db/cart_history.json'
        self.items = self.load_products()
        cart_dict = self.load_cart()
        cart_dict["cart"] = {}
        self.save_to_json(cart_dict, filename=self.cart_file)

    def view_products(self):
        with open(self.db_varor_file, "r") as f:
            temp = json.load(f)
            i = 1
            print("### PRODUCTS LIST ###")
            for entry in temp:
                name = entry["name"]
                price = entry["price"]
                print(f'{i}. {name}')
                print(f'Price: {price}')
                i = i+1
                print("\n")

    def view_cart(self):
        with open(self.cart_file, "r") as y:
            temp = json.load(y)
            cart = temp["cart"]
            print("### CART ###")
            print("Names & prices.")
            for key, value in cart.items():
                print(key, value)

    def load_cart(self):
        with open(self.cart_file, "r") as f:
            loaded_cart = json.load(f)
            return loaded_cart

    def load_cart_history(self):
        with open(self.cart_history_file, "r") as f:
            cart_history = json.load(f)
            return cart_history

    def load_products(self):
        with open(self.db_varor_file, "r") as x:
            items = json.load(x)
            return items

    def save_to_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            return

    def add_to_cart(self, item):
        with open("db/cart.json") as open_cart:
            data = json.load(open_cart)
            data["cart"][self.number_of_keys()+1] = item
            self.save_to_json(data, filename=self.cart_file)

    def number_of_keys(self):
        cart_dict = self.load_cart()
        count = 0
        for key, value in cart_dict["cart"].items():
            count += 1
        return count

    def remove_from_cart(self, item):
        cart_dict = self.load_cart()
        del cart_dict["cart"][item]
        self.save_to_json(cart_dict, filename=self.cart_file)
        print("Item removed from cart!")

    def save_to_cart_history(self, new_data):
        file_data = self.load_cart_history()
        file_data[self.id] = new_data
        self.save_to_json(data=file_data, filename=self.cart_history_file)

    def complete_order(self):
        cart_dict = self.load_cart()
        self.save_to_cart_history(cart_dict)
        cart_dict["cart"] = {}
        self.save_to_json(cart_dict, filename=self.cart_file)

    def show_cart_history(self):
        cart_history_dict = self.load_cart_history()
        print("### CART HISTORY ###")
        pprint(cart_history_dict)
