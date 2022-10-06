from cart import Cart


def nl():
    print(" ")


def Choices():
    nl()
    print("### MATAFFÄR PROGRAM ###")
    print("1. View products")
    print("2. Add an item to cart")
    print("3. View cart")
    print("4. Remove an item from cart")
    print("5. Complete order")
    print("6. Show cart history")
    print("7. Exit program")


if __name__ == "__main__":
    cart_id_input = input("What do you want your cart to be called? ")
    cart1 = Cart(id=cart_id_input)

    while True:
        Choices()
        choice = input("\nEnter your choice: ")
        nl()
        if choice == "1":
            cart1.view_products()

        elif choice == "2":
            loaded_products = cart1.items
            choice = int(input("Which item would you like to add? "))
            cart1.add_to_cart(loaded_products[choice-1])
            print(f"Item #{choice} added to the cart!\n")

        elif choice == "3":
            cart1.view_cart()
            nl()

        elif choice == "4":
            delete_item = input("Which item would you like to delete? ")
            cart1.remove_from_cart(item=delete_item)

        elif choice == "5":
            cart1.complete_order()

        elif choice == "6":
            cart1.show_cart_history()

        elif choice == "7":
            break
        else:
            nl()
            print("Error! You did not select a number!")
