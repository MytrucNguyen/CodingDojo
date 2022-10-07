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
