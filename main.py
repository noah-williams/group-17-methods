# login with username & password

print("1: Show games")
print("2: Show cart")
print("3: Show account")
print("4: Logout")
print("5: Quit program")
userInput = int(input("Please select an option 1-5: "))
while 1 <= userInput <= 5:

    # if user presses 1, show list of games
    if userInput == 1:
        print("1: Go back")
        gameInput = int(input("Please select an option: "))
        while 1 <= gameInput <= 5:
            if gameInput == 1:
                break
            print("1: Go back")
            gameInput = int(input("Please select an option: "))

    # if user presses 2, show their cart
    if userInput == 2:
        print("1: Go back")
        print("2: View cart")
        print("3: Remove game")
        print("4: Checkout")
        cartInput = int(input("Please select an option 1-4: "))
        while 1 <= cartInput <= 4:
            if cartInput == 1:
                break
            if cartInput == 2:
                quit()
            if cartInput == 3:
                quit()
            if cartInput == 4:
                quit()
            print("1: Go back")
            print("2: View cart")
            print("3: Remove game")
            print("4: Checkout")
            cartInput = int(input("Please select an option 1-4: "))

    # if user presses 3, show their account info
    if userInput == 3:
        print("1: Go back")
        print("2: View orders")
        print("3: Update info")
        print("4: Delete account")
        accountInput = int(input("Please select an option 1-4: "))
        while 1 <= accountInput <= 5:
            if accountInput == 1:
                break
            if accountInput == 2:
                quit()
            if accountInput == 3:

                print("1: Go back")
                print("2: Update shipping")
                print("3: Update payment")
                print("4: Reset password")
                print("5: Update age")
                updateInput = int(input("Please select an option 1-5: "))
                while 1 <= updateInput <= 5:
                    if updateInput == 1:
                        break
                    if updateInput == 2:
                        quit()
                    if updateInput == 3:
                        quit()
                    if updateInput == 4:
                        quit()
                    if updateInput == 5:
                        quit()
                    print("1: Go back")
                    print("2: Update shipping")
                    print("3: Update payment")
                    print("4: Reset password")
                    print("5: Update age")
                    updateInput = int(input("Please select an option 1-5: "))

            if accountInput == 4:
                quit()
            print("1: Go back")
            print("2: View orders")
            print("3: Update info")
            print("4: Delete account")
            accountInput = int(input("Please select an option 1-4: "))

    # if user presses 4, logout
    if userInput == 4:
        #todo
        quit()

    # if user presses 5, exit
    if userInput == 5:
        quit()

    print("1: Show games")
    print("2: Show cart")
    print("3: Show account")
    print("4: Logout")
    print("5: Quit program")
    userInput = int(input("Please select an option 1-5: "))