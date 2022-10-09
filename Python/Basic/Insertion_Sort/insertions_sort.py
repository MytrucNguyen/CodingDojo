# Insertion Sort
# Time Complexity: O(N2) 
# Auxiliary Space: O(1)
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/


array = [12, 11, 13, 5, 6]

def insertion_sort(arr):
    length = len(arr)

    for i in range(1, length):
        key = arr[i]

        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

insertion_sort(array)
print(array)