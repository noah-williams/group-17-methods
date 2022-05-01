import psycopg2


def view():
    try:
        conn = psycopg2.connect(
            host="34.121.18.98",
            database="methods",
            user="group17",
            password="group17")
        cur = conn.cursor()

        # gameList = ["The Elder Scrolls V: Skyrim – Special Edition", "Elden Ring", "Cyberpunk 2077", "DEATHLOOP", "LEGO Star Wars: The Skywalker Saga", "Marvel’s Avengers", "Monster Hunter: World", "Stardew Valley", "Madden NFL 22", "Battlefield 2042"]
        cur.execute("SELECT title FROM game")
        games = cur.fetchall()

        print("1: Go back")

        count_var = 2
        for x in games:
            print(count_var, ": ", x, sep='')
            count_var += 1
        game_input = int(input("Please select an option: "))

        while 1 <= game_input <= len(games) + 1:

            if game_input == 0:
                return

            else:
                print("Full info for " + games[game_input - 2])

            print("0: Go back")
            count_var = 2
            for x in games:
                print(count_var, ": ", x, sep='')
                count_var += 1
            game_input = int(input("Please select an option: "))

    except (Exception, psycopg2.DatabaseError) as error:
        print('Encountered error', error)
