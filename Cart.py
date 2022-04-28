def view():
    print("1: Go back")
    print("2: View cart")
    print("3: Remove game")
    print("4: Checkout")
    cart_input = int(input("Please select an option 1-4: "))

    while 1 <= cart_input <= 4:

        if cart_input == 1:
            return

        if cart_input == 2:
            # todo: View games in cart
            return

        if cart_input == 3:
            # todo: View games in cart, then select a game to remove
            return

        if cart_input == 4:
            # todo: Remove games in cart, then lower games stock
            return

        print("1: Go back")
        print("2: View cart")
        print("3: Remove game")
        print("4: Checkout")
        cart_input = int(input("Please select an option 1-4: "))
