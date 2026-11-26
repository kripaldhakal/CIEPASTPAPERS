def BinarySearch(array, num):

    lowerbound = 0
    upperbound = len(array) - 1

    while lowerbound <= upperbound:
        midIndex = (lowerbound + upperbound) // 2
        midValue = array[midIndex]

        if num == midValue:
            return True
            break
        elif midValue < num:
            lowerbound = midIndex + 1
        else:
            upperbound = midIndex - 1

    return False

array = [1, 3, 5, 7, 8]  #Test Value
out = BinarySearch(array, 2)
print(out)