import main

class Cart():
    def __init__(cart, userID, cursor, connect):
        # takes in which user is using the service
        cart.userID = userID

        # sql statement to see if the user already has a cart
        cursor.execute("SELECT userid FROM carts")
        # Creates ugly list from sql statement
        users_in_carts_table = cursor.fetchall()
        # creates pretty list of the userids in cart? Honestly I don't know what this line does
        Users_list = [item for t in users_in_carts_table for item in t]

    def add_to_cart(self, gameid, price, cursor, connect):
        # sql statement to see if the user already has a cart
        cursor.execute("SELECT * FROM carts")
        # Creates ugly list from sql statement
        users_in_carts_table = cursor.fetchall()

        # If there are no cart items at all, make a new one with this
        if not users_in_carts_table:
            cursor.execute("INSERT INTO carts(cartid, userid, games, total, gamescount) VALUES ( 1, " + str(self.userID) + ", " + str(gameid) + ", '" + str(float(price[1:])) + "', 1);")
        # Generic make new cart item for new user
        else:
            cursor.execute("select max(cartid) from carts")
            max_cart_row = cursor.fetchone()
            new_cartid = int(max_cart_row[0]) + 1

            cursor.execute("SELECT COUNT(games) FROM carts WHERE userid = " + str(self.userID) + " and games = '" + str(gameid) + "';")
            count_of_game = cursor.fetchone()
            if int(count_of_game[0]) > 0:
                cursor.execute("SELECT gamescount FROM carts WHERE userid = " + str(self.userID) + " and games = '" + str(gameid) + "';")
                count = cursor.fetchone()

                cursor.execute("UPDATE carts SET gamescount = " + str(count[0]+1) + " WHERE userid = " + str(self.userID) + " and games = '" + str(gameid) + "';")
                cursor.execute("UPDATE carts SET total= '" + str(float(price[1:]) * (count[0]+1)) + "' WHERE userid = " + str(self.userID) + " and games = '" + str(gameid) + "';")
            else:
                cursor.execute("INSERT INTO carts(cartid, userid, games, total, gamescount) VALUES (" + str(new_cartid) + ", " + str(self.userID) + ", " + str(gameid) + ", " + str(float(price[1:])) + ", 1);")
        # Commit these changes to the database
        connect.commit()