import Order
import main


class User:
    def __init__(user, fname, lname, username, password, shipping, payment, age, cursor):
        cursor.execute("SELECT id FROM users")
        ids = cursor.fetchall()
        new_ids = [item for t in ids for item in t]

        user.ID = main.signed_in_id = max(new_ids)+1
        user.FirstName = fname
        user.LastName = lname
        user.Username = username
        user.Password = password
        user.ShippingInfo = shipping
        user.PaymentInfo = payment
        user.OrderHistory = "''"
        user.Age = age

        cursor.execute("INSERT INTO users VALUES ('" + str(user.ID) + "', '" + user.FirstName + "', '" + user.LastName + "', '"
                       + user.Username + "', '" + user.Password + "', '" + user.ShippingInfo + "', '" + user.PaymentInfo + "', "
                       + user.OrderHistory + ", " + str(user.Age) + ");")

        print("\nThank you for creating an account, " + user.FirstName + "!")

    def output_name(self):
        return self.FirstName


def add_user(cursor):
    first = input("\n\n\nWhat is your first name? ")
    last = input("What is your last name? ")
    new_username = input("What do you want your username to be? ")
    password = input("What do you want your password to be? ")
    shipping = input("What is your shipping address? ")
    payment = input("What is your card number? ")
    age = int(input("What is your age? "))

    User(first, last, new_username, password, shipping, payment, age, cursor)


def log(cursor):
    username_correct = False
    password_correct = False

    while 1:
        username = input("\n\n\nUsername: ")

        # cursor.execute("GRANT ALL PRIVILEGES ON TABLE users TO group17")
        cursor.execute("SELECT username FROM users")
        usernames = cursor.fetchall()
        new_usernames = [item for t in usernames for item in t]

        for i in new_usernames:
            if username == i:
                username_correct = True

        if username_correct:
            break
        else:
            print("\nThere is no account with this username!")

    while 1:
        cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
        check = cursor.fetchone()

        password = input("Password: ")
        if password == check[4]:
            main.signed_in_id = check[0]
            print("\nWelcome back, " + check[1] + "!")
            break
        else:
            print("\nWrong password!\n")


def view(connection, cursor):
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
                cursor.execute("SELECT orderhistory FROM users WHERE id = " + str(main.signed_in_id))
                row = cursor.fetchall()

                print("\n\n")
                for i in row:
                    print(i)

                print("1: Go back")
                order_input = int(input("\nPlease press 1: "))

        if account_input == 3:
            while 1:

                # cursor.execute("GRANT ALL PRIVILEGES ON TABLE users TO group17")
                cursor.execute("SELECT address, payment, age FROM users WHERE id = " + str(main.signed_in_id))
                row = cursor.fetchone()

                print("\n\n\nShipping address: " + row[0])
                print("Payment info: " + row[1])
                print("Age: " + str(row[2]))

                print("\n1: Go back")
                print("2: Update shipping")
                print("3: Update payment")
                print("4: Reset password")
                print("5: Update age")
                update_input = int(input("\nPlease select an option 1-5: "))

                if update_input == 1:
                    break

                if update_input == 2:
                    new_shipping = input("\n\n\nWhat is your new shipping address? ")
                    cursor.execute("UPDATE users SET address = '" + new_shipping + "' WHERE id = " + str(main.signed_in_id))
                    connection.commit()

                if update_input == 3:
                    new_payment = input("\n\n\nWhat is your new payment information? ")
                    cursor.execute("UPDATE users SET payment = '" + new_payment + "' WHERE id = " + str(main.signed_in_id))
                    connection.commit()

                if update_input == 4:
                    new_password = input("\n\n\nWhat is your new password? ")
                    cursor.execute("UPDATE users SET password = '" + new_password + "' WHERE id = " + str(main.signed_in_id))
                    connection.commit()

                if update_input == 5:
                    new_age = int(input("\n\n\nWhat is your new age? "))
                    cursor.execute("UPDATE users SET age = " + str(new_age) + " WHERE id = " + str(main.signed_in_id))
                    connection.commit()

        if account_input == 4:
            while 1:

                print("\n\n\nAre you sure?")
                print("1: Go back")
                print("2: Yes, delete")
                update_input = int(input("\nPlease select an option 1-2: "))

                if update_input == 1:
                    break

                if update_input == 2:
                    cursor.execute("DELETE FROM users WHERE id = " + str(main.signed_in_id))
                    connection.commit()
                    main.login()
