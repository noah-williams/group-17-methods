import psycopg2
import Game
import Cart
import User
import Order


global signed_in_username


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
                User.log(cur)
                store()

            if user_input == 2:
                User.add_user(cur)
                store()

            if user_input == 3:
                quit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)


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
                Game.view(cur)

            if user_input == 2:
                Cart.view(cur)

            if user_input == 3:
                User.view(cur)

            if user_input == 4:
                login()

            if user_input == 5:
                quit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)


if __name__ == "__main__":
    login()