import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = board[r][c]
                square_key = (r // 3, c // 3)

                # Check if value already exists in current row, col, or square
                if (val in rows[r] or
                        val in cols[c] or
                        val in squares[square_key]):
                    return False

                # Add value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)

        return True