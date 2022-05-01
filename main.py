import psycopg2
import Game
import Cart
import User
import Order

global signed_in_username


def login():
    try:
        conn = psycopg2.connect(
            host="35.238.14.225",
            database="postgres",
            user="postgres",
            password="group17")
        cur = conn.cursor()

        # Login with username & password
        while 1:

            print("1: Login")
            print("2: Create account")
            print("3: Quit program")
            user_input = int(input("Please select an option 1-3: "))

            # if user presses 1, have inputs for username and password, then check if they exist in database
            if user_input == 1:
                login_check = False
                # username = input("Username: ")
                # password = input("Password: ")

                # userNameList = ["jag1065", "ch3083", "jrs1381", "nmw178"]
                cur.execute("SELECT version();")
                usernames = cur.fetchall()
                print(usernames)
                # passWordList = ["Pa55w0rd", "drowssaP", "WordPass", "Password"]
                cur.execute("SELECT password FROM users")
                passwords = cur.fetchall()

                for x in usernames:
                    if x == username:
                        index = usernames.index(x)
                        if passwords[index] == password:
                            login_check = True
                            print("Login successful.")
                            global signed_in_username
                            signed_in_username = username
                            store()
                        else:
                            print("Password incorrect. Please try again.")
                            break
                    else:
                        print("Username not recognized. Please try again or create an account.")
                        break
                if login_check:
                    break

            # if user presses 2, have inputs to create a new user, then send them to the store
            if user_input == 2:
                first = input("What is your first name? ")
                last = input("What is your last name? ")
                new_username = input("What do you want your username to be? ")
                password = input("What do you want your password to be? ")
                shipping_addr = input("What is your shipping address? ")
                payment = input("What is your card number? ")
                new_user = User.User(first, last, new_username, password, shipping_addr, payment)
                print(new_user.FirstName)
                break

            if user_input == 3:
                quit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)


def store():
    # Once logged in, run store functionality

    print("1: Show games")
    print("2: Show cart")
    print("3: Show account")
    print("4: Logout")
    print("5: Quit program")
    user_input = int(input("Please select an option 1-5: "))
    while 1 <= user_input <= 5:

        # if user presses 1, have inputs for username and password, then check if they exist in database
        if user_input == 1:
            Game.view()

        if user_input == 2:
            Cart.view()

        if user_input == 3:
            User.view()

        # if user presses 4, logout
        if user_input == 4:
            login()

        if user_input == 5:
            quit()

        print("1: Show games")
        print("2: Show cart")
        print("3: Show account")
        print("4: Logout")
        print("5: Quit program")
        user_input = int(input("Please select an option 1-5: "))


if __name__ == "__main__":
    login()
