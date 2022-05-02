import main


def view(connection, cursor):
    while 1:

        print("\n\n\n1: Go back")
        print("2: View cart")
        print("3: Remove game")
        print("4: Checkout")
        cart_input = int(input("\nPlease select an option 1-4: "))

        if cart_input == 1:
            return

        if cart_input == 2:
            cursor.execute("SELECT * FROM carts WHERE userid = " + str(main.signed_in_id))
            row = cursor.fetchall()
            print("\n\n\n" + row)

        if cart_input == 3:
            cursor.execute("DELETE FROM carts WHERE userid = " + str(main.signed_in_id) + " AND title = '" + "'")
            connection.commit()

        if cart_input == 4:
            cursor.execute("DELETE FROM carts WHERE userid = " + str(main.signed_in_id))
            connection.commit()
