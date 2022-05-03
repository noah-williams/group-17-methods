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
                    # print(better_gameids[responce - 2])
                    cursor.execute("DELETE FROM carts WHERE ctid IN (SELECT ctid FROM carts WHERE userid = " + str(signed_in_id) + " AND games = '" + str(better_gameids[responce - 2]) + "' LIMIT 1)")
                    connection.commit()
                    print("It has been removed")

        if cart_input == 4:
            cursor.execute("SELECT total FROM carts WHERE userid = " + str(signed_in_id))
            priceList = cursor.fetchall()
            totalCost = 0
            new_priceList = [item for t in priceList for item in t]
            for price in new_priceList:
                price = float(price[1:])
                totalCost += price

            cursor.execute("SELECT games FROM carts WHERE userid = " + str(signed_in_id))
            orderItems = cursor.fetchall()


            new_items = [item for t in orderItems for item in t]
            integer_items = []
            for item in new_items:
                integer_items.append(int(item))

            cursor.execute("SELECT payment FROM users WHERE id = " + str(signed_in_id))
            paymentInfo = cursor.fetchone()

            Order.add_order(totalCost, integer_items, paymentInfo, cursor, connection, signed_in_id)

            cursor.execute("DELETE FROM carts WHERE userid = " + str(signed_in_id))
            connection.commit()

            for item in new_items:
                lower_stock(connection, cursor, item)


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
                cursor.execute("SELECT orderid, date, time, total, payment, COUNT(*) FROM orders WHERE userid = '" + str(signed_in_id) + "' GROUP BY orderid, date, time, total, payment")
                count = cursor.fetchall()

                for i in range(len(count)):
                    print("\nORDER " + str(i+1) + ": -----------------------")
                    print("Date/time of purchase: " + str(count[i][1]) + ", at " + str(count[i][2]))
                    print("Total price: " + str(count[i][3]))
                    print("Payment method: " + str(count[i][4]))
                    print("\nGames purchased:\n")

                    cursor.execute("SELECT games.title FROM orders INNER JOIN games ON orders.gameid=games.id WHERE orders.userid = " + str(signed_in_id) + " AND orders.orderid = " + str(i+1))

                    for j in range(count[i][5]):
                        row = cursor.fetchone()
                        print(row[0])

                print("\n\n\n1: Go back")
                order_inputTMP = input("Please press 1: ")
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
                    cursor.execute("DELETE FROM orders WHERE userid = " + str(signed_in_id))
                    connection.commit()
                    cursor.execute("DELETE FROM users WHERE id = " + str(signed_in_id))
                    connection.commit()
                    login()


def viewGames(connection, cursor, new_cart):
    cursor.execute("SELECT title, stock FROM games")
    games = cursor.fetchall()
    cursor.execute("SELECT title FROM games")
    game_titles = cursor.fetchall()
    new_games = [item for t in game_titles for item in t]

    while 1:

        print("\n\n1: Go back")
        count_var = 2
        for x in games:
            if x[1] <= 0:
                print(count_var, ": ", x[0], " (OUT OF STOCK!)", sep='')
            else:
                print(count_var, ": ", x[0], sep='')
            count_var += 1

        try:
            game_input = int(input("\nPlease select an option 1-" + str(count_var - 1) + ": "))

            if game_input == 1:
                return

            else:
                game_title = str(new_games[game_input - 2])

                cursor.execute('SELECT stock FROM games WHERE title = (%s)', (game_title,))
                stock = cursor.fetchone()

                if stock[0] > 0:

                    cursor.execute('SELECT age FROM users WHERE id = (%s)', (signed_in_id,))
                    age = cursor.fetchone()
                    cursor.execute('SELECT esrb FROM games WHERE title = (%s)', (game_title,))
                    esrb = cursor.fetchone()

                    if esrb[0] == "E":
                        viewGameDetails(cursor, connection, new_cart, game_title)
                    elif esrb[0] == "E10+" and age[0] >= 10:
                        viewGameDetails(cursor, connection, new_cart, game_title)
                    elif esrb[0] == "T" and age[0] >= 13:
                        viewGameDetails(cursor, connection, new_cart, game_title)
                    elif esrb[0] == "M" and age[0] >= 18:
                        viewGameDetails(cursor, connection, new_cart, game_title)
                    else:
                        print("\n\n\nYou are too young for this game!")

                else:
                    print("\nWe're sorry, but this game is currently out of stock!")

        except (BaseException, TypeError) as error:
            print('Please select a valid option', error)


def viewGameDetails(cursor, connection, cart, gameTitle):
    print("\n\n\nFull info for " + gameTitle)

    cursor.execute('SELECT * FROM games WHERE title = (%s)', (gameTitle,))
    game_data = cursor.fetchone()
    labels = ["Game ID", "Title", "Developer", "Publisher", "Genre", "Price", "ESRB rating",
              "Number of copies available",
              "User reviews",
              "Release date"]
    i = 0
    for x in game_data:
        print(labels[i], ": ", x, sep='')
        i += 1
    if input('Do you want to add this game to your cart? y/n: ') == ('y' or 'Y'):
        cart.add_to_cart(game_data[0], game_data[5], cursor, connection)


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
