from sqlite3 import Row
import main
import Order

def view(cursor):
    while 1:

        print("\n\n\n1: Go back")
        print("2: View cart")
        print("3: Remove game")
        print("4: Checkout")
        cart_input = int(input("\nPlease select an option 1-4: "))

        if cart_input == 1:
            return

        if cart_input == 2:
            cursor.execute("SELECT * FROM cart WHERE username = '" + main.signed_in_username + "'")
            row = cursor.fetchall()
            print("\n\n\n" + row)

        if cart_input == 3:
            cursor.execute("DELETE FROM cart WHERE username = '" + main.signed_in_username + "' AND title = '" + "'")
            row = cursor.fetchone()
            print(row)

        if cart_input == 4:
            cursor.execute("SELECT price FROM cart WHERE username = '" + main.signed_in_username + "'")
            priceList = cursor.fetchall()
            totalCost = 0
            for price in priceList:
                totalCost += price
            cursor.execute("SELECT title FROM cart WHERE username = '" + main.signed_in_username + "'")
            orderItems = cursor.fetchall()
            cursor.execute("SELECT paymentInfo FROM cart WHERE username = '" + main.signed_in_username + "'")
            paymentInfo = cursor.fetchone()
            Order.new_order(totalCost, orderItems, paymentInfo, cursor)
            cursor.execute("DELETE FROM cart WHERE username = '" + main.signed_in_username + "'")
            row = cursor.fetchone()
            print(row)
