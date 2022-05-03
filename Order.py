import datetime
from datetime import date
from datetime import datetime
import psycopg2


class Order:
    def __init__(order, OrderID, UserID, OrderDate, OrderTime, TotalCost, GameID, PaymentInfo, Count, cursor, connection):

        order.OrderID = OrderID
        order.UserID = UserID
        order.OrderDate = OrderDate
        order.OrderTime = OrderTime
        order.TotalCost = TotalCost
        order.GameID = GameID
        order.Payment = PaymentInfo[0]
        print("Debug Count:" + str(Count))
        order.Count = Count
        print("Debug Order.Count:" + str(order.Count))

        cursor.execute("INSERT INTO orders VALUES (" + str(order.OrderID) + ", " + str(order.UserID) + ", '" + str(order.OrderDate) + "', '" + str(order.OrderTime) + "', " + str(order.TotalCost) + ", " + str(order.GameID) + ", '" + order.Payment + "', " + str(order.Count) + ");")
        connection.commit()


def add_order(TotalCost, OrderItems, PaymentInfo, count, cursor, connection, sign_in):
    print("Debug add_order:" + str(count))
    OrderDate = date.today()
    OrderTime = datetime.now().strftime("%H:%M:%S")

    cursor.execute("SELECT orderid FROM orders")
    ids = cursor.fetchall()
    new_ids = [item for t in ids for item in t]
    if not new_ids:
        new_ids = [0]

    for i in range(len(OrderItems)):
        Order(max(new_ids)+1, sign_in, OrderDate, OrderTime, TotalCost, OrderItems[i], PaymentInfo, count, cursor, connection)


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
