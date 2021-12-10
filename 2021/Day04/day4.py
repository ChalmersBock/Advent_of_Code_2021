import os
import sys


class BingoBoard:
    line_length = 5  # Hardcoded size of a line

    # Takes a list of 25 numbers representing the the bingo board
    def __init__(self, numbers):
        self.rows = []
        self.columns = []
        self.all_numbers = numbers

        for i in range(self.line_length):
            new_row = []
            for j in range(self.line_length):
                new_row.append(numbers[j + i*self.line_length])
            self.rows.append(new_row)

        for i in range(self.line_length):
            new_column = []
            for j in range(self.line_length):
                new_column.append(numbers[i + j * self.line_length])
            self.columns.append(new_column)

    @staticmethod
    def all_marked(line, drawn_numbers):
        return all(x in drawn_numbers for x in line)

    def check_if_bingo(self, drawn_numbers):
        for row in self.rows:
            if self.all_marked(row, drawn_numbers):
                return True
        for column in self.columns:
            if self.all_marked(column, drawn_numbers):
                return True
        return False

    def get_non_picked_nbr_sum(self, drawn_numbers):
        return sum(list(set(self.all_numbers) - set(drawn_numbers)))


def get_draw_numbers_and_boards():
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        draw_numbers = file.readline().rstrip().split(",")
        bingo_boards = []  # To store the board objects
        numbers_list = []  # For storing all numbers in the file

        for line in file.readlines():
            if line != "\n":
                line.rstrip()
                for i in line.split(" "):
                    if i != "":
                        numbers_list.append(int(i))

        size = 25  # Hardcoded size of boards
        # Split the list into 25 number chunks and create a board from each chunk
        for i in range(int(len(numbers_list)/size)):
            new_board_numbers = []
            for j in range(size):
                new_board_numbers.append(numbers_list[j + i*size])
            bingo_boards.append(BingoBoard(new_board_numbers))

    return draw_numbers, bingo_boards


def winning_board(draw_numbers, bingo_boards, first_bingo):
    drawn = []
    selected_board = None
    boards = bingo_boards
    winning_number = -1

    for number in draw_numbers:
        drawn.append(int(number))

        without_bingo_boards = []
        for board in boards:
            if not board.check_if_bingo(drawn):
                without_bingo_boards.append(board)
            elif first_bingo:
                selected_board = board
                break

        if (first_bingo and selected_board) or len(without_bingo_boards) == 0:
            winning_number = int(number)
            break

        if len(without_bingo_boards) == 1:
            selected_board = without_bingo_boards[0]

        boards = without_bingo_boards

    winner_score = winning_number * selected_board.get_non_picked_nbr_sum(drawn)
    if first_bingo:
        print(f'Answer Q1 (First bingo score): {winner_score}')
    else:
        print(f'Answer Q2 (Last bingo score): {winner_score}')


if __name__ == '__main__':
    _draw_numbers, _bingo_boards = get_draw_numbers_and_boards()
    winning_board(_draw_numbers, _bingo_boards, True)
    winning_board(_draw_numbers, _bingo_boards, False)


