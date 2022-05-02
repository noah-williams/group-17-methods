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
        game_input = int(input("\nPlease select an option 1-" + str(count_var) + ": "))

        if game_input == 1:
            return

        else:
            print("\n\n\nFull info for " + new_games[game_input - 2])
            cursor.execute("SELECT * FROM games WHERE games.id = %d", game_input)
            game_data = list(cursor.fetchone())
            labels = ["GameId", "Title", "Developer", "Publisher", "Genre", "Price", "Rating", "Inventory", "Rating", "Release Date"]
            i = 0
            for x in game_data:
                print(labels[i], ": ", x , sep='')
                i += 1
            print("\n\n\n")
