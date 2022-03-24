# !/usr/bin/env python3
# coding: utf-8
# Created By: Tomasz Kaczak


import csv
import sys
import argparse


def join_csv(file_path_1, file_path_2, column_name, join_type):
    with open(file_path_1, 'r') as file_1, open(file_path_2, 'r') as file_2:
        reader_1 = csv.DictReader(file_1)
        reader_2 = csv.DictReader(file_2)
        if join_type == 'inner':
            join_inner(reader_1, reader_2, column_name)
        elif join_type == 'left':
            join_left(reader_1, reader_2, column_name)
        elif join_type == 'right':
            join_right(reader_1, reader_2, column_name)
        else:
            print('Invalid join type')



def join_inner(reader_1, reader_2, column_name):
    for row_1 in reader_1:
        for row_2 in reader_2:
            if row_1[column_name] == row_2[column_name]:
                print(row_1, row_2)


def join_left(reader_1, reader_2, column_name):
    for row_1 in reader_1:
        for row_2 in reader_2:
            if row_1[column_name] == row_2[column_name]:
                print(row_1, row_2)
                break


def join_right(reader_1, reader_2, column_name):
    for row_1 in reader_1:
        for row_2 in reader_2:
            if row_1[column_name] == row_2[column_name]:
                print(row_1, row_2)
                break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path_1', help='path to the first file')
    parser.add_argument('file_path_2', help='path to the second file')
    parser.add_argument('column_name', help='column name to join')
    parser.add_argument('join_type', help='join type')
    args = parser.parse_args()
    join_csv(args.file_path_1, args.file_path_2, args.column_name, args.join_type)


if __name__ == '__main__':
    main()