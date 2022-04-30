def view():
    print("1: Go back")
    game_input = int(input("Please select an option: "))

    while 1 <= game_input <= 100:

        if game_input == 1:
            return

        # todo: Show list of games that you can select
        # Implementation Idea: Use Select Name from Games and add those to a list. Then use a for loop to iterate through the list and generate a menu which allows the user to select a game by giving the index number which then does a Select * From Games Where Name = list[i] 

        print("1: Go back")
        game_input = int(input("Please select an option: "))
