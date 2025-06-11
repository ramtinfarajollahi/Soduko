from random import sample, randint, choice

easy = (3, 5)
medium = (4, 7)
hard = (5, 8)

class Cell:
    def __init__(self, num, pos, prev_cell=None):
        self.num = num
        self.options = None

    def __repr__(self):
        return str(self.num)


def delete_numbers_for_start(solved_box, diff):
    # based on the difficulty, choose how many cols numbers to delete for each row
    numb_of_cols_to_delete_for_each_row = [randint(*diff) for _ in range(9)]

    # based on the values computed, choose which columns to get deleted for each row
    indices_to_delete_for_each_row = [sample(range(9), num_del) for num_del in numb_of_cols_to_delete_for_each_row]

    # delete those columns (set the num attribute equal to 0)
    for i, col_indices in enumerate(indices_to_delete_for_each_row):
        for col_ind in col_indices:
            solved_box[i][col_ind].num = 0

    return solved_box



def initialize():
    box = [[Cell(num=0, pos=(row, col)) for col in range(9)] for row in range(9)]
    rows_opts = [set(range(1, 10)) for _ in range(9)]
    cols_opts = [set(range(1, 10)) for _ in range(9)]
    # suppose the grid order is like, first row, then col, like 
    # 1 2 3
    # 4 5 6
    grids_opts = [set(range(1, 10)) for _ in range(9)]
    return box, rows_opts, cols_opts, grids_opts

        

def create_solved_box(box, rows_opts, cols_opts, grids_opts):
    # boolean variable needed for changing indices of the cell using backtracking when at the first column
    row_up = False
    i = 0
    # iterating rows
    while i < 9:
        # finding the row index of 3*3 grid the current cell (we have total of 3 rows)
        grid_row = i // 3

        # move one row up, and last column
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


# if this script gets run directly, and not imported
if __name__ == "__main__":
    for row in create_solved_box(*initialize()):
        print(row)


# # FIRST WAY:

# # kar mikone, bedune backtracking
# def create_solved_box():
#     box = []
#     # create a set for each column to check for iterations faster 
#     checked_cols = [set() for _ in range(9)]
#     for _ in range(9):
#         checked = set()
#         # randomly create permutation of the new row, until it matches the 3 rules 
#         while True:
#             permuted = sample(range(1, 10), 9)
#             permuted_tuple = tuple(permuted)   # for hashing in sets
#             if permuted_tuple not in checked:
#                 if creation_validation(box, permuted, checked_cols):
#                     box.append(permuted)
#                     # add the value of the new row to the corresponding column set, for future checking
#                     for i, val in enumerate(permuted):
#                         checked_cols[i].add(val)
#                     break
#                 else:
#                     checked.add(permuted_tuple)
#     for row in box:
#         print(row)
#     print()

#     return box


# SECOND WAY: back

# gets stuck mostly at 7 rows completion and moves back and forth between row 4 and 7
# def create_solved_box():
#     box = []
#     # create a set for each column to check for iterations faster 
#     checked_cols = [set() for _ in range(9)]
#     # number of tries before changin the last modified row
#     tries = 10000
#     while True:
#         # this loop is for creation of 9 rows
#         k = 0
#         while k < 9: 
#             count = 0
#             checked = set()
#             # needed to make a new boolean variable, 
#             # to break from this loop easier
#             found_valid_row = False

#             # randomly create permutation of the new row, until it matches the 3 rules 
#             # or number of options generated exceeds the number of maximum tries 
#             while count < tries:
#                 permuted = sample(range(1, 10), 9)
#                 permuted_tuple = tuple(permuted)   # for hashing in sets
#                 if permuted_tuple not in checked:
#                     if creation_validation(box, permuted, checked_cols):
#                         box.append(permuted)
#                         # add the value of the new row to the corresponding column set, for future checking
#                         for i, val in enumerate(permuted):
#                             checked_cols[i].add(val)
#                         found_valid_row = True
#                         break
#                     else:
#                         checked.add(permuted_tuple)
#                 count += 1
#             if found_valid_row:
#                 k += 1
#             else:
#                 # removes the last row generated and validated 
#                 # in the previous iteration from the box 
#                 if k == 0:
#                     print("the solution has started over from scratch")
#                     break

#                 # backtrack
#                 last_row = box.pop()
#                 for i, val in enumerate(last_row):
#                     checked_cols[i].remove(val)
#                 k -= 1
#                 print(f"backtracked to row {k}")
        
#         if len(box) == 9:
#             # breaking the most outer loop (while True)
#             break


#     for row in box:
#         print(row)

#     return box

# create_solved_box()



# HELPER FUNCTIONS FOR THE FIRST AND SECOND METHOD:

# def check_for_columns(new_row, checked_cols):
#     if any(new_row[i] in checked_col for i, checked_col in enumerate(checked_cols)):
#         return False
#     return True

#     # mishod daqiqan 4 khate balaro intori ham goft:

#     # check for iterations in columns
#     # for i in range(rows):
#     #     for j in range(9):
#     #         if new_row[j] == box[i][j]:
#     #             return False


# def check_for_small_square(box, new_row):
#     rows = len(box)

#     # adding it to make checking for squares eaesier
#     tmp_box = box + [new_row]

#     # no need to loop for box rows, because they've been already checked before
#     box_i = (rows) // 3
#     k_range = (rows + 1) % 3 or 3
#     # the first row of the new box, no need to check
#     if k_range == 1:
#         return True
#     for box_j in range(3):
#         seen = set()
#         # row inside the box
#         for k in range(k_range):
#             # col inside the box
#             for h in range(3):
#                 val = tmp_box[3 * box_i + k][3 * box_j + h]
#                 if val in seen:
#                     return False
#                 seen.add(val)
#     return True
#     # rows        rows + 1    index_max   box_i   k_range
#     # 3           4           3           1       1   4 % 3             check nemikhad
#     # 4           5           4           1       2 = 5 % 3
#     # 5           6           5           1       0 = 6 % 3             vali lazeme 3 baseh, pas or 3 gozasthim bala
#     # 6           7           6           2       1 = 7 % 3             check nemikhad



# def creation_validation(box, new_row, checked_cols):
#     # for the first iteration where the box is empty
#     if not box:
#         return True
    
#     if not check_for_columns(new_row, checked_cols):
#         return False
#     if not check_for_small_square(box, new_row):
#         return False
#     return True
