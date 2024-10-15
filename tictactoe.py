from game import Game

game = Game()

while True:
    game.set_players()

    while True:
        game.set_starting_player()
        game.set_board()
        game.board.fill_board()
        while game.active:
            game.get_move()
            game.board.fill_board()
            game.check_active()
            game.change_active_player()
        continue_game = input("Do you want to play again with the same players (Y/n)? ")
        if continue_game.lower() in ["y", "yes"]:
            print("")
            game.active = True
        elif continue_game.lower() in ["n", "no"]:
            break

    continue_game = input("Do you want to play again with different players (Y/n)? ")
    if continue_game.lower() in ["y", "yes"]:
        print("")
        game.active = True
    elif continue_game.lower() in ["n", "no"]:
        print("\nThanks for playing!\n")
        break
