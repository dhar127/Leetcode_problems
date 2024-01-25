class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in map(str, range(1, 10)):
                        if self.isvalid(board, i, j, k):
                            board[i][j] = k
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def isvalid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] == c or board[row][i] == c or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True
