from tictactoe_classes import TicTacToe
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_play():
    while True:
        user_input = input("\nStart new game? (y/n): ").lower()
        if user_input in ["y", "n"]:
            if user_input == "y":
                clear_screen()
                return True
            return False


def position_keypad():
    row3 = "| (7) | (8) | (9) | "
    row2 = "| (4) | (5) | (6) | "
    row1 = "| (1) | (2) | (3) | "
    print(f"\n{row3.center(35, ' ')}")
    print(f"{row2.center(35, ' ')}")
    print(f"{row1.center(35, ' ')}")


def play():
    clear_screen()
    p1_name = input("\nEnter player 1 name: ")
    p2_name = input("\nEnter Player 2 name: ")
    clear_screen()
    game = TicTacToe(p1_name, p2_name)

    while True:
        if start_play():  # ask user to start new game after every completed game
            game.empty_board()
        else:
            break

        while True:
            # ====== START NEW GAME ====== #
            player_turn = game.randomise()  # randomise markers and which player to go first

            position_keypad()
            game.make_move(player_turn)  # first player to make the first move
            clear_screen()
            game.display_board()  # display board state

            while True:
                # ====== SUCCESSIVE PLAYER TURNS ====== #
                p_idx = game.players.index(player_turn)  # index of the first player that was chosen
                player_turn = game.players[1 - p_idx]  # switch to the other player

                position_keypad()
                game.make_move(player_turn)  # player to make move
                clear_screen()
                game.display_board()

                # ====== END GAME SCENARIOS ====== #
                if game.end_game(player_turn):  # draw or 3-in-a-row
                    break
            break

    clear_screen()
    game.display_statistics()  # display full game stats


if __name__ == "__main__":
    play()


