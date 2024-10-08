def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    boxes = [set() for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            if num in rows[i]:
                return False
            rows[i].add(num)

            if num in cols[j]:
                return False
            cols[j].add(num)

            box_idx = (i // 3) * 3 + (j // 3)
            if num in boxes[box_idx]:
                return False
            boxes[box_idx].add(num)

    return True