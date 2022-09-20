#!/usr/bin/python3

"""
This is a module for N queens.
"""


if __name__ == '__main__':

    import sys
    import copy

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except BaseException:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    def get_board(size):
        """Returns an n by n board"""
        board = [0] * size
        for ix in range(size):
            board[ix] = [0] * size
        return board

    def print_solutions(solutions, size):
        """Prints all the solutions in user friendly way"""
        new = []
        for sol in solutions:
            tmp = []
            for i, row in enumerate(sol):
                inner = []
                for j, num in enumerate(row):
                    if num == 1:
                        inner.append(j)
                        inner.append(i)
                tmp.append(inner)
            new.append(tmp)
        for ans in new:
            print(ans)

    def is_safe(board, row, col, size):
        """Check if it's safe to place a queen at board[x][y]"""

        # check row on left side
        for iy in range(col):
            if board[row][iy] == 1:
                return False

        ix, iy = row, col
        while ix >= 0 and iy >= 0:
            if board[ix][iy] == 1:
                return False
            ix -= 1
            iy -= 1

        jx, jy = row, col
        while jx < size and jy >= 0:
            if board[jx][jy] == 1:
                return False
            jx += 1
            jy -= 1

        return True

    def solve(board, col, size):
        """Use backtracking to find all solutions"""
        # base case
        if col >= size:
            return

        for i in range(size):
            if is_safe(board, i, col, size):
                board[i][col] = 1
                if col == size - 1:
                    add_solution(board)
                    board[i][col] = 0
                    return
                solve(board, col + 1, size)
                # backtrack
                board[i][col] = 0

    def add_solution(board):
        """Saves the board state to the global variable 'solutions'"""
        global solutions
        saved_board = copy.deepcopy(board)
        solutions.append(saved_board)

    board = get_board(size)
    solutions = []
    solve(board, 0, size)

    print_solutions(solutions, size)
