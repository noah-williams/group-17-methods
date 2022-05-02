import main
import psycopg2

def view(connection, cursor):
    cursor.execute("SELECT title FROM games")
    games = cursor.fetchall()
    new_games = [item for t in games for item in t]

    while 1:

        print("\n\n\n1: Go back")
        count_var = 2
        for x in games:
            print(count_var, ": ", x, sep='')
            count_var += 1
        game_input = int(input("\nPlease select an option 1-" + str(count_var-1) + ": "))

        if game_input == 1:
            return

        else:
            print("\n\n\nFull info for " + new_games[game_input - 2])
            game_title = str(new_games[game_input - 2])
            cursor.execute('SELECT * FROM games WHERE games.title = (%s)', (game_title,))
            game_data = cursor.fetchone()
            labels = ["GameId", "Title", "Developer", "Publisher", "Genre", "Price", "ESRB", "Inventory", "User Rating", "Release Date"]
            i = 0
            for x in game_data:
                labels[i], ": ",
                print(labels[i], ": ", x , sep='')
                i += 1
            print("\n")

def lower_stock(connection, cursor, title):
    cursor.execute('SELECT stock FROM games WHERE games.title = (%s)', (title,))
    row = cursor.fetchone()
    for x in row:
        temp = int(x)
    print(temp)
    stock = temp - 1
    cursor.execute('UPDATE games SET stock = (%s) WHERE games.title = (%s)', (stock, title,))
    connection.commit()
    cursor.execute('SELECT stock FROM games WHERE games.title = (%s)', (title,))
    row2 = cursor.fetchone()
    for y in row2:
        temp2 = int(y)
    print(temp2)
