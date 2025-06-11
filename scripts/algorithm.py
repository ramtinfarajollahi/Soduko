from random import sample
from helpers import check_for_columns, check_for_small_square

def creation_validation(box, new_row, checked_cols):
    # for the first iteration where the box is empty
    if not box:
        return True
    
    if not check_for_columns(new_row, checked_cols):
        return False
    if not check_for_small_square(box, new_row):
        return False
    return True


# kar mikone, bedune backtracking
def create_solved_box():
    box = []
    # create a set for each column to check for iterations faster 
    checked_cols = [set() for _ in range(9)]
    for _ in range(9):
        checked = set()
        # randomly create permutation of the new row, until it matches the 3 rules 
        while True:
            permuted = sample(range(1, 10), 9)
            permuted_tuple = tuple(permuted)   # for hashing in sets
            if permuted_tuple not in checked:
                if creation_validation(box, permuted, checked_cols):
                    box.append(permuted)
                    # add the value of the new row to the corresponding column set, for future checking
                    for i, val in enumerate(permuted):
                        checked_cols[i].add(val)
                    break
                else:
                    checked.add(permuted_tuple)
    for row in box:
        print(row)

create_solved_box()

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


