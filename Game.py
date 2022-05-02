def view(cursor):
    # gameList = ["The Elder Scrolls V: Skyrim – Special Edition", "Elden Ring", "Cyberpunk 2077", "DEATHLOOP", "LEGO Star Wars: The Skywalker Saga", "Marvel’s Avengers", "Monster Hunter: World", "Stardew Valley", "Madden NFL 22", "Battlefield 2042"]
    cursor.execute("GRANT ALL PRIVILEGES ON TABLE games TO group17")
    cursor.execute("SELECT games.\"gameName\" FROM games")
    games = cursor.fetchall()

    while 1:

        print("\n\n\n0: Go back")
        count_var = 1
        for x in games:
            print(count_var, ": ", x, sep='')
            count_var += 1
        game_input = int(input("\nPlease select an option: "))

        if game_input == 0:
            return

        else:
            print("Full info for " + games[game_input - 1])
            cursor.execute("SELECT * FROM games WHERE games.\"gameID\" = %s", game_input)
            game_data = cursor.fetchall()
            labels = ["GameId", "Title", "Developer", "Publisher", "Genre", "Price", "Rating", "Inventory", "Rating", "Release Date"]
            i = 0
            for x in game_data:
                print(labels[i], ": ", x , sep='')
                i += 1
            print("\n\n")
            
