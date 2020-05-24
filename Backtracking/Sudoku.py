class Solution:
    # @param A : list of list of chars
    def solveSudoku(self, sudoku):
        def isSafe(number,r,c):
            #check rows 
            for i in range(9):
                if(sudoku[r][i]==number):
                    return False
            #check cols
            for i in range(9):
                if(sudoku[i][c]==number):
                    return False
            
            #check box
            box_start_i=3*(r//3)
            box_start_j=3*(c//3)
            for i in range(box_start_i,box_start_i+3):
                for j in range(box_start_j,box_start_j+3):
                    if(sudoku[i][j]==number):
                        return False
                        
            return True
            
        
        def sudokuSolver(row,col):
            if(row==9):
                #sudoku solved
                return True
            if(col==9):
                return sudokuSolver(row+1,0) #solve it for next col
            
            if(sudoku[row][col]!="."):
                #not empty
                return sudokuSolver(row,col+1)
            for number in range(1,10):
                if(isSafe(str(number),row,col)):
                    sudoku[row][col]=str(number) #place number
                    if(sudokuSolver(row,col+1)):
                        return True
                    sudoku[row][col]="." #unplace number since it wasn't safe to place it
                        
                        
            return False
        
        
        sudokuSolver(0,0)
        
