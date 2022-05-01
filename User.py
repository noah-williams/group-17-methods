import Order
import psycopg2

class User:
    def __init__(user, FirstName, LastName, Username, Password, ShippingInfo, PaymentInfo):
        user.FirstName = FirstName
        user.Lastname = LastName
        user.Username = Username
        user.Password = Password
        user.ShippingInfo = ShippingInfo
        user.PaymentInfo = PaymentInfo

    def Login(user, Username, Password):
        #something something database call something something
        print('test')

    def output_name(user):
        return user.FirstName

def addUser(cursor):
    flag0,flag1,flag2,flag3,flag4,flag5 = 0
    firstTMP = input("What is your first name? ")
    if (isinstance(firstTMP,str)):
        firstName = firstTMP
        flag0 = 1
    lastTMP = input("What is your last name? ")
    if (isinstance(lastTMP,str)):
        lastName = lastTMP
        flag1 = 1
    new_usernameTMP = input("What do you want your username to be? ")
    if (isinstance(new_usernameTMP, str)):
        username = new_usernameTMP
        flag2 = 1
    passwordTMP = input("What do you want your password to be? ")
    if (isinstance(passwordTMP, str)):
        password = passwordTMP
        flag3 = 1
    ShippingAddyTMP = input("What is your shipping address? ")
    if (isinstance(ShippingAddyTMP, str)):
        address = ShippingAddyTMP
        flag4 = 1
    paymentTMP = input("What is your card number? ")
    if (isinstance(paymentTMP, str)):
        cardNumber = paymentTMP
        flag5 = 1
    #new_user = User.User(first, last, new_username, password, ShippingAddy, payment)
    #print(new_user.FirstName)
    if ((flag0 &flag1 & flag2 & flag3 & flag4 & flag5)==1):

        cursor.execute("INSERT INTO users values('" +  +"'")




def log(cursor):
    loginCheck = False
    userName = input("Username: ")

    # userNameList = ["jag1065", "ch3083", "jrs1381", "nmw178"]
    try:
        cursor.execute("GRANT ALL PRIVILEGES ON TABLE users TO group17")
        cursor.execute("SELECT * FROM users WHERE username LIKE '" + userName + "'")
        check = cursor.fetchone()
        #print(check)
        passWord = input("Password: ")
        if (passWord == check[4]):
            inUser = userName
            loginCheck = True
    except(Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)
    if loginCheck == True:
        print("Welcome, " + userName + "!")



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