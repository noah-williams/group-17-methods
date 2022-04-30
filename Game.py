def view():
    gameList = ["The Elder Scrolls V: Skyrim – Special Edition", "Elden Ring", "Cyberpunk 2077", "DEATHLOOP", "LEGO Star Wars: The Skywalker Saga", "Marvel’s Avengers", "Monster Hunter: World", "Stardew Valley", "Madden NFL 22", "Battlefield 2042"]
    print("1. Go back")
    countVar = 2
    for x in gameList:
        print(countVar, ". ",  x, sep = '')
        countVar += 1
    game_input = int(input("Please select an option: "))

    while 1 <= game_input <= len(gameList)+1:

        if game_input == 0:
            return
        
        else:
            print("Full info for " + gameList[game_input-2])

        print("0. Go back")
        countVar = 2
        for x in gameList:
            print(countVar, ". ", x, sep = '')
            countVar += 1
        game_input = int(input("Please select an option: "))
