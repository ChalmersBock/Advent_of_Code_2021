import os
import sys

board_size = 5

class BingoBoard:
    line_length = board_size

    # Takes a list of 25 numbers representing the the bingo board
    def __init__(self, numbers):
        self.rows = []
        self.columns = []
        self.diagonals = []
        self.all_numbers = numbers

        for i in range(self.line_length):
            new_row = []
            for n in range(self.line_length):
                new_row.append(numbers[n + i*self.line_length])
            self.rows.append(new_row)

        for i in range(self.line_length):
            new_column = []
            for n in range(self.line_length):
                new_column.append(numbers[i + n * self.line_length])
            self.columns.append(new_column)

        new_diagonal = []
        for i in range(self.line_length):
            new_diagonal.append(numbers[i + (self.line_length * i)])
        self.diagonals.append(new_diagonal)

        new_diagonal = []
        for i in range(self.line_length):
            new_diagonal.append(numbers[(self.line_length - i - 1) + (self.line_length * i)])
        self.diagonals.append(new_diagonal)

    def all_marked(self, line, drawn_nbrs):
        return all(x in drawn_nbrs for x in line)

    def check_if_bingo(self, drawn_nbrs):
        for row in self.rows:
            if self.all_marked(row, drawn_nbrs):
                return True
        for column in self.columns:
            if self.all_marked(column, drawn_nbrs):
                return True
        for diagonal in self.diagonals:
            if self.all_marked(diagonal, drawn_nbrs):
                return True
        return False

    def get_non_picked_nbr_sum(self, drawn_nbrs):
        return sum(list(set(self.all_numbers) - set(drawn_nbrs)))

    def print_board(self):
        for row in self.rows:
            print(f'{row}')


def get_draw_numbers_and_boards(size):
    with open(os.path.join(sys.path[0], "data"), "r", encoding='utf-8') as file:
        draw_numbers = file.readline().rstrip().split(",")

        bingo_boards = []  # To store the board objects

        numbers_list = []  # For storing all numbers in the file
        for line in file.readlines():
            if line != "\n":
                line.rstrip()
                for x in line.split(" "):
                    if x != "":
                        numbers_list.append(int(x))

        # Split the list into 25 number chunks and create a board from each chunk
        for i in range(int(len(numbers_list)/size)):
            new_board_numbers = []
            for n in range(size):
                new_board_numbers.append(numbers_list[n + i*size])
            bingo_boards.append(BingoBoard(new_board_numbers))

    return (draw_numbers, bingo_boards)


def giant_squid_bingo_q1(size):
    draw_numbers, bingo_boards = get_draw_numbers_and_boards(size)
    drawn = []
    winning_board = None
    winning_number = -1

    # Draw numbers until a board gets bingo
    for number in draw_numbers:
        drawn.append(int(number))
        for board in bingo_boards:
            if board.check_if_bingo(drawn):
                winning_board = board
                break

        if winning_board:
            winning_number = int(number)
            break

    print(f'Answer Q1: {winning_number*winning_board.get_non_picked_nbr_sum(drawn)}')


def find_surviving_boards(boards, drawn):
    surviving_boards = []
    for board in boards:
        if not board.check_if_bingo(drawn):
            surviving_boards.append(board)
    return surviving_boards


def giant_squid_bingo_q2(size):
    draw_numbers, bingo_boards = get_draw_numbers_and_boards(size)
    drawn = []
    losing_board = None
    winning_number = -1

    # Draw numbers until a board gets bingo
    for number in draw_numbers:
        drawn.append(int(number))
        bingo_boards = find_surviving_boards(bingo_boards, drawn)

        # When we have one board left we know that it has lost
        if len(bingo_boards) == 1:
            losing_board = bingo_boards[0]

        # The draw that the number of surving boards become 0 is the draw when we should stop
        if len(bingo_boards) == 0:
            winning_number = int(number)
            break

    print(f'Answer Q2: {winning_number * losing_board.get_non_picked_nbr_sum(drawn)}')


if __name__ == '__main__':
    giant_squid_bingo_q1(board_size*board_size)
    giant_squid_bingo_q2(board_size*board_size)


