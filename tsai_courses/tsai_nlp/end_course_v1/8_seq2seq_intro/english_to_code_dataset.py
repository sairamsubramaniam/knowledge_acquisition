# write a python program to multiply three numbers 
num1 = 1.5
num2 = 6.3
num3 = -2.3
product = num1 * num2 * num3
print(f'Product: {product}')


# write a python function that when given two numbers, would divide the first number by second number and return the quotient and remainder
def divide_first_number_by_second(num1, num2):
    return (num1 // num2), (num1 % num2)


# write a python function to return the largest and smallest numbers in the given list and return None if the list is empty
def largest_and_smallest(list_of_nums):
    if list_of_nums:
        return max(list_of_nums), min(list_of_nums)
    else:
        return


# write a recursive python function to print the nth fibonacci number, where n is provided as the argument
def fibonacci_recursive(n):
   if n <= 1:
       return n
   else:
       return (recur_fibo(n-1) + recur_fibo(n-2))


# write a python function that would read the given input file path and print its contents
def read_and_print_file(filepath):
    with open(filepath, "r") as infile:
        print( infile.read() )


# write a python program that would print the first n positive integers using a for loop
n = 62
for num in range(n):
    print(num)


# write a python function that returns the input list sorted in ascending order
def sort_ascending(list_to_be_sorted):
    return sorted(list_to_be_sorted)


# write a python function that returns the input list sorted in descending order
def sort_descending(list_to_be_sorted):
    return sorted(list_to_be_sorted, reverse=True)


# write a python function that would return the sum of first n natural numbers, where n is the input
def sum_first_n(n):
    return ( n * (n+1) ) // 2


# write a recursive python function that would return the sum of first n natural numbers, where n is the input
def sum_first_n_recursive(n):
    if n == 0:
        return 0
    return sum_first_n_recursive(n-1) + n


# write a python function that would filter a list of dictionaries where a specified key equals given value, list_of_dictionaries, key and value are inputs to this function.
def filter_with_key_value(list_of_dicts, key, value):
    return list( filter( lambda x: x.get(key) == value, list_of_dicts ) )


# write a recursive python function that takes either a list or tuple as input and reverses the order of its elements
def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()
    if seq == emptySeq:
        return emptySeq
    restrev = reverse(seq[1:])
    first = seq[0:1]
    result = restrev + first
    return result    


# write a python function that returns the square of a given input number
def square(x):
    return x**2


# write a python function that performs selection sort on the given list or tuple or string and returns the new sorted sequence
def selection_sort(list_to_be_sorted):
    sorted_list = list_to_be_sorted[:]
    for i in range(len(sorted_list)):
        new_min = sorted_list[i]
        new_min_old_place = i
        for j in range(i+1, len(sorted_list)):
            if new_min > sorted_list[j]:
                new_min = sorted_list[j]
                new_min_old_place = j
        old_val = sorted_list[i]
        sorted_list[i] = new_min
        sorted_list[new_min_old_place] = old_val
    return sorted_list


# write a python program that asks for user input and prints the given input
a = input("User Input")
print(a)


# write a python function shifts and scales all numbers in the given list by the given mean and standard deviation
def shift_and_scale(list_of_nums, mean, std):
    return [ (x-mean) / std for x in list_of_nums ]


# write a python function that takes in a list of sequences and zips each corresponding element from the list into a tuple and returns the list of such tuples
def zip_(list_of_seq):
    return list(zip(*list_of_seq))


# write a python program that asks user to guess a number between 1 and 5 and guess it within 3 guesses
print("Please guess a number between 1 and 5 and I will guess within 3 chances!")
guess1 = input("Is it <= 3? enter y/n \n")
if guess1 == "y":
    guess2 = input("Is it <= 2? enter y/n \n")
    if guess2 == "y":
        guess3 = input("Is it 1? enter y/n \n")
        if guess3 == "y":
            print("Yay! found the number, its 1")
        else:
            print("Yay! found the number, its 2")
    else:
        print("Yay! found the number, its 3")
else:
    guess2 = input("Is it 4? enter y/n \n")
    if guess2 == "y":
        print("Yay! found the number, its 4")
    else:
        print("Yay! found the number, its 5")


# write python program that would merge two dictionaries by adding the second one into the first
a = {"a": 1, "b": 3}
b = {"c": 1, "d": 3}
a.update(b)


# write a python function that would reverse the given string
def reverse_string(str_to_be_reversed):
    return str_to_be_reversed[::-1]


# write a python program that would print "Hello World"
print("Hello World")


# write a python program that would swap variable values
a = 10
b = 15
a, b = b, a


# write a python program that iterates over a dictionary and prints its keys and values
a = {"a":1, "b":2, "c":3, "d":4}
for k, v in a.items():
    print(k, v)


# write a python function that would print the ASCII value of a given character
def print_ascii(char):
    print(ord(char))


# write a python function that takes in two numbers and returns their HCF
def hcf(num1, num2):
    smaller = num1 if num1 < num2 else num2
    for i in range(1, smaller+1):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i
    return hcf


# write a python function that takes in two numbers and returns their LCM
def lcm(num1, num2):
    bigger = num1 if num1 > num2 else num2
    while True:
        if (bigger % num1 == 0) and (bigger % num2 == 0):
            break
        bigger += 1
    return bigger


# write a recursive python function to calculate sum of natural numbers upto n, where n is an argument
def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)


