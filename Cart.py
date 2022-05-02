import main

class Cart():

    cart_list = []

    def __init__(cart, userID, cursor, connect):
        # takes in what user is using the service
        cart.userID = userID

        # sql statement to see if the user already has a cart
        cursor.execute("SELECT userid FROM carts")
        # honestly I don't know what this line does
        cartid = cursor.fetchall()
        # Or this line
        Users_list = [item for t in cartid for item in t]

        existing_cart_flag = False

        for i in Users_list:
            if i == userID:
                existing_cart_flag = True

        if existing_cart_flag == False:
            if not cartid:
                cursor.execute(
                    "INSERT INTO carts(cartid, userid, games, total) VALUES ( 1, " + str(userID) + ",  ' ' , 0.0);" 
                )
            else:
                cursor.execute(
                    'INSERT INTO carts(cartid, userid, games, total) VALUES (%s, %s, %s, %s)',
                    (max(cartid)+1, userID, '', 0.0)
                )
            connect.commit()