def solve_n_queens(n):
    def is_safe(row, col, diagonals, anti_diagonals, cols):
        return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

    def backtrack(row, diagonals, anti_diagonals, cols, board, solutions):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col, diagonals, anti_diagonals, cols):
                board[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                
                backtrack(row + 1, diagonals, anti_diagonals, cols, board, solutions)
                
                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

    solutions = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board, solutions)
    return solutions

n = 4
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in solution:
        print(row)
    print()
