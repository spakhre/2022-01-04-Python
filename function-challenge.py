print('#2 Write a Python function to sum all the numbers in a list.')

def sum_number(n):
    sum = 0
    for n1 in n:
        sum += n1
    return sum
print(sum_number((1,2,3,5,6)))

print('\n#5 Write a Python function to check whether a number is in a given range')

def test_number(a):
    if a in range(-10, 20):
        print(f"{a} is within range of -10 and 20")

    else:
        print(f"{a} is out of range")

test_number(100)
test_number(-5)

#################################################################################
print('\n#7 Write a Python function that takes a list and returns a new list with unique elements of the first list')

def unique_list(numbers):
    list1 = []

    for number in numbers:
        if number not in list1:
            list1.append(number)
    return list1

print(unique_list([1,1,3,4,5,5,9,0,0]))
print(unique_list([-1,-1,3,4,-5,5,9,0,0]))

#########################################################################
print('\n#9 Write a Python program to print the even numbers from a given list')

def even_num(list2):
    list3 = []
    for number in list2:
        if number %2 == 0:
            list3.append(number)
    return list3

print(even_num([0,1,2,3,4,66,55,87]))




