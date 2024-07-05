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

    def reject_sol(x, y):
        """Determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(sol[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_sol(x):
        """Clears the answer from the point of falure on"""
        for i in range(x, n):
            sol[i][1] = None

    def nqueens(x):
        """Recursive backtracking function to find the solution"""
        for y in range(n):
            clear_sol(x)
            if reject_sol(x, y):
                sol[x][1] = y
                if (x == n - 1):
                    print(sol)
                else:
                    nqueens(x + 1)
    nqueens(0)
