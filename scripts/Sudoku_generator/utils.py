from typing import List, Tuple, Set
from core import Cell
from random import sample, randint


def initialize() -> Tuple[List[List['Cell']], List[Set[int]], List[Set[int]], List[Set[int]]]:
    """
    Initializes the data structures for generating a Sudoku grid.

    Returns:
        Tuple containing:
        - box (List[List[Cell]]): A 9x9 grid of `Cell` objects with all values set to 0.
        - rows_opts (List[Set[int]]): List of sets representing available numbers for each row.
        - cols_opts (List[Set[int]]): List of sets representing available numbers for each column.
        - grids_opts (List[Set[int]]): List of sets representing available numbers for each 3x3 subgrid.
    """

    box = [[Cell(num=0) for col in range(9)] for row in range(9)]
    rows_opts = [set(range(1, 10)) for _ in range(9)]
    cols_opts = [set(range(1, 10)) for _ in range(9)]
    # suppose the grid order is like, first row, then col, like 
    # 1 2 3
    # 4 5 6
    grids_opts = [set(range(1, 10)) for _ in range(9)]
    return box, rows_opts, cols_opts, grids_opts


def choose_difficulty(diffs: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Prompts the user to choose a difficulty level and returns the corresponding (min, max) tuple.

    Parameters:
        diffs (List[Tuple[int, int]]): A list of tuples, each representing a difficulty level
                                       as a range (min, max) for deletion counts.

    Returns:
        Tuple[int, int]: The tuple corresponding to the selected difficulty.
    """

    text = """Which difficulty do you wish to play? (type the number please, like: 1)
    1) easy     2) medium   3) hard
    """
    while True:
        choice = input(text)

        if choice.strip() not in {"1", "2", "3"}:
            print("Please pay attention to the format and just write the number of your choice \n like: \n 1")
            continue

        else:
            diff_ind = int(choice) - 1 
            diff = diffs[diff_ind]
            return diff
        



def delete_numbers_for_start(solved_box: List[List['Cell']], diff: Tuple[int, int]) -> List[List['Cell']]:
    """
    Deletes numbers from a fully solved Sudoku board to generate a puzzle with empty cells
    based on a given difficulty level.

    Args:
        solved_box (List[List[Cell]]): A 9x9 grid of `Cell` objects representing a solved Sudoku puzzle.
        diff (Tuple[int, int]): A tuple representing the minimum and maximum number of cells to delete per row.

    Returns:
        List[List[Cell]]: A modified Sudoku grid with numbers removed according to the difficulty.
    """

    # based on the difficulty, choose how many cols numbers to delete for each row
    numb_of_cols_to_delete_for_each_row = [randint(*diff) for _ in range(9)]

    # based on the values computed, choose which columns to get deleted for each row
    indices_to_delete_for_each_row = [sample(range(9), num_del) for num_del in numb_of_cols_to_delete_for_each_row]

    # delete those columns (set the num attribute equal to 0)
    for i, col_indices in enumerate(indices_to_delete_for_each_row):
        for col_ind in col_indices:
            solved_box[i][col_ind].num = 0

    return solved_box