#79
def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    def backtrack(r, c, idx):
        if idx == len(board):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = backtrack(r + 1, c, idx + 1) or backtrack(r - 1, c, idx + 1) or backtrack(r, c + 1, idx + 1) or backtrack(r, c- 1, idx + 1)
        board[r][c] = temp
        return found
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

word = "BJ"
board = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']]
print(exist(board, word))