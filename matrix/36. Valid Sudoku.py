# 36. Valid Sudoku
import collections
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:



        # neetcode solution
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in rows[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True

        # neetcode solution

        y = 0
        for row in board:
            elements = set()
            total_el = 0
            for col in row:
                if col != '.':
                    elements.add(col)
                    total_el +=1
            if len(elements) != total_el:
                return False
            
            elements = set()
            total_el = 0
            for x in range(9):
                if board[x][y] != '.':
                    elements.add(board[x][y])
                    total_el +=1
            if len(elements) != total_el:
                return False
            y+=1
            


        x=0
        y=0
        
        while x < 9:
            elements = set()
            total_el = 0
            for k in range(x,x+3):
                for l in range(y,y+3):
                    if board[k][l] != '.':
                        elements.add(board[k][l])
                        total_el +=1
                    print(f'{k} , {l}')
            print('-----------')
            if len(elements) != total_el:
                return False
            y+=3
            if y == 9:
                x+=3
                y=0

        return True



board = [["5","3",".",".","7",".",".",".","."] 
,["6",".",".","1","9","5",".",".","."] 
,[".","9","8",".",".",".",".","6","."] 
,["8",".",".",".","6",".",".",".","3"] 
,["4",".",".","8",".","3",".",".","1"] 
,["7",".",".",".","2",".",".",".","6"] 
,[".","6",".",".",".",".","2","8","."] 
,[".",".",".","4","1","9",".",".","5"] 
,[".",".",".",".","8",".",".","7","9"]] 




board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] # invalid


print(Solution().isValidSudoku(board)) # valid
