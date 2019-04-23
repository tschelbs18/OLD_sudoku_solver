# Functions

def fn_check_solutions(CellRow, CellCol, RowList, ColList, BoxList, initial_solutions):
    potential_solutions = []
    if RowList[CellRow][CellCol] != 0:
        potential_solutions = [RowList[CellRow][CellCol]]
        return potential_solutions
    else:
        potential_solutions = initial_solutions[:]
        for x in RowList[CellRow]:
            try:
                potential_solutions.remove(x)
            except: 
                pass
        for y in ColList[CellCol]:
            try:
                potential_solutions.remove(y)
            except: 
                pass
        for z in BoxList[fn_box_lookup(CellRow,CellCol)]:
            try:    
                potential_solutions.remove(z)
            except: 
                pass
    return potential_solutions
    
def fn_row_solutions (CellRow, CellCol, RowList, ColList, BoxList, initial_solutions): 
    row_solutions = []
    for y in range(0,9):
        if y != CellCol:
            potential_solutions = []
            potential_solutions = fn_check_solutions(CellRow, y, RowList, ColList, BoxList, initial_solutions)
            for val in potential_solutions:
                row_solutions.append(val)
    return row_solutions
    
def fn_col_solutions (CellRow, CellCol, RowList, ColList, BoxList, initial_solutions):
    col_solutions = []
    for x in range(0,9):
        if x != CellRow:
            potential_solutions = []
            potential_solutions = fn_check_solutions(x, CellCol, RowList, ColList, BoxList, initial_solutions)
            for val in potential_solutions:
                col_solutions.append(val)
    return col_solutions
    
def fn_box_solutions (CellRow, CellCol, RowList, ColList, BoxList, initial_solutions):
    box_solutions = []
    Box = fn_box_lookup(CellRow,CellCol)
    xy = fn_cells_lookup(Box)
    for y in range(xy[1], xy[1] + 3):    
        for x in range(xy[0], xy[0] + 3):
            if x != CellRow or y != CellCol:
                potential_solutions = []
                potential_solutions = fn_check_solutions(x, y, RowList, ColList, BoxList, initial_solutions)
                for val in potential_solutions:
                    box_solutions.append(val)
    return box_solutions
    
def fn_num_list(string_list):
    num_list = []
    for x in string_list:
        y = int(x)
        num_list.append(y)
    return num_list
    
def fn_col_list(Puzzle_Rows):
    Puzzle_Cols = []
    for y in range(0,9):
        col = []
        for x in range(0,9):
            z = Puzzle_Rows[x][y]
            col.append(z)
        Puzzle_Cols.append(col)
    return Puzzle_Cols
        
def fn_box_list(Puzzle_Rows):
    Puzzle_Boxes = [[],[],[],[],[],[],[],[],[]]
    for y in range(0,9):
        for x in range(0,9):
            z = Puzzle_Rows[x][y]
            box_num = fn_box_lookup(x,y)
            Puzzle_Boxes[box_num].append(z)
    return Puzzle_Boxes

# Returns the box where the cell resides
def fn_box_lookup(CellRow, CellCol):
    if CellRow <= 2:
        if CellCol <= 2:
            Box = 0
        elif CellCol <= 5:
            Box = 1
        else:
            Box = 2
    elif CellRow <= 5:
        if CellCol <= 2:
            Box = 3
        elif CellCol <= 5:
            Box = 4
        else:
            Box = 5
    else:
        if CellCol <= 2:
            Box = 6
        elif CellCol <= 5:
            Box = 7
        else:
            Box = 8
    return Box
    
# Returns the upper left most cell of the Box    
def fn_cells_lookup(Box):
    if Box == 0:
        xy = [0,0]
    elif Box == 1:
        xy = [0,3]
    elif Box == 2:
        xy = [0,6]
    elif Box == 3:
        xy = [3,0]
    elif Box == 4:
        xy = [3,3]
    elif Box == 5:
        xy = [3,6]
    elif Box == 6:
        xy = [6,0]
    elif Box == 7:
        xy = [6,3]
    elif Box == 8:
        xy = [6,6]
    return xy
    
