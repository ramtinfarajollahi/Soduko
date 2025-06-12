from typing import List, Set
from random import choice


class Cell:
    """
    Represents a single cell in a Soduko grid

    Attributes:
    - num (int): The current number in the cell (0 if empty)
    - options Optional[Set[int]]: A set of possible numbers the cell can take based on the rules, used during solving.
    """

    def __init__(self, num: int):
        """
        Initializes a Cell object.

        Parameters:
        - num (int): The initial number in the cell (0 for empty).
        """

        self.num = num
        self.options = None

    def __repr__(self) -> str:
        """
        Returns a string representation of the cell's number.
        """

        return str(self.num)
    



def create_solved_box(
    box: List[List["Cell"]],
    rows_opts: List[Set[int]],
    cols_opts: List[Set[int]],
    grids_opts: List[Set[int]]
) -> List[List["Cell"]]:
    
    """
    Solves a Sudoku puzzle using a backtracking and Depth-First-Search (DFS) approach and fills in the provided box grid.

    Parameters:
        box (List[List[Cell]]): A 9x9 grid of Cell objects representing the Sudoku board.
        rows_opts (List[Set[int]]): A list of sets representing available numbers for each row.
        cols_opts (List[Set[int]]): A list of sets representing available numbers for each column.
        grids_opts (List[Set[int]]): A list of sets representing available numbers for each 3x3 subgrid.

    Returns:
        List[List[Cell]]: The filled and valid Sudoku board.
    """
    
    # boolean variable needed for changing indices of the cell using backtracking when at the first column
    row_up = False
    i = 0
    # iterating rows
    while i < 9:
        # finding the row index of 3*3 grid the current cell (we have total of 3 rows)
        grid_row = i // 3

        # move one row up, and to the last column
        if row_up:
            j = 8
            row_up = False
        # move to the left-most column
        else:
            j = 0

        # iterating columns
        while j < 9:
            cell = box[i][j]
            availible_options = cell.options

            # finding the column index of 3*3 grid the current cell (we have total of 3 columns)
            grid_col = j // 3
            grid_ind = (grid_row * 3) + grid_col

            # We have a total of 3 options:
            # 1- we have already expanded this cell and have other choices left
            # 2- we have already expanded this cell and exhausted all the options
            # 3- it is the first time expanding this cell, (the 0 cell)

            # Option 1:
            # It means we have already expanded this cell and have other choices left
            if availible_options:
            # these two are the same in this situation:
            # if isinstance(availible_options, list) and len(availible_options) > 0:     
                num = choice(list(availible_options))
                # remove this option, so that when we step back, we don't choose the same option again
                availible_options.remove(num)
                cell.options = availible_options

                # delete the previous chioce for this cell,
                # and add them for future uses
                prev_num = cell.num 
                rows_opts[i].add(prev_num)
                cols_opts[j].add(prev_num)
                grids_opts[grid_ind].add(prev_num)
                
                # add the new option to the cell
                # and delete it from options
                cell.num = num
                rows_opts[i].remove(num)
                cols_opts[j].remove(num)
                grids_opts[grid_ind].remove(num)

                # move to the next cell
                j += 1

            # Option 2:
            # It means we have already expanded this cell and exhausted all the options,
            # It means we have reached here by backtracking, and now we need to backtrack more
            elif availible_options == set():
                # back tracking
                # change the cell, as if it was never generated
                cell.options = None
                num = cell.num
                cell.num = 0
                rows_opts[i].add(num)
                cols_opts[j].add(num)
                grids_opts[grid_ind].add(num)
                # first column, needs to fall back to the row before and the last column
                if j == 0:
                    row_up = True
                    i -= 2
                    break
                    
                # not the first column, need to just fall back to the column before
                else:
                    j -= 1 
                    # note that we didn't need to write 'break', because we need to stay in the inner loop
                
            
            # Option 3:
            # It means it is the first time expanding this cell, (the 0 cells) 
            # it might find a solution and it might not 
            elif availible_options == None:

                # find which options are availible
                availible_options = grids_opts[grid_ind].intersection(rows_opts[i], cols_opts[j])

                # found a solution
                if availible_options:
                    num = choice(list(availible_options))
                    cell.num = num

                    # remove this option, so that when we step back, we don't choose the same option again
                    availible_options.remove(num)
                    # change the forntier from None to a set
                    cell.options = availible_options

                    rows_opts[i].remove(num)
                    cols_opts[j].remove(num)
                    grids_opts[grid_ind].remove(num)

                    j += 1
        
            
                # It means it is the first time expanding this cell, and no solution was found, need to backtrack:
                else:
                    if j == 0:
                        row_up = True
                        i -= 2
                        break 
                        
                    # not the first column, need to just fall back to the column before
                    else:
                        j -= 1 

                        # note that we didn't need to write 'break', because we need to stay in the inner loop 
            

        i += 1
            
    return box