# write a python function that deletes the last element of a list and returns the list and the deleted element
def delete_last_element(list_to_be_processed):
    deleted_element = list_to_be_processed.pop()
    return list_to_be_processed, deleted_element


# write a python function that takes in a list and returns a list containing the squares of the elements of the input list
def square_list_elements(list_to_be_squared):
    return list( map(lambda x: x**2, list_to_be_squared) )


# write a python function that finds square roots of a given number, if the square root is an integer, else returns the message "Error - the square root is not an integer"
def find_integer_square_roots(num):
    found = False
    for k in range(1, (num//2)+1):
        if ((k**2)==num):
            found = True
            break
    if not found:
        return "Error - the square root is not an integer"
    return -k, k


# write a python program that prints out natural numbers less than or equal to the given number using a while loop
input_num = 27
while input_num:
    print(input_num)
    input_num -= 1


# write a python function that takes two numbers. The function divides the first number by the second and returns the answer. The function returns None, if the second number is 0
def divide(num1, num2):
    if num2 == 0:
        return
    else:
        return num1 / num2


# write a python program uses else with for loop
seq = "abcde"
for k in seq:
    if k == "f":
        break
else:
    print("f Not Found!")


# write a recursive python function that performs merge sort on the given list or tuple or string and returns the new sorted sequence
def sort_and_merge(l1, l2):
    new_list = []
    i = 0
    j = 0
    l1_len = len(l1)
    l2_len = len(l2)    
    while (i <= l1_len-1) and (j <= l2_len-1):
        if l1[i] < l2[j]:
            new_list.append(l1[i])
            i +=1
        else:
            new_list.append(l2[j])
            j +=1
    if i <= (l1_len-1):
        new_list += l1[i:]
    if j <= (l2_len-1):
        new_list += l2[j:]
    return new_list

def recursive_merge_sort(list_to_be_sorted):
    final_list = []
    first = 0
    last = len(list_to_be_sorted)
    if last <= 1:
        final_list.extend( list_to_be_sorted )
    else:
        mid = last // 2
        l1 = recursive_merge_sort( list_to_be_sorted[:mid] )
        l2 = recursive_merge_sort( list_to_be_sorted[mid:] )
        final_list.extend( sort_and_merge( l1, l2 ) )
    return final_list


# write a python program results in a too many values to unpack error
a, b = (1, 2, 3)





