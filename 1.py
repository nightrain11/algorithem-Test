import random


def generalRandomArray(maxsize: int, maxValue: int):
    list = [random.randint(0, maxValue) - random.randint(0, maxValue)
            for i in range(random.randint(1, maxsize))]
    # print(list)
    return list


def comparator(array):
    array.sort()


def insertSort(array):
    for i in range(len(array)):
        if i > 0 and array[i - 1] > array[i]:
            for k in range(i - 1, -1, -1):
                if array[k + 1] < array[k]:
                    array[k + 1], array[k] = array[k], array[k + 1]


def compare(array1, array2):
    isSame = True
    if array1 is None and array2 is not None or array2 is None and array1 is not None:
        isSame = False
    if len(array1) != len(array2):
        isSame = False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            isSame = False
    return isSame


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


def main():
    testTimes = 50000
    maxSize = 10
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        randList = generalRandomArray(maxSize, maxValue)
        copyList = randList.copy()
        randList = mergeSort(randList)
        insertSort(copyList)
        succeed = compare(randList, copyList)
        if not succeed:
            print(randList)
            print(copyList)
            break
    if not succeed:
        print("not same")

main()