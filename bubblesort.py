def bubblesort(array):

    n = len(array)

    for i in range(n):

        for j in range(n-1):

            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array

print(bubblesort([12, 33, 1, 23, 55, 43]))