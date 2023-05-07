def is_safe(board, row, col):
    N = len(board)
    
    # Check the same row to the left
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check the upper left diagonal
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check the lower left diagonal
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # If there is no queen in any of the above positions, it's safe to place a queen
    return True


def solve_n_queens(board, col):
    N = len(board)
    
    # If all queens are placed, print the board
    if col == N:
        for i in range(N):
            print(board[i])
        print("\n")
        return True

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack if placing the queen doesn't lead to a solution

    # If no solution is found, return false
    return False


# Initialize the board with zeros and call the solve_n_queens function to solve the problem
N = 8
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_n_queens(board, 0):
    print("No solution found")