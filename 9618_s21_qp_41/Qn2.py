
def linearSearch(num):
    for i in range(len(arrayData)):
        if num == arrayData[i]:
            return True
    return False

def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-1):
            if array[j] < array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

ask = int(input("Enter a number: "))
if linearSearch(ask) == True:
    print("The number is present in the array")
else:
    print("The number is not present in the array")

bubblesort(arrayData)