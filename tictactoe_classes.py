import random

# personalise print displays:
VAL = 50    # length
CHAR = "-"  # fillchar

player_markers = [
    "O",  # naughts
    "X"  # crosses
]


class Player:

    def __init__(self, player_name):
        self.name = player_name
        self.marker = None
        self.wins = 0
        self.first_turns = 0


class TicTacToe:

    def __init__(self, p1_name, p2_name):
        self.players = [Player(p1_name), Player(p2_name)]  # instantiated Player() classes within Board()
        self.grid = ["-"] + [" "] * 9
        self.filled_positions = 0
        self.games_played = 0  # no. of games played on Board()
        self.draws = 0  # no. of tied game outcomes

    def display_board(self):
        """ Display current board state. """
        pos = self.grid
        row3 = "| " + pos[7] + " | " + pos[8] + " | " + pos[9] + " | "
        row2 = "| " + pos[4] + " | " + pos[5] + " | " + pos[6] + " | "
        row1 = "| " + pos[1] + " | " + pos[2] + " | " + pos[3] + " | "
        print(f"\n{row3.center(35, ' ')}")
        print(f"\n{row2.center(35, ' ')}")
        print(f"\n{row1.center(35, ' ')}")

    def empty_board(self):
        """ Resets to an empty board for the start of every new game. """
        self.grid = ["-"] + [" "] * 9
        self.filled_positions = 0

    def display_player_symbols(self):
        p1, p2 = self.players[0], self.players[1]
        print("\n" + "".center(VAL, "-"))
        print(f" {p1.name} is ({p1.marker}), {p2.name} is ({p2.marker}) ".center(VAL, "-"))
        print("".center(VAL, "-"))

    def randomise(self):
        """
        Randomises player_turn symbols and pick which player_turn to go first.
        """
        # randomise player_turn symbols:
        print("\nShuffling players and markers...")
        random.shuffle(player_markers)
        self.players[0].marker = player_markers[0]  # assign player_turn 1 marker
        self.players[1].marker = player_markers[1]  # assign player_turn 2 marker
        self.display_player_symbols()  # display symbols
        # randomise which player_turn to go first:
        player = random.choice(self.players)
        player.first_turns += 1
        print(f" {player.name} ({player.marker}) to go first ".center(VAL, "-"))
        print("".center(VAL, "-"))
        return player

    def valid_input(self, player):
        """
        Asks for user input for the player's marker position.
        Loops until input is a valid: a numeric value between 1-9.
        """
        while True:
            try:
                marker_position = int(input(f"\n{player.name} ({player.marker}), enter position (1-9): "))
                if self.grid[marker_position] not in player_markers and marker_position in range(1, 10):
                    break
                print(f"Position {marker_position} is occupied. Try again.")
            except ValueError:
                print("ValueError: Invalid character input, try again.")
            except IndexError:
                print("IndexError: Invalid input, try again.")
        return marker_position

    def place_marker(self, player, marker_position):
        self.grid[marker_position] = player.marker
        self.filled_positions += 1

    def make_move(self, player):
        """ PLAYER TURN """
        marker_position = self.valid_input(player)
        self.place_marker(player, marker_position)

    def check_win(self, current_player):
        """
        Checks for three in a row of the same marker in any direction.
        Returns the player (and hence their marker) associated with the win.
        """
        pos = self.grid
        m = current_player.marker
        if (pos[7] == pos[5] == pos[3] == m) or (pos[9] == pos[5] == pos[1] == m) or \
                (pos[7] == pos[8] == pos[9] == m) or (pos[4] == pos[5] == pos[6] == m) or \
                (pos[1] == pos[2] == pos[3] == m) or (pos[7] == pos[4] == pos[1] == m) or \
                (pos[8] == pos[5] == pos[2] == m) or (pos[9] == pos[6] == pos[3] == m):
            print("\n" + "".center(VAL, "-"))
            print("  THREE IN A ROW!  ".center(VAL, "-"))
            print("".center(VAL, "-"))
            print(f"  {current_player.name} wins with ({current_player.marker})!  ".center(VAL, "-"))
            print("".center(VAL, "-"))
            current_player.wins += 1    # update player stats
            self.games_played += 1
            return True
        return False

    def check_draw(self):
        """ Checks if the game board is filled with nine markers. """
        if self.filled_positions == 9:
            print("\n" + "".center(VAL, "-"))
            print("  BOARD FULL!  ".center(VAL, "-"))
            print("".center(VAL, "-"))
            print("  This game is a draw  ".center(VAL, "-"))
            print("".center(VAL, "-"))
            self.draws += 1
            self.games_played += 1
            return True
        return False

    def end_game(self, player):
        return self.check_win(player) or self.check_draw()

    def display_statistics(self):
        """ Display game and player statistics once user exits main game loop """
        if self.games_played > 0:
            p1, p2 = self.players[0], self.players[1]
            print("\n" + "".center(VAL, CHAR))
            print(f"***  GAME STATISTICS  ***".center(VAL, CHAR))
            print("" + "".center(VAL, CHAR))
            print(f"{CHAR * 2}| No. of games: {self.games_played} |".ljust(VAL, CHAR))
            print(f"{CHAR * 2}| Draws: {self.draws} ({(self.draws/self.games_played)*100 :.1f}%) |".ljust(VAL, CHAR))
            print("" + "".center(VAL, CHAR))
            print(f"{CHAR * 2}| {p1.name} |".ljust(VAL, CHAR))
            print(f"{CHAR * 2}| Wins: {p1.wins} ({(p1.wins/self.games_played)*100 :.1f}%) |".ljust(VAL, CHAR))
            print(f"{CHAR * 2}| First Turns: {p1.first_turns} ({(p1.first_turns/self.games_played)*100 :.1f}%) |".ljust(VAL, CHAR))
            print("" + "".center(VAL, CHAR))
            print(f"{CHAR * 2}| {p2.name} |".ljust(VAL, CHAR))
            print(f"{CHAR * 2}| Wins: {p2.wins} ({(p2.wins/self.games_played)*100 :.1f}%)|".ljust(VAL, CHAR))
            print(f"{CHAR * 2}| First turns: {p2.first_turns} ({(p2.first_turns/self.games_played)*100 :.1f}%)|".ljust(VAL, CHAR))
            print("".center(VAL, CHAR))

        """
        Example command line output of game stats:
        
        --------------------------------------------------
        ------------***  GAME STATISTICS  ***-------------
        --------------------------------------------------
        --| No. of games: 5 |-----------------------------
        --| Draws: 0 (0.0%) |-----------------------------
        --------------------------------------------------
        --| Player 1 |------------------------------------
        --| Wins: 1 (20.0%) |-----------------------------
        --| First Turns: 1 (20.0%) |----------------------
        --------------------------------------------------
        --| Player 2 |------------------------------------
        --| Wins: 4 (80.0%) |-----------------------------
        --| First turns: 4 (80.0%) |----------------------
        --------------------------------------------------

        """


