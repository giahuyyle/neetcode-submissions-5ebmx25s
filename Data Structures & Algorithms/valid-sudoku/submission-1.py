class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for r in range(9):
            seen_row = set()

            for c in range(9):
                if board[r][c] in seen_row and board[r][c] != ".":
                    return False
                else:
                    seen_row.add(board[r][c])
        
        # cols
        for c in range(9):
            seen_col = set()
            for r in range(9):
                if board[r][c] in seen_col and board[r][c] != ".":
                    return False
                else:
                    seen_col.add(board[r][c])

        # 3x3 boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen_box = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        if board[r][c] != ".":
                            if board[r][c] in seen_box:
                                return False
                            seen_box.add(board[r][c])
                            
        return True