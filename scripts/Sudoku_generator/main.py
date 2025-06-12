from core import create_solved_box
from utils import choose_difficulty, initialize, delete_numbers_for_start
from config import DIFFICULTIES

if __name__ == "__main__":
    diff = choose_difficulty(DIFFICULTIES)

    print("The complete Sudoku:")
    solved_box = create_solved_box(*initialize())
    for row in solved_box:
        print(row)

    print("\nSudoku with deleted numbers:")
    for row in delete_numbers_for_start(solved_box, diff):
        print(row)
