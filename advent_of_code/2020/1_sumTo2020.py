
"""
Problem Description:
find the two entries that sum to 2020 and then multiply those two numbers together.
Input: https://adventofcode.com/2020/day/1/input
"""

from itertools import combinations
import time
start = time.time()


# READ INPUTS:
input_filepath = "inputs/1_sumTo2020"

with open(input_filepath, "r") as inp:
    nums = inp.read().split("\n")[:-1]


# REMOVE NUMBERS THAT WOULD EXCEED 2020, IF ADDED TO MIN NUMBER
nums = [int(n) for n in nums]
maxnum = ( 2020 - min(nums) )
nums = [n for n in nums if n <= maxnum]


# DIVIDE NUMBERS AS THOSE LESS THAN HALF OF 2020 & THOSE ABOVE
midpoint = (2020 // 2)
exact_midpoint = ( (midpoint + midpoint) == 2020 )

first_half = [n for n in nums if n <= midpoint]
second_half = [n for n in nums if n > midpoint]


# SEARCH FOR THREE NUMBERS:
numb1, numb2, numb3 = 0, 0, 0
two_num_combins = combinations(first_half, 2)

for tn in two_num_combins:
    for s in second_half:
        if (sum(tn) + s) == 2020:
            print("The three numbers that add to 2020 and their poduct are:")
            print(tn[0], tn[1], s, tn[0]*tn[1]*s)
            break


# SEARCH FOR TWO NUMBERS:
def two_nums_add_to_2020(first_half, second_half, midpoint, exact_midpoint):
    num1, num2 = 0, 0
    one_midpoint_found = False

    for f in first_half:

        if (f == midpoint) and exact_midpoint:
            if one_midpoint_found:
                num2 = f
                print("The two numbers that add to 2020 and their poduct are:")
                print(num1, num2, num1*num2)
                break
            else:
                num1 = f
                one_midpoint_found = True
                continue

        for s in second_half:
            if ((f+s)==2020):
                num1, num2 = f, s
                print("The two numbers that add to 2020 and their poduct are:")
                print(num1, num2, num1*num2)
                break


two_nums_add_to_2020(first_half, second_half, midpoint, exact_midpoint)
