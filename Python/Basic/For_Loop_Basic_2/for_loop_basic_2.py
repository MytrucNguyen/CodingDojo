# Biggie Size
def biggie_size(array_list_given): 
    new_array = []
    for num in array_list_given:
        if num > 0:
            new_array.append("big")
        else:
            new_array.append(num)
    return new_array
print(biggie_size([-1, 3, 5, -5]))

# Count Positives
def count_positives(array_given):
    positive_sum = 0
    for num in array_given:
        if num > 0:
            positive_sum += 1
    array_given[-1] = positive_sum
    return array_given

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total
def sum_total(given_array):
    total_sum = 0
    for num in given_array:
        total_sum += num
    return total_sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Average 
def average(array_given):
    total_sum = 0
    length_of_array = len(array_given)

    for num in array_given:
        total_sum += num
    return total_sum/length_of_array

print(average([1,2,3,4]))

# Length 
def length(array_given):
    length_total = 0

    if len(array_given) > 0:
        for num in array_given:
            length_total += 1      
    
    return length_total

print(length([37,2,1,-9]))
print(length([]))

# Minimum 
def minimum(array_given):
    if(len(array_given) == 0):
        return False
        
    array_given.sort()
    return array_given[0]
        

print(minimum([37,2,1,-9]))
print(minimum([]))

# Maximum  
def maximum(array_given):
    if(len(array_given) == 0):
        return False

    array_given.sort()
    return array_given[-1]
        

print(maximum([37,2,1,-9]))
print(maximum([]))

# Ultimate Analysis
def ultimate_analysis(array_given):
    sum = 0

    analysis = {
        'sum_total': 0,
        'average': 0,
        'minimum': 0,
        'maximum': 0,
        'length': 0
    }

    array_given.sort()

    for num in array_given:
        sum += num
    

    analysis['sum_total'] = sum
    analysis['average'] = sum/len(array_given)
    analysis['minimum'] = array_given[0]
    analysis['length'] = len(array_given)
    analysis['maximum'] = array_given[-1]

    return analysis

print(ultimate_analysis([37,2,1,-9]))

# Reverse List
def reverse_list(given_array):
    return given_array[::-1]

print(reverse_list([37,2,1,-9]))