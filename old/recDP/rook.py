
# size n board then the number of moves
def num_of_moves(n):

    # n * n chessboard
    dp = [ [ 0 for i in range(n) ] for j in range(n)] 

    # set all the cells in the 0th row and 0th column to 1
    for i in range(n):
        dp[0][i] = 1
        dp[i][0] = 1


    # for each cell, the rook can either arrive at the current cell either from 
    # the cell just on top of it vertically or just to the left of it 
    # (we are moving from top to bottom left to right)
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 
    
    
    #return the answer in the last cell (diagonally opposite)
    return dp[n - 1][n - 1]

print(num_of_moves(8)) # 3432
    