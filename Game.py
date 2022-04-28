def view():
    print("1: Go back")
    game_input = int(input("Please select an option: "))

    while 1 <= game_input <= 100:

        if game_input == 1:
            return

        # todo: Show list of games that you can select

        print("1: Go back")
        game_input = int(input("Please select an option: "))
