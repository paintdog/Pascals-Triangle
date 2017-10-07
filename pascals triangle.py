#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_pascals_triangle(n):    
    table = []
    for i in range(n):
        if i == 0:
            table.append([1])
        elif i == 1:
            table.append([1, 1])
        else:
            line = []
            for i, item in enumerate(table[-1][:-1]):
                line.append(table[-1][i] + table[-1][i + 1])
            table.append([1] + line + [1])
    return table


def output_triangle(triangle):
    for line in triangle:
        width = len(" ".join(map(str, triangle[-1])))
        print(" ".join(map(str, line)).center(width, " "))
    

if __name__ == "__main__":
    n = 5
    triangle = get_pascals_triangle(n)
    output_triangle(triangle)
