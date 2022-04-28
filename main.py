from goto import with_goto
import Game
import Cart
import User
import Order


@with_goto
# Login with username & password

label .begin
print("1: Login")
print("2: Create account")
print("3: Quit program")
userInput = int(input("Please select an option 1-3: "))

while 1 <= userInput <= 3:

    # if user presses 1, have inputs for username and password, then check if they exist in database
    if userInput == 1:
        # todo
        break

    # if user presses 2, have inputs to create a new user, then send them to the store
    if userInput == 2:
        # todo
        break

    if userInput == 3:
        quit()

    print("1: Login")
    print("2: Create account")
    print("3: Quit program")
    userInput = int(input("Please select an option 1-3: "))


# Once logged in, run store functionality

print("1: Show games")
print("2: Show cart")
print("3: Show account")
print("4: Logout")
print("5: Quit program")
userInput = int(input("Please select an option 1-5: "))
while 1 <= userInput <= 5:

    if userInput == 1:
        Game.view()

    if userInput == 2:
        Cart.view()

    if userInput == 3:
        User.view()

    # if user presses 4, logout
    if userInput == 4:
        goto .begin

    if userInput == 5:
        quit()

    print("1: Show games")
    print("2: Show cart")
    print("3: Show account")
    print("4: Logout")
    print("5: Quit program")
    userInput = int(input("Please select an option 1-5: "))
