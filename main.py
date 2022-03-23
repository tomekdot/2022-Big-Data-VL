# Goal
# Your task is to implement an executable program, which will read two csv files, join them using a specified column
# and then write the result to the standard output.
# Users should be able to specify the join type (inner, left or right).
# Implementation should not rely on external libraries for joining the files.

# The program should be executed with a command: join file_path file_path column_name join_type
# Assumptions
# 1. Input files conform to the https://datatracker.ietf.org/doc/html/rfc4180
# 2. Header is always present
# 3. Rows may appear in any order
# 4. Each input file can be much bigger than there is available memory on the machine

# 1. Implement and argue for the default join type (if none specified)
# 2. Handle invalid parameters
# 3. Not testing something is also OK as long as the decision can be defended
# 4. Document the solution and important decisions you have

# !/usr/bin/env python3
# coding: utf-8
# Created By: Tomasz Kaczak

import sys
import csv


def join_csv(file_path_1, file_path_2, column_name, join_type):
    with open(file_path_1, 'r') as file_1, open(file_path_2, 'r') as file_2:
        reader_1 = csv.DictReader(file_1)
        reader_2 = csv.DictReader(file_2)
        if join_type == 'inner':
            return join_inner(reader_1, reader_2, column_name)
        elif join_type == 'left':
            return join_left(reader_1, reader_2, column_name)
        elif join_type == 'right':
            return join_right(reader_1, reader_2, column_name)
        else:
            raise ValueError('Wrong join type')


def join_inner(reader_1, reader_2, column_name):
    result = []
    for row_1 in reader_1:
        for row_2 in reader_2:
            if row_1[column_name] == row_2[column_name]:
                result.append(row_1)
                result.append(row_2)
    return result


def join_left(reader_1, reader_2, column_name):
    result = []
    for row_1 in reader_1:
        for row_2 in reader_2:
            if row_1[column_name] == row_2[column_name]:
                result.append(row_1)
                result.append(row_2)
                break
    return result


def join_right(reader_1, reader_2, column_name):
    result = []
    for row_1 in reader_1:
        for row_2 in reader_2:
            if row_1[column_name] == row_2[column_name]:
                result.append(row_1)
                result.append(row_2)
                break
    return result


def main():
    if len(sys.argv) != 5:
        raise ValueError('Wrong number of arguments')
    file_path_1 = sys.argv[1]
    file_path_2 = sys.argv[2]
    column_name = sys.argv[3]
    join_type = sys.argv[4]
    result = join_csv(file_path_1, file_path_2, column_name, join_type)
    for row in result:
        print(row)


if __name__ == '__main__':
    main()