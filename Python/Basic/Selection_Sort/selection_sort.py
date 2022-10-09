# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index

arr = [51, 2, 1, 9, 7, 6, 21, -5]


def selectionSort(array):

    size = len(array)

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):

            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

         # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])


selectionSort(arr)
print(f'The array after sorting in Ascending Order by selection sort is: {arr}')
