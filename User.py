import Order
import main


class User:
    def __init__(user, id, fname, lname, username, password, shipping, payment, age, cursor):
        cursor.execute("SELECT id FROM users")
        ids = cursor.fetchall()
        new_ids = [item for t in ids for item in t]

        user.ID = id
        user.FirstName = fname
        user.LastName = lname
        user.Username = username
        user.Password = password
        user.ShippingInfo = shipping
        user.PaymentInfo = payment
        user.OrderHistory = "''"
        user.Age = age

        cursor.execute(
            "INSERT INTO users VALUES ('" + str(user.ID) + "', '" + user.FirstName + "', '" + user.LastName + "', '"
            + user.Username + "', '" + user.Password + "', '" + user.ShippingInfo + "', '" + user.PaymentInfo + "', "
            + user.OrderHistory + ", " + str(user.Age) + ");")

        print("\nThank you for creating an account, " + user.FirstName + "!")

    def output_name(self):
        return self.FirstName


