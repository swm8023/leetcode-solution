'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        lt, rt, bt = [0] * 9, [0] * 9, [0] * 9
        for i in range(9):
            for j in range(9):
                print i, j
                if (board[i][j] == '.'):
                    continue;
                num = ord(board[i][j]) - ord('1')
                if 0 == (~(lt[i]|rt[j]|bt[j/3*3+i/3]) & (1<<num)):
                    return False
                lt[i] |= 1 << num
                rt[j] |= 1 << num
                bt[j/3*3+i/3] |= 1 << num
        return True
    
