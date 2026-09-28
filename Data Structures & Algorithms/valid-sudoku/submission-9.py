class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for n in range(9):
                if board[i][n] == ".":
                    continue
                
                if (board[i][n] in cols[n] or
                    board[i][n] in rows[i] or 
                    board[i][n] in squares[i//3,n//3]):

                    return False

                cols[n].add(board[i][n])
                rows[i].add(board[i][n])
                squares[i//3,n//3].add(board[i][n])
        return True