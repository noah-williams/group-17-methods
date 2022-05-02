import main

class Cart():

    cart_list = []

    def __init__(cart, userID, cursor):
        # takes in what user is using the service
        cart.userID = userID

        # sql statement to see if the user already has a cart
        cursor.execute("SELECT userid FROM carts")
        # honestly I don't know what this line does
        current_users = cursor.fetchall()
        # Or this line
        Users_list = [item for t in current_users for item in t]