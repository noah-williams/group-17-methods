import datetime
from datetime import date
from datetime import datetime
import psycopg2


class Order:
    def __init__(order, OrderID, UserID, OrderDate, OrderTime, TotalCost, GameID, PaymentInfo, cursor, connection):

        order.OrderID = OrderID
        order.UserID = UserID
        order.OrderDate = OrderDate
        order.OrderTime = OrderTime
        order.TotalCost = TotalCost
        order.GameID = []
        for game in GameID:
            order.GameID.append(game)
        order.Payment = PaymentInfo[0]
        ids = ""
        i = 0
        for game in order.GameID:
            cursor.execute("INSERT INTO orders VALUES (" + str(order.OrderID +i) + ", " + str(order.UserID) + ", '" + str(order.OrderDate) + "', '" + str(order.OrderTime) + "', " + str(order.TotalCost) + ", " +  str(game) + ", '" +  order.Payment +  "');")
            i += 1
        connection.commit()


def add_order(TotalCost, OrderItems, PaymentInfo, cursor, connection, sign_in):
    OrderDate = date.today()
    OrderTime = datetime.now().strftime("%H:%M:%S")

    cursor.execute("SELECT orderid FROM orders")
    ids = cursor.fetchall()
    new_ids = [item for t in ids for item in t]
    if not new_ids:
        new_ids = [0]

    for i in range(len(OrderItems)):
        Order(max(new_ids)+1, sign_in, OrderDate, OrderTime, TotalCost, OrderItems[i], PaymentInfo, cursor, connection)


def view(cursor, sign_in):
    cursor.execute('SELECT * FROM orders WHERE userid = (%s)', (sign_in,))
    orders = cursor.fetchall()
    count = len(orders)
    cursor.execute('SELECT * FROM orders WHERE userid = (%s)', (sign_in,))
    x = 0
    labels = ["Order ID", "User ID", "Order Date", "Order Time", "Total Price", "Games", "Payment Info"]
    while x < count:
        order = cursor.fetchone()
        i = 0
        for y in order:
            print(labels[i], ": ", x, sep='')
            i += 1
        print()
        x += 1
    return
