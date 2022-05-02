import main

class Cart():

    cart_list = []

    def __init__(cart, userID, cursor, connect):
        # takes in which user is using the service
        cart.userID = userID

        # sql statement to see if the user already has a cart
        cursor.execute("SELECT userid FROM carts")
        # Creates ugly list from sql statement
        users_in_carts_table = cursor.fetchall()
        # creates pretty list of the userids in cart? Honestly I don't know what this line does
        Users_list = [item for t in users_in_carts_table for item in t]

        existing_cart_flag = False

        for i in Users_list:
            if i == userID:
                existing_cart_flag = True

        if existing_cart_flag == False:

            if not users_in_carts_table:
                cursor.execute(
                    "INSERT INTO carts(cartid, userid, games, total) VALUES ( 1, " + str(userID) + ",  ' ' , 0.0);" 
                )
            else:
                cursor.execute("select max(cartid) from carts")
                max_cart_row = cursor.fetchone()
                new_cartid = int(max_cart_row[0]) + 1
                cursor.execute(
                    "INSERT INTO carts(cartid, userid, games, total) VALUES (" + str(new_cartid) + ", " + str(userID) + ", ' ', 0.0);"
                )
            connect.commit()