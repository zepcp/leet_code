from typing import List


class Solution:
    """
    Runtime: 832 ms, faster than 14.37% of Python3 online submissions for Sudoku Solver.
    Memory Usage: 22.2 MB, less than 5.17% of Python3 online submissions for Sudoku Solver.
    """
    sudoku_size = 9
    square_size = 3
    possible_values = [str(x) for x in range(1, sudoku_size + 1)]

    def get_line(self, board: List[List[str]], line: int) -> List:
        return board[line]

    def get_column(self, board: List[List[str]], column: int) -> List:
        return [line[column] for line in board]

    def square_group(self, value: int) -> (int, int):
        return (0, 2) if value in (0, 1, 2) else (3, 5) if value in (3, 4, 5) else (6, 8)

    def get_square(self, board: List[List[str]], line: int, column: int) -> List:
        line_min, line_max = self.square_group(line)
        column_min, column_max = self.square_group(column)

        values = []
        for line in board[line_min:line_max + 1]:
            values += line[column_min:column_max + 1]
        return values

    def get_options(self, existing_values):
        return [opt for opt in self.possible_values if opt not in existing_values]

    def solveDeterministic(self, board: List[List[str]]) -> bool:
        line, column, square_values, stuck = 0, 0, [], True
        while line < self.sudoku_size:
            line_values = self.get_line(board, line)
            if line % self.square_size == 0:
                square_values = self.get_square(board, line, column)

            column = 0
            while column < self.sudoku_size:
                column_values = self.get_column(board, column)
                if column % self.square_size == 0:
                    square_values = self.get_square(board, line, column)

                if board[line][column] == ".":
                    options = self.get_options(line_values + column_values + square_values)
                    if len(options) == 1:
                        board[line][column] = options[0]
                        stuck = False

                column += 1
            line += 1

        if not stuck:
            self.solveDeterministic(board)

        return False if [None for line in board if "." in line] else True

    def brute_force(self, board: List[List[str]], rollback: List):
        line, column, square_values = 0, 0, []
        while line < self.sudoku_size:
            line_values = self.get_line(board, line)

            column = 0
            while column < self.sudoku_size:
                column_values = self.get_column(board, column)
                square_values = self.get_square(board, line, column)

                if board[line][column] == ".":
                    options = self.get_options(line_values + column_values + square_values)
                    if not options:
                        last_action = rollback[-1]
                        if last_action["pick"] < len(last_action["options"]) - 1:
                            last_action["pick"] += 1
                            board[last_action["line"]][last_action["column"]] = last_action["options"][last_action["pick"]]
                            return self.brute_force(board, rollback)
                        else:
                            while True:
                                board[last_action["line"]][last_action["column"]] = "."
                                del rollback[-1]
                                last_action = rollback[-1]
                                if last_action["pick"] < len(last_action["options"]) - 1:
                                    break
                            last_action["pick"] += 1
                            board[last_action["line"]][last_action["column"]] = last_action["options"][last_action["pick"]]
                            return self.brute_force(board, rollback)
                    board[line][column] = options[0]
                    rollback.append({"line": line, "column": column, "options": options, "pick": 0})
                    return self.brute_force(board, rollback)

                column += 1
            line += 1
        return

    def solveSudoku(self, board: List[List[str]]) -> None:
        solved = self.solveDeterministic(board)
        if not solved:
            self.brute_force(board, [])

        return


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    print("BOARD_1")
    for x in board:
        print(x)

    Solution().solveSudoku(board)

    print("SOLUTION")
    for x in board:
        print(x)

    board = [[".",".","9","7","4","8",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","2",".","1",".","9",".",".","."],
             [".",".","7",".",".",".","2","4","."],
             [".","6","4",".","1",".","5","9","."],
             [".","9","8",".",".",".","3",".","."],
             [".",".",".","8",".","3",".","2","."],
             [".",".",".",".",".",".",".",".","6"],
             [".",".",".","2","7","5","9",".","."]]

    print("\n\nBOARD_2")
    for x in board:
        print(x)

    Solution().solveSudoku(board)

    print("SOLUTION")
    for x in board:
        print(x)
