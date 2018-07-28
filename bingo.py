#!/usr/bin/python3

import random
import time

#Prints the bingo table
def print_table(table) :
    i = 0
    for num in table :
        # A two digit number occupies more space on the screen
        # Hence padding for them is only one space
        if num > 9 :
            print(num, end=' ')
        #And every single digit is padded by 2 spaces
        else :
            print(num, end='  ')
        i += 1
        # Printing a new line for every five numbers
        if i % 5 == 0 :
            print()

# Strikes out the number that has been used
# Striking out actually overwrites the number with 0
def strike_out(num, table) :
    i = 0
    for x in table :
        if x == num :
            table[i] = 0
            break
        i += 1

# Check how many rows are completed
def row_check(table) :
    i = 0
    lines = 1 #Current line number
    count = 0
    line_count = 0 # Completed lines' count

    # Loop over the table
    while i < 25 :
        #print("i: ", i)

        #Check if the first 5 numbers of any line are zeroes
        if table[i] == 0 :
            count += 1
        # If atleast one of them is not zero, them move to next line
        else :
            i = 4 * lines #Advance the index to the next line
            lines += 1 #Update current line number
            count = 0 # Reset the zeroes count

        # If 5 consecutive zeroes occur in any line,
        # that means that line is completed
        #Increase the line count
        if count == 5 :
            lines += 1
            line_count += 1
            count = 0
        i += 1
    return line_count

#Check how many columns are completed
def column_check(table) :
    column = 1 # Current column number
    i = 0
    count = 0 #Zeros' count
    column_count = 0 # Completed columns' count

    # Loop over the table
    while i < 25 :
        #print(i)

        # Check how many zeroes are there in each column
        if table[i] == 0 :
            count += 1
            i += 4 # Moving the index to next row same column

        #If atleast one of them is not zero, 
        #then move the index to the next column
        else :
            i = column #Advance to next column
            count = 0 # reset the zeroes' count
            column += 1 # Update the column to the next column

        #If the number of zeroes is 5,
        # that means that the column is completed
        if count == 5 :
            column_count += 1 #increase the column count by 1
            count = 0 # reset the zeroes count
            i = column - 1 # Set the index to column -1 
                           # Since count starts from 0
            column += 1 # Update the current column number
        i += 1
    return column_count

#Check if the diagonal got completed or not
def diagonal_check(table) :

    #Positions of diagonals in a 5x5 square
    #Ofcourse this doesn't hold generality
    diag1 = [0, 6, 12, 18, 24]
    diag2 = [4, 8, 12, 16, 20]

    #Number of diagonals got completed
    diag_count = 0
    count = 0 #Number of consecutive zeros

    #Check if all the elements of diagonals are zeroes
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


table = list() # Bingo table
i = 0
#Filling the table with number from 1 - 25
#in random positions
while i < 25 :
    #Generate a random number between 0 and 25 (inclusive)
    num = (int(random.random()*100) % 26)

    #If the number is not previously filled in table 
    #, then write it in the table
    if num not in table and 0 < num <= 25:
        table.append(num)
        #print(num)
        i += 1
#print_table(table)

lines = 0 #Number of lines striked out
striked_out_table = list() #Table to hold the striked out numbers

#File to store the numbers that system says
sys_file = open("system_nums.txt", "w") 
#File to store the numbers that user says
user_file = open("user_nums.txt", "w")

#Who starts the game? Computer or the user..
start = input("Do u want to start first(y/n): ")

#If the user rejected to start, then computer starts the game
#by generating a number
if start == "N" or start == "n" :
    guess = (int(random.random()*100) % 25) + 1
    print("my number: ", guess)
    #Write every number into the sys_file that system says 
    sys_file.write(str(guess) + ", ")
    #Add the number into the striked out numbers holder
    striked_out_table.append(guess)

while True :
    #Getting user's choice
    strike = input("Enter a number: ")

    #If the user enters 'done', 
    #means that he/she won the game
    #then simply quit the game
    if strike == "done" :
        print("Congratulations!!")
        print_table(table)
        break
    #Write every number into user_file that user says
    user_file.write(str(strike) + ", ")
    strike = int(strike)
    #Add that number to striked out numbers holder
    striked_out_table.append(strike)

    #If the number that user said is not in the range
    #then ask again to enter another number
    if not 0 < strike <= 25 :
        print("Please enter a number between 1 and 25")
        continue

    #If the number has already been striked out then
    #ask the user an other number
    elif strike not in table :
        print("That number already been striked out")
        continue

    #Call strike out function to strike out that number
    strike_out(strike, table)

    #print_table(table)

    #Call the below three functions to check how line are striked out
    lines = row_check(table)
    lines += column_check(table)
    lines += diagonal_check(table)
    #print("striked lines: ", lines)

    #If number of lines reached 5, then computer wins the game
    if lines >= 5 :
        print("I WON :D")
        print_table(table)

        #Add new line at the end of each file
        sys_file.write('\n')
        user_file.write('\n')
        quit()

    #Generate system choice
    while True :
        #Generate a number between 1 and 25(inclusive)
        num = (int(random.random()*100) % 25) + 1

        #the generated number will be taken into account only iff
        #The number isn't already striked out
        #The number is in the table
        if num not in striked_out_table and num in table :
            time.sleep(1) #Just for show..Pretend like thinking :D
            print("\nMy number: ", num)

            #write all the numbers into sys_file that system says
            sys_file.write(str(num) + ", ")
            strike = num

            #Call strike out function to strike that number out
            strike_out(strike, table)
            #print_table(table)

            #call the below three functions
            #To check the number of striked out lines
            lines = row_check(table)
            lines += column_check(table)
            lines += diagonal_check(table)
            #print("striked lines: ", lines)
            break

    #If the number of striked out lines reached 5
    #Means that the computer has won the game
    if lines >= 5 :
        print("I WON :D")
        print_table(table)
        
        #Add new line at the end of each file
        sys_file.write('\n')
        user_file.write('\n')
        quit()

