import Order
import main
import psycopg2


class User:
    def __init__(user, FirstName, LastName, Username, Password, ShippingInfo, PaymentInfo, Age, cursor):
        try:
            user.FirstName = FirstName
            user.Lastname = LastName
            user.Username = main.signed_in_username = Username
            user.Password = Password
            user.ShippingInfo = ShippingInfo
            user.PaymentInfo = PaymentInfo

            cursor.execute("SELECT id FROM users")
            ids = cursor.fetchall()

            cursor.execute(
                'INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (max(ids)+1, FirstName, LastName, Username, Password, ShippingInfo, PaymentInfo, "", Age))
            row = cursor.fetchone()
            print(row)

        except (Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)

    def output_name(user):
        return user.FirstName


def add_user(cursor):
    first = input("\n\n\nWhat is your first name? ")
    last = input("What is your last name? ")
    new_username = input("What do you want your username to be? ")
    password = input("What do you want your password to be? ")
    shipping_addr = input("What is your shipping address? ")
    payment = input("What is your card number? ")
    age = int(input("What is your age? "))
    User(first, last, new_username, password, shipping_addr, payment, age, cursor)


def log(cursor):
    login_check = False
    username = input("\n\n\nUsername: ")

    # usernames = ["jag1065", "ch3083", "jrs1381", "nmw178"]
    try:
        # cursor.execute("GRANT ALL PRIVILEGES ON TABLE users TO group17")
        cursor.execute("SELECT * FROM users WHERE username LIKE '" + username + "'")
        check = cursor.fetchone()

        password = input("Password: ")
        if password == check[4]:
            main.signed_in_username = username
            login_check = True
    except(Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)
    if login_check:
        print("\nWelcome, " + check[1] + "!")


def view(cursor):
    while 1:

        print("\n\n\n1: Go back")
        print("2: View orders")
        print("3: Update info")
        print("4: Delete account")
        account_input = int(input("\nPlease select an option 1-4: "))

        if account_input == 1:
            return

        if account_input == 2:

            order_input = 0
            while order_input != 1:
                cursor.execute("SELECT blank FROM users WHERE username = '" + main.signed_in_username + "'")
                row = cursor.fetchall()

                print("\n\n")
                for i in row:
                    print(i)

                print("1: Go back")
                order_input = int(input("\nPlease press 1: "))

        if account_input == 3:
            while 1:

                # cursor.execute("GRANT ALL PRIVILEGES ON TABLE users TO group17")
                cursor.execute("SELECT address, cardNumber, password, age FROM users WHERE username = '" + main.signed_in_username + "'")
                row = cursor.fetchone()
                print(row)

                print("\n\n\nShipping address: " + row[0])
                print("Payment info: " + row[1])
                print("Age: " + row[3])

                print("\n1: Go back")
                print("2: Update shipping")
                print("3: Update payment")
                print("4: Reset password")
                print("5: Update age")
                update_input = int(input("\nPlease select an option 1-5: "))

                if update_input == 1:
                    break

                if update_input == 2:
                    new_shipping = input("What is your new shipping address?")
                    cursor.execute("UPDATE vendors SET shippingaddress = = '" + new_shipping + "' WHERE username = '" + main.signed_in_username + "'")
                    row = cursor.fetchone()
                    print(row)

                if update_input == 3:
                    new_payment = input("What is your new payment information?")
                    cursor.execute('UPDATE vendors SET paymentinfo = %s WHERE username = %s;', (new_payment, main.signed_in_username))
                    row = cursor.fetchone()
                    print(row)

                if update_input == 4:
                    new_password = input("What is your new password?")
                    cursor.execute('UPDATE vendors SET password = %s WHERE username = %s;', (new_password, main.signed_in_username))
                    row = cursor.fetchone()
                    print(row)

                if update_input == 5:
                    new_age = input("What is your new age?")
                    cursor.execute('UPDATE vendors SET age = %s WHERE username = %s;', (new_age, main.signed_in_username))
                    row = cursor.fetchone()
                    print(row)

        if account_input == 4:
            while 1:

                print("Are you sure?")
                print("1: Go back")
                print("2: Yes, delete.")
                update_input = int(input("\nPlease select an option 1-2: "))

                if update_input == 1:
                    break

                if update_input == 2:
                    cursor.execute('DELETE FROM users WHERE username = %s', main.signed_in_username)
                    row = cursor.fetchone()
                    print(row)
                    main.login()
