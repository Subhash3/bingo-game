#!/usr/bin/python3

import random
import time

def print_table(table) :
    i = 0
    for num in table :
        print(num, end=' ')
        i += 1
        if i % 5 == 0 :
            print()

def strike_out(num, table) :
    i = 0
    for x in table :
        if x == num :
            table[i] = 0
            break
        i += 1

def row_check(table) :
    i = 0
    lines = 1
    count = 0
    line_count = 0
    while i < 25 :
        #print("i: ", i)
        if table[i] == 0 :
            count += 1
        else :
            i = 4 * lines
            lines += 1
            count = 0
        if count == 5 :
            lines += 1
            line_count += 1
            count = 0
        i += 1
    return line_count


def column_check(table) :
    column = 1
    i = 0
    count = 0
    column_count = 0
    while i < 25 :
        #print(i)
        if table[i] == 0 :
            count += 1
            i += 4
        else :
            i = column
            count = 0
            column += 1
        if count == 5 :
            column_count += 1
            count = 0
            i = column - 1
            column += 1
        i += 1
    return column_count

def diagonal_check(table) :
    diag1 = [0, 6, 12, 18, 24]
    diag2 = [4, 8, 12, 16, 20]
    diag_count = 0
    count = 0

    for x in diag1 :
        if table[x] == 0 :
            count += 1
        else :
            break
    if count == 5 :
        diag_count += 1
        count = 0
    for y in diag2 :
        if table[y] == 0 :
            count += 1
        else :
            break
    if count == 5 :
        diag_count += 1
        count = 0
    return diag_count


table = list()
i = 0
while i < 25 :
    num = (int(random.random()*100) % 26)
    if num not in table and 0 < num <= 25:
        table.append(num)
        #print(num)
        i += 1
#print_table(table)

lines = 0
striked_out_table = list()
while True :
    strike = input("Enter a number: ")
    if strike == "done" :
        print("Congratulations!!")
        break
    strike = int(strike)
    striked_out_table.append(strike)
    if not 0 < strike <= 25 :
        print("Please enter a number between 1 and 25")
        continue
    elif strike not in table :
        print("That number already been striked out")
        continue
    strike_out(strike, table)
    #print_table(table)
    lines = row_check(table)
    lines += column_check(table)
    lines += diagonal_check(table)
    #print("striked lines: ", lines)
    if lines >= 5 :
        print("I WON :D")
        print_table(table)
        quit()

    while True :
        num = (int(random.random()*100) % 25) + 1
        if num not in striked_out_table and num in table :
            time.sleep(1)
            print("\nMy number: ", num)
            strike = num
            strike_out(strike, table)
            #print_table(table)
            lines = row_check(table)
            lines += column_check(table)
            lines += diagonal_check(table)
            #print("striked lines: ", lines)
            break
    if lines >= 5 :
        print("I WON :D")
        print_table(table)
        quit()

