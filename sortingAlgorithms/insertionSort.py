def insertionSorting(array):
    for i in range(1, len(array)):
        currentIndex = array[i]
        j = i - 1
        while j>= 0 and array[j] > currentIndex:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = currentIndex
    print(' '.join(str(x) for x in array))
        

array = [3, 11, 56, 78, 32, 12, 13]
insertionSorting(array)        

