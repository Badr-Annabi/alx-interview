#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on anN×N chessboard
"""


from sys import argv

if __name__ == "__main__":
    sol = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        sol.append([i, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == sol[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(sol[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""
        for i in range(x, n):
            sol[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                sol[x][1] = y
                if (x == n - 1):
                    print(sol)
                else:
                    nqueens(x + 1)

    nqueens(0)
