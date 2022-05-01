import psycopg2
import Game
import Cart
import User
import Order

checkVar = False


def main():
    # Login with username & password
    if not checkVar:
        try:
            connect = psycopg2.connect(
                host="35.238.14.225",
                database="postgres",
                user="group17",
                password="group17"
            )
            cur = connect.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)

    while 1:

        print("1: Login")
        print("2: Create account")
        print("3: Quit program")
        user_input = int(input("Please select an option 1-3: "))

        # if user presses 1, have inputs for username and password, then check if they exist in database
        if user_input == 1:
            # todo
            User.log(cur)
        # if user presses 2, have inputs to create a new user, then send them to the store
        if user_input == 2:


            break

        if user_input == 3:
            quit()

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
            main()

        if user_input == 5:
            quit()

        print("1: Show games")
        print("2: Show cart")
        print("3: Show account")
        print("4: Logout")
        print("5: Quit program")
        user_input = int(input("Please select an option 1-5: "))


if __name__ == "__main__":
    main()
