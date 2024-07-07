class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diag = 0
        self.antiDiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        player = 1 if player == 1 else -1

        self.rows[row] += player
        self.cols[col] += player
        if row == col: self.diag += player
        if row == (self.n - 1 - col): self.antiDiag += player

        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.antiDiag) == self.n:
            if player == 1: return 1
            elif player == -1: return 2

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)