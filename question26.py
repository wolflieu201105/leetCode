class Solution(object):
    def isValidSudoku(self, board):
        def checkRow(row, num):
            count = 0
            for i in board[row]:
                if i == num:
                    count += 1
            if count > 1:
                return True
            return False
        def checkColumn(column, num):
            count = 0
            for i in range (9):
                if board[i][column] == num:
                    count += 1
            if count > 1:
                return True
            return False
        squareList = [[0,1,2],[3,4,5],[6,7,8]]
        def checkSquare(x, y, num):
            count = 0
            for i in squareList[x]:
                for t in squareList[y]:
                    if board[i][t] == num:
                        count += 1
            if count > 1:
                return True
            return False
        for i in range(9):
            for y in range(9):
                if board[i][y].isnumeric() == False:
                    continue
                if checkRow(i, board[i][y]) or checkColumn(y, board[i][y]) or checkSquare(int(i/3), int(y/3), board[i][y]):
                    return False
        return True
    print(isValidSudoku(None, [[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]))