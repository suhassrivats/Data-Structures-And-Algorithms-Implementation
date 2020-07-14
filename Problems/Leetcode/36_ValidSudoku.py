class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_set_list = [set() for _ in range(9)]
        cols_set_list = [set() for _ in range(9)]
        cube_set_list = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = board[i][j]

                # Make sure that same number doesn't exist in row, col and cube
                if ((num in rows_set_list[i]) or (num in cols_set_list[j]) or
                        (num in cube_set_list[i//3][j//3])):
                    return False
                else:
                    rows_set_list[i].add(num)
                    cols_set_list[j].add(num)
                    cube_set_list[i//3][j//3].add(num)
        return True
