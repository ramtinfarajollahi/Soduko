def check_for_columns(new_row, checked_cols):
    if any(new_row[i] in checked_col for i, checked_col in enumerate(checked_cols)):
        return False
    return True

    # mishod daqiqan 4 khate balaro intori ham goft:

    # check for iterations in columns
    # for i in range(rows):
    #     for j in range(9):
    #         if new_row[j] == box[i][j]:
    #             return False


def check_for_small_square(box, new_row):
    rows = len(box)

    # adding it to make checking for squares eaesier
    tmp_box = box + [new_row]

    # no need to loop for box rows, because they've been already checked before
    box_i = (rows) // 3
    k_range = (rows + 1) % 3 or 3
    # the first row of the new box, no need to check
    if k_range == 1:
        return True
    for box_j in range(3):
        seen = set()
        # row inside the box
        for k in range(k_range):
            # col inside the box
            for h in range(3):
                val = tmp_box[3 * box_i + k][3 * box_j + h]
                if val in seen:
                    return False
                seen.add(val)
    return True
    # rows        rows + 1    index_max   box_i   k_range
    # 3           4           3           1       1   4 % 3             check nemikhad
    # 4           5           4           1       2 = 5 % 3
    # 5           6           5           1       0 = 6 % 3             vali lazeme 3 baseh, pas or 3 gozasthim bala
    # 6           7           6           2       1 = 7 % 3             check nemikhad