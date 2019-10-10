def mergeSort(array):
    if len(array) <= 1:
        return array or []
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    indexL = 0
    indexR = 0
    tempArray = []
    while indexL < mid and indexR < len(right):
        if left[indexL] >= right[indexR]:
            tempArray.append(right[indexR])
            indexR = indexR + 1
        else:
            tempArray.append(left[indexL])
            indexL = indexL + 1
    if len(left) - 1 >= indexL:
        tempArray.extend(left[indexL:])
    elif len(right) - 1 >= indexR:
        tempArray.extend(right[indexR:])
    return tempArray


array = [89, -34, -77, 6, 3, 20, -28]

print(mergeSort(array))