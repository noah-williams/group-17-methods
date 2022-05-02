import main
import datetime
from datetime import date
from datetime import datetime
import psycopg2
class Order:
    def __init__(order, UserID, OrderDate, OrderTime, TotalCost, OrderItems, PaymentInfo, cursor):
        try:
            order.UserID = UserID
            order.OrderDate = OrderDate
            order.OrderTime = OrderTime
            order.TotalCost = TotalCost
            order.OrderItems = OrderItems
            order.paymentInfo = PaymentInfo

            cursor.execute("SELECT id FROM orders")
            ids = cursor.fetchall()

            cursor.execute(
                'INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (max(ids)+1, UserID, OrderDate, OrderTime, TotalCost, OrderItems, PaymentInfo))
            rows = cursor.fetchone()
            print(rows)

        except (Exception, psycopg2.DatabaseError) as error:
            print('Encountered error', error)

    def output_name(user):
        return user.FirstName

def add_order(TotalCost, OrderItems, PaymentInfo, cursor):
    cursor.execute('SELECT id FROM users WHERE username = (%s)', (main.signed_in_username,))
    temp = cursor.fetchone()
    for x in temp:
        UserID = x
    OrderDate = date.today()
    OrderTime = datetime.now().strftime("%H :%M: %S")
    Order(UserID, OrderDate, OrderTime, TotalCost, OrderItems, PaymentInfo, cursor)

def view(cursor):
    cursor.execute('SELECT id FROM users WHERE username = (%s)', (main.signed_in_username,))
    temp = cursor.fetchone()
    for x in temp:
        UserID = x
    cursor.execute('SELECT * FROM orders WHERE userid = (%s)', (UserID,))
    orders = cursor.fetchall()
    count = len(orders)
    cursor.execute('SELECT * FROM orders WHERE userid = (%s)', (UserID,))
    x = 0
    labels = ["Order ID", "User ID", "Order Date", "Order Time", "Total Price", "Games", "Payment Info"]
    while x < count:
        order = cursor.fetchone()
        i = 0
        for y in order:
            print(labels[i], ": ", x , sep='')
            i += 1
        print()
        x += 1
    return
