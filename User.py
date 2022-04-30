import Order

class User:
    def __init__(user, FirstName, LastName, Username, Password, ShippingInfo, PaymentInfo):
        user.FirstName = FirstName
        user.Lastname = LastName
        user.Username = Username
        user.Password = Password
        user.ShippingInfo = ShippingInfo
        user.PaymentInfo= PaymentInfo

    def Login(user, Username, Password):
        #something something database call something something
        print('test')

    def output_name(user):
        return user.FirstName

def view():
    print("1: Go back")
    print("2: View orders")
    print("3: Update info")
    print("4: Delete account")
    account_input = int(input("Please select an option 1-4: "))

    while 1 <= account_input <= 5:

        if account_input == 1:
            return

        if account_input == 2:

            # todo: Show list of orders

            print("1: Go back")
            order_input = int(input("Please press 1: "))
            while order_input != 1:
                print("1: Go back")
                order_input = int(input("Please press 1: "))

        if account_input == 3:

            print("1: Go back")
            print("2: Update shipping")
            print("3: Update payment")
            print("4: Reset password")
            print("5: Update age")
            update_input = int(input("Please select an option 1-5: "))

            while 1 <= update_input <= 5:

                if update_input == 1:
                    break

                if update_input == 2:
                    # todo: Update string in database
                    quit()

                if update_input == 3:
                    # todo: Update string in database
                    quit()

                if update_input == 4:
                    # todo: Update string in database
                    quit()

                if update_input == 5:
                    # todo: Update integer in database
                    quit()

                print("1: Go back")
                print("2: Update shipping")
                print("3: Update payment")
                print("4: Reset password")
                print("5: Update age")
                update_input = int(input("Please select an option 1-5: "))

        if account_input == 4:
            quit()

        print("1: Go back")
        print("2: View orders")
        print("3: Update info")
        print("4: Delete account")
        account_input = int(input("Please select an option 1-4: "))
