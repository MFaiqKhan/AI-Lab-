import copy

def is_safe(board, row, col, n):
    # Check the row
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True


def n_queens_util(board, col, n):
    if col >= n:
        return [copy.deepcopy(board)]  # Create a deep copy of the board

    solutions = []

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            for solution in n_queens_util(board, col + 1, n):
                solutions.append(solution)
            board[i][col] = "."

    return solutions


def n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = n_queens_util(board, 0, n)

    # Print solutions as 2D matrices
    for solution in solutions:
        for row in solution:
            print(row)
        print()

    return solutions


# Run the code
n = 8
n_queens(n)


# runtime complexity: O(n^n)
# space complexity: O(n^2)
# time taken in my machine: 0.0009999275207519531 seconds