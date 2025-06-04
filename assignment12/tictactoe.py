class TictactoeExpectation(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][1]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeExpectation("That's not a valid move.")
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index //3
        col = move_index % 3

        if self.board_array[row][col] != " ":
            raise TictactoeExpectation("That spot is taken.")
        
        self.board_array[row][col] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        for i in range(3):
            if self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2] != " ":
                return (True, f"{self.board_array[0][i]} wins!")
            
            if self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i] != " ":
                return (True, f"{self.board_array[0][i]} wins!")
            
        if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " ":
            return (True, f"{self.board_array[0][0]} wins!")
        if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " ":
            return (True, f"{self.board_array[0][2]} wins!")
        

        if all(cell != " " for now in self.board_array for cell in now):
            return (True, "Cat's Game.")
        
        return (False, f"{self.turn}'s turn.")
    
if __name__ == '__main__':
    print("Welcome to TicTacToe!")
    board = Board()

    while True:
        print(board)
        print(f"Valid moves: {Board.valid_moves}")
        move = input(f"{board.turn}'s move: ")

        try:
            board.move(move)
        except TictactoeExpectation as e:
            print("Error:", e.messge)
            continue

        game_over, message = board.whats_next()
        if game_over:
            print(board)
            print(message)
            break 