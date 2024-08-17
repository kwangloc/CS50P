def find_next_empty(puzzle):
    # 0 == empty
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # check row
    if guess in puzzle[row]:
        return False

    # check col
    for row in range(9):
        if puzzle[row][col] == guess:
            return False
        
    # check 3x3 square

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None: 
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            solve_sudoku(puzzle)


def main():
    # puzzle = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]

    # print(solve_sudoku(puzzle))

    print(0 == None)

if __name__ == '__main__':
    main()

