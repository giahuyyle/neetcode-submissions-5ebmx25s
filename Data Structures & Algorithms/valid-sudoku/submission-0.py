class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = Counter(board[i]).most_common()

            col = []
            for j in range(9):
                col.append(board[j][i])
            col = Counter(col).most_common()

            for el in row:
                if el[0] != "." and el[1] > 1:
                    return False
                if el[0] != "." and el[1] <= 1:
                    break

            for el in col:
                if el[0] != "." and el[1] > 1:
                    return False
                if el[0] != "." and el[1] <= 1:
                    break
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
        