# Find where to expand in minesweeper 

#Implement a function that turns neighbours of 0 to -2 when a user hits a 0 cell. Ignore when other cells are clicked 


def click(field, num_rows, num_cols, given_i, given_j):
    #BFS approach
    if(field[given_i][given_j]==0):
        expand=[(given_i,given_j)]
        #Only expand when 0 is clicked
        while expand:
            x,y=expand.pop(0)
            field[x][y]=-2
            for i in range(x-1,x+2):
                if(i>=0 and i<num_rows):
                    for j in range(y-1,y+2):
                        if(j>=0 and j<num_cols):
                            if(field[i][j]!=-1 and field[i][j]==0): #NOT BOMB
                                expand.append((i,j))
                            
                            
        
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
