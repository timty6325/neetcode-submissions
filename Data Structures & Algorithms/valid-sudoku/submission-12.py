class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for i in range(9):
            for n in range(9):
                if board[i][n] == '.':
                    continue
            
                cols[n] = cols.get(n, [])
                rows[i] = rows.get(i, [])
                squares[(i//3,n//3)] = squares.get((i//3,n//3), [])

                if (board[i][n] in cols[n] or
                    board[i][n] in rows[i] or
                    board[i][n] in squares[(i//3,n//3)]):
                    return False

                cols[n].append(board[i][n])
                rows[i].append(board[i][n])
                squares[(i//3,n//3)].append(board[i][n])

            
                
        return True


