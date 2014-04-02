'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        lt, rt, bt = [0] * 9, [0] * 9, [0] * 9
        self.dt = {}
        for i in range(9): self.dt[1<<i] = chr(ord('1')+i)
        for i in range(9):
            board[i] = list(board[i])
            for j in range(9):
                if (board[i][j] == '.'):
                    continue;
                num = ord(board[i][j]) - ord('1')
                lt[i] |= 1 << num
                rt[j] |= 1 << num
                bt[j//3*3+i//3] |= 1 << num
        self.dfs(board, 0, lt, rt, bt)
        board = [''.join(s) for s in board]
    
    def dfs(self, board, p, lt, rt, bt):
        while p < 81 and board[p/9][p%9] != '.':
            p += 1
        if p == 81:
            return True
        i, j, k = p//9, p%9, p%9//3*3+p//9//3
        if board[i][j] != '.':
            self.dfs(board, p + 1, lt, rt, bt)
            return True
        can = (~(lt[i]|rt[j]|bt[k])) & (0x1ff)
        pre = board[i]
        while can:
            num = can&-can
            board[i][j] = self.dt[num]
            lt[i] |= num
            rt[j] |= num
            bt[k] |= num
            if self.dfs(board, p + 1, lt, rt , bt):
                return True
            board[i][j] = '.'
            lt[i] &= ~num
            rt[j] &= ~num
            bt[k] &= ~num
            can -= num
        return False
    
  
    
