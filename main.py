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

            print("\n1: Login")
            print("2: Create account")
            print("3: Quit program")

            user_inputTMP = input("\nPlease select an option 1-3: ")
            try:
                user_input = int(user_inputTMP)
            except(Exception, TypeError, ValueError):
                user_input = -1
                print("\n\nPlease choose a valid option.")

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
    while 1:
        ageTMP = input("What is your age? ")
        try:
            age = int(ageTMP)
            break
        except(Exception, TypeError, ValueError):
            print("Please input a valid age integer")

    User.User(first, last, new_username, password, shipping, payment, age, cursor)


def log(cursor):
    username_correct = False

    while 1:
        username = input("\nUsername: ")

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

        new_cart = Cart.Cart(signed_in_id, cur, connect)

        while 1:

            print("\n\n1: Show games")
            print("2: Show cart")
            print("3: Show account")
            print("4: Logout")
            print("5: Quit program")
            user_inputTMP = input("\nPlease select an option 1-5: ")
            try:
                user_input = int(user_inputTMP)
            except(Exception, ValueError, TypeError):
                user_input = -1
                print("Invalid Integer Chosen, try again")

            if user_input == 1:
                viewGames(connect, cur, new_cart)

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

        print("\n1: Go back")
        print("2: View cart")
        print("3: Remove game")
        print("4: Checkout")
        cart_inputTMP = input("\nPlease select an option 1-4: ")
        try:
            cart_input = int(cart_inputTMP)
        except(Exception, TypeError, ValueError):
            cart_input = -1
            print("Invalid integer entry.")

        if cart_input == 1:
            return

        if cart_input == 2:
            # Gets all the gameids in their cart
            cursor.execute("SELECT games FROM carts where userid = " + str(signed_in_id) + ";")

            # puts them in a list
            gameids = cursor.fetchall()

            # Then a different list
            better_gameids = [item for t in gameids for item in t]

            total = 0.00
            print("\nThe items in your cart are:\n")
            numbered = 1
            # Iterates over each of your cart items ands lists the games in your cart
            for i in better_gameids:
                # Finds each game in the games table
                cursor.execute("SELECT title,price FROM games WHERE id = " + i +";")
                cart_item = cursor.fetchone()

                #prints the game and the price of the game
                print(numbered, ": ",str(cart_item[0]) + " " + str(cart_item[1]))

                # Adds the price of each game to a total
                cart_item_price = cart_item[1]
                total += float(cart_item_price[1:])
                numbered += 1

            print("\nThe total price of the items in your cart is: ", total)

        if cart_input == 3:
            while 1:
                print("\nWhich game do you want to remove?")

                # Gets all the gameids in their cart
                cursor.execute("SELECT games FROM carts where userid = " + str(signed_in_id) + ";")

                # puts them in a list
                gameids = cursor.fetchall()

                # Then a different list
                better_gameids = [item for t in gameids for item in t]

                print("\n1: Go back")
                count_var = 2
                # Iterates over each of your cart items ands lists the games in your cart
                for i in better_gameids:
                    # Finds each game in the games table
                    cursor.execute("SELECT title,price FROM games WHERE id = " + i +";")
                    cart_item = cursor.fetchone()

                    #prints the game and the price of the game
                    print(count_var, ": ", str(cart_item[0]) + " " + str(cart_item[1]), sep='')

                    count_var += 1
                responce = input("\nPlease select an option 1-" + str(count_var - 1) + ": ")
                count_var -= 1

                if responce == '1':
                    break
                if 1 < int(responce) <= count_var:
                    responce = int(responce)
                    print(better_gameids[responce - 2])
                    cursor.execute("DELETE FROM carts WHERE ctid IN (SELECT ctid FROM carts WHERE userid = " + str(signed_in_id) + " AND games = '" + str(better_gameids[responce - 2]) + "' LIMIT 1)")
                    connection.commit()
                    print("It has been removed")

        if cart_input == 4:
            cursor.execute('SELECT id FROM users WHERE username = (%s)', (main.signed_in_username,))
            temp = cursor.fetchone()
            for x in temp:
                UserID = x
            cursor.execute("SELECT price FROM cart WHERE userid = (%s)", (UserID,))
            priceList = cursor.fetchall()
            totalCost = 0
            for price in priceList:
                totalCost += price
            cursor.execute("SELECT title FROM cart WHERE userid = (%s)", (UserID,))
            orderItems = cursor.fetchall()
            cursor.execute("SELECT paymentInfo FROM cart WHERE userid = (%s)", (UserID,))
            paymentInfo = cursor.fetchone()
            Order.add_order(totalCost, orderItems, paymentInfo, cursor)
            cursor.execute("DELETE FROM carts WHERE userid = " + str(signed_in_id))
            connection.commit()


def viewUser(connection, cursor):
    global signed_in_id
    while 1:

        print("\n\n\n1: Go back")
        print("2: View orders")
        print("3: Update info")
        print("4: Delete account")
        account_inputTMP = input("\nPlease select an option 1-4: ")

        try:
            account_input = int(account_inputTMP)
        except (Exception, TypeError, ValueError):
            account_input = -1
            print("Please select a valid choice.")

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
                order_inputTMP = input("\nPlease press 1: ")
                try:
                    order_input = int(order_inputTMP)
                except(Exception, ValueError, TypeError):
                    order_input = 1

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
                update_inputTMP = input("\nPlease select an option 1-5: ")
                try:
                    update_input = int(update_inputTMP)
                except(Exception, ValueError, TypeError):
                    update_input = -1

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
                    while 1:
                        new_ageTMP = input("\n\n\nWhat is your new age? ")
                        try:
                            new_age = int(new_ageTMP)
                            break
                        except(Exception, ValueError, TypeError):
                            print("Please enter a valid integer age")

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


def viewGames(connection, cursor, new_cart):
    cursor.execute("SELECT title FROM games")
    games = cursor.fetchall()
    new_games = [item for t in games for item in t]

    while 1:

        print("\n\n1: Go back")
        count_var = 2
        for x in games:
            print(count_var, ": ", x, sep='')
            count_var += 1

        try:
            game_input = int(input("\nPlease select an option 1-" + str(count_var - 1) + ": "))

            if game_input == 1:
                return

            else:
                print("\n\n\nFull info for " + new_games[game_input - 2])
                game_title = str(new_games[game_input - 2])
                cursor.execute('SELECT * FROM games WHERE games.title = (%s)', (game_title,))
                game_data = cursor.fetchone()
                labels = ["GameId", "Title", "Developer", "Publisher", "Genre", "Price", "ESRB", "Inventory",
                          "User Rating",
                          "Release Date"]
                i = 0
                for x in game_data:
                    print(labels[i], ": ", x, sep='')
                    i += 1
                print("\n")
                if input('Do you want to add this game to your cart? y/n: ') == ('y' or 'Y'):
                    #print(game_data[5])
                    new_cart.add_to_cart(game_data[0], game_data[5], cursor, connection)

        except (BaseException, TypeError) as error:
            print('Please select a valid option', error)


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
