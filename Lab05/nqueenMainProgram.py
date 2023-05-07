class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]: # takes in an integer n and returns a list of list of strings
        col = set() # a set of columns to store the columns that have been used
        posDiag = set()  # (row + col) , positive diagonals also known as upper diagonals
        negDiag = set()  # (row - col) , negative diagonals also known as lower diagonals

        res = [] # a list of list of strings to store the solutions
        board = [["." for _ in range(n)] for _ in range(n)] # a 2D list of strings to store the board

        """
         printBoard function: This function takes the current board as input and prints it in a human-readable format.
        """

        def printBoard(board):
            for row in board:
                print(" ".join(row))
            print("\n")

        def backtrack(r): # a recursive function that takes in a row number r
            if r == n: # if r is equal to n, we have reached the end of the board means solution found
                copy = ["".join(row) for row in board] # create a copy of the board
                res.append(copy) # append the copy to the res list
                print("Solution found:")
                printBoard(board)
                #print(f"Current solutions: {res}")
                return
            
            """
            Check if placing a queen in the current cell would result in an attack 
            (i.e., if the column, positive diagonal, or negative diagonal is already occupied). 
            If so, skip this cell and continue to the next column.
            Otherwise, place the queen in the current cell and update the col, posDiag, and negDiag sets.
            Print the updated board using the printBoard function.
            Call the backtrack function for the next row (r + 1).
            Backtrack: Remove the queen from the current cell, update the col, posDiag, and negDiag sets, 
            and print the updated board using the printBoard function.
            """

            for c in range(n): # for each column in the board, in range[0, n) means 0 to n-1
                if c in col or (r + c) in posDiag or (r - c) in negDiag: 
                    continue 
                # if the column, positive diagonal, or negative diagonal is already occupied, 
                # skip this cell and continue to the next column 
                # next column means next iteration of the for loop e.g
                # for c in range(8):
                #   if c in col or (r + c) in posDiag or (r - c) in negDiag:
                #       continue
                # lets say c = 0, r = 0
                # if 0 in col or (0 + 0) in posDiag or (0 - 0) in negDiag:
                #   continue
                # if not then place the queen in the current cell and update the col, posDiag, and negDiag sets.
                # continue will skip the below code and go to the next iteration of the for loop

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                #print(f"Placing queen at row {r}, col {c}:")
                #printBoard(board)

                backtrack(r + 1) # why ? because we are placing the queen in the next row r + 1 
                # if sol is found then backtrack will return and we will remove the queen from the current cell

                col.remove(c) # why ? because we are backtracking and removing the queen from the current cell
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

                #print(f"Backtracking at row {r}, col {c}:")
                #printBoard(board)

        backtrack(0)
        return res

# run the code
n = 8
print(Solution().solveNQueens(n))


""" 
. . Q . . . . .
. . . . Q . . .
. Q . . . . . .
. . . . . . . Q
. . . . . Q . .
. . . Q . . . .
. . . . . . Q .
Q . . . . . . .

 """


""" 
Initialize an empty board, col, posDiag, and negDiag sets.

Call backtrack(0).

For row 0, try placing the queen in the first column (0, 0). Update col, posDiag, and negDiag. Call backtrack(1).

For row 1, placing the queen in columns 0 and 1 would result in an attack, so skip them. Place the queen in column 2 (1, 2). Update col, posDiag, and negDiag. Call backtrack(2).

For row 2, placing the queen in column 0 would result in an attack, so skip it. Place the queen in column 1 (2, 1). Update col, posDiag, and negDiag. Call backtrack(3).

For row 3, placing the queen in columns 0, 1, and 2 would result in an attack, so skip them. Place the queen in column 3 (3, 3). Update col, posDiag, and negDiag.

Now, r == n (4 == 4), so a solution is found. Add the current board configuration to res. The board looks like:
"""

""" 
Q . . .
. . Q .
. Q . .
. . . Q
"""

# After finding the solution, the algorithm backtracks. means algorithm will contonue the code from where it left off, 
# it will remove the col and posDiag and negDiag and update the board
# Remove the queen from the last placed cell (3, 3) and update col, posDiag, and negDiag. The board now looks like:

""" 
Q . . .
. . Q .
. Q . .
. . . .

"""

""" 
Continue searching for other valid configurations in previous rows. 
The search will eventually find another solution, and the process repeats.
"""

""" 
The code board = [["." for _ in range(n)] for _ in range(n)] is a nested list 
comprehension that creates a square 2D matrix of size n x n and initializes all its 
elements with the character ".". The outer loop iterates n times, creating a new list for 
each row, and the inner loop iterates n times as well, filling the row with ".".

Here's a breakdown of the code:

for _ in range(n): This outer loop iterates n times, where _ is a throwaway variable, 
indicating that we don't need its value in the loop.

["." for _ in range(n)]: This inner loop also iterates n times, and for each iteration, 
it adds a "." to the list. This creates a row of n "." characters.

[... for _ in range(n)]: The outer loop creates a list of the inner lists (rows), 
resulting in a 2D matrix of size n x n.

In the context of the N-Queens problem, this code creates an empty chessboard, 
where each cell is represented by a ".". The board will be later updated with the character 
"Q" to represent the position of the queens.
"""