def view(connection, cursor):
    # gameList = ["The Elder Scrolls V: Skyrim – Special Edition", "Elden Ring", "Cyberpunk 2077", "DEATHLOOP", "LEGO Star Wars: The Skywalker Saga", "Marvel’s Avengers", "Monster Hunter: World", "Stardew Valley", "Madden NFL 22", "Battlefield 2042"]
    cursor.execute("SELECT title FROM games")
    games = cursor.fetchall()

    while 1:

        print("\n\n\n1: Go back")
        count_var = 2
        for x in games:
            print(count_var, ": ", x, sep='')
            count_var += 1
        game_input = int(input("\nPlease select an option 1-" + str(count_var) + ": "))

        if game_input == 0:
            return

        else:
            print("Full info for " + games[game_input - 2])
