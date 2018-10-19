import random
import csv


def read_file(file_name):
    with open(file_name, 'rt') as data_file:
        rows = csv.reader(data_file)
        table = list(rows)
        for row in rows:
            print(row)
        return table


def convert_data(data_table):
    for row in data_table:
        for i in range(len(row)):
            row[i] = float(row[i])


if __name__ == "__main__":
    data = read_file("data.csv")
    convert_data(data)

print("hello world!")
