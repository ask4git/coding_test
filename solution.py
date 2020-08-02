#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임
url: https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
"""


class Board:
    def __init__(self):
        self.data = []

    def __getitem__(self, item):
        print(self.data)

    def push(self, item):
        if item != 0:
            self.data.append(item)

    def pop(self):
        if self.empty():
            return -1
        return self.data.pop()

    def empty(self):
        if self.data:
            return False
        return True


class ResultBoard(Board):
    def __init__(self):
        super().__init__()
        self.num_of_deleted = 0

    def push(self, _item):
        if _item != -1:
            self.data.append(_item)
        self.delete_item()

    def delete_item(self):
        while True:
            if len(self.data) < 2:
                break
            if self.is_same_item():
                self.pop()
                self.pop()
                self.num_of_deleted += 2
            else:
                break

    def is_same_item(self):
        if len(self.data) < 2:
            return False
        tail_index = len(self.data) - 1
        if self.data[tail_index] == self.data[tail_index - 1]:
            return True
        return False


def solution(board, moves):

    # initialize
    board_data = [Board() for i in range(len(board))]
    result_data = ResultBoard()

    # set input data
    for row_value in reversed(board):
        for col_index, col_value in enumerate(row_value):
            board_data[col_index].push(col_value)

    # move
    for move in moves:
        v = board_data[move - 1].pop()
        result_data.push(v)

    return result_data.num_of_deleted


def main():
    test_case_board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    test_case_moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(test_case_board, test_case_moves))


if __name__ == '__main__':
    main()