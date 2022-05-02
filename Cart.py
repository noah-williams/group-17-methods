import main

class Cart():

    cart_list = []

    def __init__(cart, userID, cursor):
        cart.userID = userID

        cursor.execute("SELECT cartid FROM carts")
        current_cartids = cursor.fetchall()