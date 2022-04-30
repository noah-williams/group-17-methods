import psycopg2
import Game
import Cart
import User
import Order

checkVar = False

def main():
    # Login with username & password
    if checkVar != True:
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="testdb",
                user="postgres",
                password="<password goes here>")
            cur = conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)
            
    # label .begin
    print("1: Login")
    print("2: Create account")
    print("3: Quit program")
    user_input = int(input("Please select an option 1-3: "))

    while 1 <= user_input <= 3:

        # if user presses 1, have inputs for username and password, then check if they exist in database
        if user_input == 1:
            # todo
            break

        # if user presses 2, have inputs to create a new user, then send them to the store
        if user_input == 2:
            # todo
            break

        if user_input == 3:
            quit()

        print("1: Login")
        print("2: Create account")
        print("3: Quit program")
        user_input = int(input("Please select an option 1-3: "))

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
                # todo
                loginCheck = False
                userName = input("Username: ")
                passWord = input("Password: ")
                userNameList = ["jag1065", "ch3083", "jrs1381", "nmw178"]
                passWordList = ["Pa55w0rd", "drowssaP", "WordPass", "Password"]
                for x in userNameList:
                    if x == userName:
                        listIndex = userNameList.index(x)
                        if passWordList[listIndex] == passWord:
                            loginCheck = True
                            print("Login successful.")
                            break
                        else:
                            print("Password incorrect. Please try again.")
                            break
                    else:
                        print("Username not recognized. Please try again or create an account.")
                        break
                if loginCheck == True:
                    break

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
