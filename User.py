import Order
import main
import psycopg2


class User:
    def __init__(user, FirstName, LastName, Username, Password, ShippingInfo, PaymentInfo):
        try:
            conn = psycopg2.connect(
                host="34.121.18.98",
                database="methods",
                user="group17",
                password="group17")
            cur = conn.cursor()

            user.FirstName = FirstName
            user.Lastname = LastName
            user.Username = Username
            user.Password = Password
            user.ShippingInfo = ShippingInfo
            user.PaymentInfo= PaymentInfo

            cur.execute("INSERT INTO users (firstname, lastname, username, password, shippingaddress, paymentinfo) VALUES (%s, %s, %s)", (FirstName, LastName, Username, Password, ShippingInfo, PaymentInfo))
            row = cur.fetchone()
            print(row)

        except (Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)

    def output_name(user):
        return user.FirstName

def view():
    try:
        conn = psycopg2.connect(
            host="34.121.18.98",
            database="methods",
            user="group17",
            password="group17")
        cur = conn.cursor()

        print("1: Go back")
        print("2: View orders")
        print("3: Update info")
        print("4: Delete account")
        account_input = int(input("Please select an option 1-4: "))

        while 1 <= account_input <= 5:

            if account_input == 1:
                return

            if account_input == 2:

                cur.execute("SELECT orderhistory FROM users WHERE username = %s", main.signed_in_username)
                row = cur.fetchall()
                print(row)

                print("1: Go back")
                order_input = int(input("Please press 1: "))
                while order_input != 1:
                    print("1: Go back")
                    order_input = int(input("Please press 1: "))

            if account_input == 3:

                print("1: Go back")
                print("2: Update shipping")
                print("3: Update payment")
                print("4: Reset password")
                print("5: Update age")
                update_input = int(input("Please select an option 1-5: "))

                while 1 <= update_input <= 5:

                    if update_input == 1:
                        break

                    if update_input == 2:
                        new_shipping = input("What is your new shipping address?")
                        cur.execute("UPDATE vendors SET shippingaddress = %s WHERE username = %s", (new_shipping, main.signed_in_username))
                        row = cur.fetchone()
                        print(row)

                    if update_input == 3:
                        new_payment = input("What is your new payment information?")
                        cur.execute("UPDATE vendors SET paymentinfo = %s WHERE username = %s", (new_payment, main.signed_in_username))
                        row = cur.fetchone()
                        print(row)

                    if update_input == 4:
                        new_password = input("What is your new password?")
                        cur.execute("UPDATE vendors SET password = %s WHERE username = %s", (new_password, main.signed_in_username))
                        row = cur.fetchone()
                        print(row)

                    if update_input == 5:
                        new_age = input("What is your new age?")
                        cur.execute("UPDATE vendors SET age = %s WHERE username = %s", (new_age, main.signed_in_username))
                        row = cur.fetchone()
                        print(row)

                    print("1: Go back")
                    print("2: Update shipping")
                    print("3: Update payment")
                    print("4: Reset password")
                    print("5: Update age")
                    update_input = int(input("Please select an option 1-5: "))

            if account_input == 4:
                quit()

            print("1: Go back")
            print("2: View orders")
            print("3: Update info")
            print("4: Delete account")
            account_input = int(input("Please select an option 1-4: "))

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)
