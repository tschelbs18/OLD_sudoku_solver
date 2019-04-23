# Sudoku Solver V1
# Author: Ted Schelble

import time
import sudoku_functions as sf

# Open Puzzle to Solve
# Make this dynamic later either select a txt file with a puzzle
#  or input your own puzzle using a gui
# http://websudoku.com/solutions/Evil_4,755,634,211.htm 
# ^ Evil Puzzle Solution, Step 14 is where the program gets hung

path = r'Puzzles'
input_puzzle = r'\sudoku4_hard.txt'

# Load data
input_puzzle_rows = open(path + input_puzzle)
Puzzle_Rows = []
Puzzle_Cols = []
Puzzle_Boxes = [[],[],[],[],[],[],[],[],[]]

# Test load
# Add functionality here to confirm all integers 0-9 input and that puzzle is 9x9
for line in input_puzzle_rows:
    row = str(line).replace("\n", '').split('|')
    # print(line) #base puzzle rows "|" delimited
    print(row) #list of inputs
    row_as_num = sf.fn_num_list(row)
    Puzzle_Rows.append(row_as_num[:])
    # time.sleep(1)
    
# Create columns and boxes list
Puzzle_Boxes = sf.fn_box_list(Puzzle_Rows)
Puzzle_Cols = sf.fn_col_list(Puzzle_Rows)


# Initialize base variables
initial_solutions = list(range(1,10))
Solved = False
iterations = 0


# Main Loop
while Solved == False:
    
    for x in range(0,9):
        for y in range(0,9):
            cell_solutions = []
            row_solutions = []
            col_solutions = []
            box_solutions = []
            cell_solutions = sf.fn_check_solutions(x,y,Puzzle_Rows,Puzzle_Cols,Puzzle_Boxes, initial_solutions)
            if len(cell_solutions) == 1 and Puzzle_Rows[x][y] == 0:
                # Update Rowlist to account for determined value
                Puzzle_Rows[x][y] = cell_solutions[0]
                
                # Reconfigure the ColList and BoxList
                Puzzle_Boxes = sf.fn_box_list(Puzzle_Rows)
                Puzzle_Cols = sf.fn_col_list(Puzzle_Rows)
                
            elif len(cell_solutions) > 1 and Puzzle_Rows[x][y] == 0:
                row_solutions = sf.fn_row_solutions(x,y,Puzzle_Rows,Puzzle_Cols,Puzzle_Boxes, initial_solutions)
                for val in cell_solutions:
                    if val not in row_solutions:
                        # Update Rowlist to account for determined value
                        Puzzle_Rows[x][y] = val
                        
                        # Reconfigure the ColList and BoxList
                        Puzzle_Boxes = sf.fn_box_list(Puzzle_Rows)
                        Puzzle_Cols = sf.fn_col_list(Puzzle_Rows)
                        
                if Puzzle_Rows[x][y] == 0:
                    col_solutions = sf.fn_col_solutions(x,y,Puzzle_Rows,Puzzle_Cols,Puzzle_Boxes, initial_solutions)
                    for val in cell_solutions:
                        if val not in col_solutions:
                            # Update Rowlist to account for determined value
                            Puzzle_Rows[x][y] = val
                            
                            # Reconfigure the ColList and BoxList
                            Puzzle_Boxes = sf.fn_box_list(Puzzle_Rows)
                            Puzzle_Cols = sf.fn_col_list(Puzzle_Rows)   
                        
                if Puzzle_Rows[x][y] == 0:
                    box_solutions = sf.fn_box_solutions(x,y,Puzzle_Rows,Puzzle_Cols,Puzzle_Boxes, initial_solutions)
                    for val in cell_solutions:
                        if val not in box_solutions:
                            # Update Rowlist to account for determined value
                            Puzzle_Rows[x][y] = val
                            
                            # Reconfigure the ColList and BoxList
                            Puzzle_Boxes = sf.fn_box_list(Puzzle_Rows)
                            Puzzle_Cols = sf.fn_col_list(Puzzle_Rows)                            

            #~ print(cell_solutions)
            #~ print(row_solutions)
            #~ print(col_solutions)
            #~ print(box_solutions)
            # time.sleep(.25)
            # Break the loop if iterations hits over 1k
            iterations = iterations + 1
            print(iterations)
    if iterations >= 1000:
        Solved = True
        print(str(iterations) + " iterations performed before solving.")
               
print("Partially solved or solved puzzle below...")
                
for x in range(0,9):
    print(Puzzle_Rows[x])


