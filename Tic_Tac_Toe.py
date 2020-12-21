import itertools

game_size = int(input("What size Tic Tac Toe do you wanna play :"))

def win(current_game):

        def all_same(l) :
                player_won = l[0]
                if l.count(l[0]) == len(l) and l[0] != 0:
                        return True
                else :
                        return False

        for row in current_game:
                if all_same(row):
                        print(f"player {row[0]} is the winner horizontally!")
                        return True

        for cols in range(len(current_game)):
                check_vertical = []

                for row in current_game:
                        check_vertical.append(row[cols])
                if all_same(check_vertical):
                        print(f"player {check_vertical[0]} is the winner vertically!")
                        return True
        check_diagonals = []

        for idx in range(len(current_game)):
                check_diagonals.append(current_game[idx][idx])
        if all_same(check_diagonals):
                print(f"player {check_diagonals[0]} is the winner diagonally!")
                return True

        check_diagonals2 = []

        for cols, rows in enumerate(reversed(range(len(current_game)))):
                check_diagonals2.append(current_game[rows][cols])
        if all_same(check_diagonals2):
                print(f"player {check_diagonals2[0]} is the winner diagonally!")
                return True
        return False

def game_board (game_map, player = 0, row = 0, column = 0, just_display = False):
        try:

                if game_map[row][column]!= 0 :
                        print("Position already occupied, please choose another")
                        return game_map,False
                print("   "+"  ".join([str(i) for i in range(len(game_map))]))
                if not just_display :
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                return game_map, True
        except IndexError as I:
                print("Error: Make sure you enter row/column between 0 & 2", I)
                return False
        except Exception as e :
               print("Something went very wrong!", e)
               return False

play  =  True
players = [1,2]
player_choice = itertools.cycle(players)
while play:
        game = [[0 for i in range(game_size)]for i in range(game_size) ]
        game_won = False
        game, _ = game_board(game, just_display=True)
        while not game_won:
                current_player = next(player_choice)
                print(f"Current Player: {current_player}")
                played = False
                while not played:
                        column_choice = int(input("What column do you want to play? :"))
                        row_choice = int(input("What row do you want to play? :"))
                        game, played = game_board(game, current_player, row_choice, column_choice)

                        if win(game):
                                game_won = True
                                again = input("Game over, would you like to play again (y/n) : ")
                                if again.lower() == "y":
                                        print('restarting....')
                                else:
                                        print("Byeee Guu kha")
                                        play = False














