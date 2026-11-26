def InsersionSort(array):

    for i in range(1, len(array)):

        DataToInsert = array[i]
        Inserted = False
        Next = i - 1

        while Next >= 0 and not Inserted:

            if DataToInsert < array[Next]:
                array[Next + 1] = array[Next]
                Next -= 1
                array[Next + 1] = DataToInsert
            else:
                Inserted = True

    return  array

array = [12, 44, 21, 55, 1, 34]  # Test Data
print(InsersionSort(array))