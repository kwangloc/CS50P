'''
- solving Sudoku using backtracking algorithm
- puzzle 9x9: 2D list of integers where each inner list is a row in puzzle
- return whether a solution exists
- mutates puzzle to be the solution (if solution exists)

- Idea: try every possible situations
- Step 1: choose a empty on the puzzle to make a guess
- Step 2: make a guess from [1,9], recursively call the function

'''

def display_puzzle(puzzle):
    for r in range(9):
        for c in range(9):
            print(puzzle[r][c], end=' ')
        print()
    print()

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our list indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    
    # check row
    if guess in puzzle[row]:
        return False
    
    # check column
    for r in range(9):
        if puzzle[r][col] == guess:
            return False
        
    # check 3x3 square, there are 9 squares in a puzzle
    # figure out where in the 3x3 square we are
    # find the starting index (row/col) of the 3x3 square

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # print("valid")
    return True

def solve_sudoku(puzzle):
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None: 
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if valid, place that guess on puzzle
            puzzle[row][col] = guess
            # step 4: recursively call the function 
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid or if the guess doesn't solve puzzle, we backtrack and try a new guess
        puzzle[row][col] = 0 # mark as empty

    # step 6: possible cases
    # 1. this approach is wrong -> backtrack
    # 2. all guesses wrong -> no solutions
    print("Reach false")
    return False

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

    puzzle = [
        [3, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 1, 9, 0, 8, 0],
        [0, 5, 0, 0, 6, 8, 0, 0, 0],
        [2, 0, 6, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 7, 0, 1, 0, 5, 0, 4, 0],
        [1, 0, 9, 0, 0, 0, 2, 0, 0]
    ]

    print("Original puzzle:")
    display_puzzle(puzzle)
    # for r in range(9):
    #     for c in range(9):
    #         print(puzzle[r][c], end=" ")
    #     print()

    print(solve_sudoku(puzzle))
    print("Solved puzzle:")
    display_puzzle(puzzle)
    


if __name__ == '__main__':
    main()
