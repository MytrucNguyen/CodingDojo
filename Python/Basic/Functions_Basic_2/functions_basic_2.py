# Countdown 
def count_down(start_num, end, step):
    count_down_array = []
    for num in range(start_num, end-1, step):
        count_down_array.append(num)

    print(count_down_array)

count_down(5, 0, -1)


# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))


# First Plus Length
def first_plus_length(array):
    sum = 0
    length = len(array)
    sum = array[0] + length

    return sum
print(first_plus_length([1,2,3,4,5]))


# Values Greater than Second
def values_greater_than_second(array):
    if (len(array) < 2):
        return False
    
    new_array = []
    for num in array:
        if(num > array[1]):
            new_array.append(num)

    return new_array

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# This Length, That Value
def length_and_value(num1, num2):
    return ([num2] * num1)
    
print(length_and_value(4, 7))
print(length_and_value(6, 2))

def length_and_value2(size, value):
    newList = []
    for num in range(size):
        newList.append(value)
    return newList


print(length_and_value2(4, 7))