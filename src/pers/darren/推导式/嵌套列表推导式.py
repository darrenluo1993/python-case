#!/usr/bin/env python3

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(len(matrix))

list1 = [row for row in matrix]
print(list1)

list2 = [[row[i] for row in matrix] for i in range(4)]
print(list2)
