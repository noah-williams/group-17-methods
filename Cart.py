import main

class Cart(self, userID, cursor):

    cart_list = []

    def __init__(self, userID):
        self.userID = userID

        cursor.execute("SELECT cartid FROM carts")
        current_cartids = cursor.fetchall()