import psycopg2
import Game
import Cart
import User
import Order

global signed_in_id


def login():
    try:
        connect = psycopg2.connect(
            host="35.238.14.225",
            database="postgres",
            user="group17",
            password="group17")
        cur = connect.cursor()

        while 1:

            print("\n\n\n1: Login")
            print("2: Create account")
            print("3: Quit program")
            user_input = int(input("\nPlease select an option 1-3: "))

            if user_input == 1:
                log(cur)
                connect.commit()
                store()

            if user_input == 2:
                add_user(cur)
                connect.commit()
                store()

            if user_input == 3:
                quit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)


def add_user(cursor):
    first = input("\n\n\nWhat is your first name? ")
    last = input("What is your last name? ")
    new_username = input("What do you want your username to be? ")
    password = input("What do you want your password to be? ")
    shipping = input("What is your shipping address? ")
    payment = input("What is your card number? ")
    age = int(input("What is your age? "))

    User.User(first, last, new_username, password, shipping, payment, age, cursor)


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
        global signed_in_id
        password = input("Password: ")
        if password == check[4]:
            signed_in_id = check[0]
            print("\nWelcome back, " + check[1] + "!")
            break
        else:
            print("\nWrong password!\n")


def store():
    try:
        connect = psycopg2.connect(
            host="35.238.14.225",
            database="postgres",
            user="group17",
            password="group17")
        cur = connect.cursor()

        while 1:

            print("\n\n\n1: Show games")
            print("2: Show cart")
            print("3: Show account")
            print("4: Logout")
            print("5: Quit program")
            user_input = int(input("\nPlease select an option 1-5: "))

            if user_input == 1:
                viewGames(connect, cur)

            if user_input == 2:
                viewCart(connect, cur)

            if user_input == 3:
                viewUser(connect, cur)

            if user_input == 4:
                login()

            if user_input == 5:
                quit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)


def viewCart(connection, cursor):
    global signed_in_id
    while 1:

        print("\n\n\n1: Go back")
        print("2: View cart")
        print("3: Remove game")
        print("4: Checkout")
        cart_input = int(input("\nPlease select an option 1-4: "))

        if cart_input == 1:
            return

        if cart_input == 2:
            cursor.execute("SELECT * FROM carts WHERE userid = " + str(signed_in_id))
            row = cursor.fetchall()

            new_row = [item for t in row for item in t]
            print("\n\n")
            for i in new_row:
                print(i)

        if cart_input == 3:
            # cursor.execute("DELETE FROM carts WHERE userid = " + str(main.signed_in_id) + " AND title = '" + "'")
            # connection.commit()
            return

        if cart_input == 4:
            cursor.execute("DELETE FROM carts WHERE userid = " + str(signed_in_id))
            connection.commit()


def viewUser(connection, cursor):
    global signed_in_id
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
                cursor.execute("SELECT orderhistory FROM users WHERE id = " + str(signed_in_id))
                row = cursor.fetchall()

                print("\n\n")
                for i in row:
                    print(i)

                print("1: Go back")
                order_input = int(input("\nPlease press 1: "))

        if account_input == 3:
            while 1:

                # cursor.execute("GRANT ALL PRIVILEGES ON TABLE users TO group17")
                cursor.execute("SELECT address, payment, age FROM users WHERE id = " + str(signed_in_id))
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
                    cursor.execute(
                        "UPDATE users SET address = '" + new_shipping + "' WHERE id = " + str(signed_in_id))
                    connection.commit()

                if update_input == 3:
                    new_payment = input("\n\n\nWhat is your new payment information? ")
                    cursor.execute(
                        "UPDATE users SET payment = '" + new_payment + "' WHERE id = " + str(signed_in_id))
                    connection.commit()

                if update_input == 4:
                    new_password = input("\n\n\nWhat is your new password? ")
                    cursor.execute(
                        "UPDATE users SET password = '" + new_password + "' WHERE id = " + str(signed_in_id))
                    connection.commit()

                if update_input == 5:
                    new_age = int(input("\n\n\nWhat is your new age? "))
                    cursor.execute("UPDATE users SET age = " + str(new_age) + " WHERE id = " + str(signed_in_id))
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
                    cursor.execute("DELETE FROM users WHERE id = " + str(signed_in_id))
                    connection.commit()
                    login()


def viewGames(connection, cursor):
    cursor.execute("SELECT title FROM games")
    games = cursor.fetchall()
    new_games = [item for t in games for item in t]

    while 1:

        print("\n\n\n1: Go back")
        count_var = 2
        for x in games:
            print(count_var, ": ", x, sep='')
            count_var += 1
        game_input = int(input("\nPlease select an option 1-" + str(count_var - 1) + ": "))

        if game_input == 1:
            return

        else:
            print("\n\n\nFull info for " + new_games[game_input - 2])
            game_title = str(new_games[game_input - 2])
            cursor.execute('SELECT * FROM games WHERE games.title = (%s)', (game_title,))
            game_data = cursor.fetchone()
            labels = ["GameId", "Title", "Developer", "Publisher", "Genre", "Price", "ESRB", "Inventory", "User Rating",
                      "Release Date"]
            i = 0
            for x in game_data:
                labels[i], ": ",
                print(labels[i], ": ", x, sep='')
                i += 1
            print("\n")


def lower_stock(connection, cursor, title):
    cursor.execute('SELECT stock FROM games WHERE games.title = (%s)', (title,))
    row = cursor.fetchone()
    for x in row:
        temp = int(x)
    print(temp)
    stock = temp - 1
    cursor.execute('UPDATE games SET stock = (%s) WHERE games.title = (%s)', (stock, title,))
    connection.commit()
    cursor.execute('SELECT stock FROM games WHERE games.title = (%s)', (title,))
    row2 = cursor.fetchone()
    for y in row2:
        temp2 = int(y)
    print(temp2)



if __name__ == "__main__":
    login()
