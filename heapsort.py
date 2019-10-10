import random


def maxHeapify(array, i, heapSize):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heapSize and array[left] > array[largest]:
        largest = left
    if right < heapSize and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        maxHeapify(array, largest, heapSize)


def maxHeapifyNew(array, i, heapSize):
    left = 2 * i + 1
    while(left <= heapSize):
        largest = i
        if left + 1 < heapSize and array[left + 1] > array[largest]:
            largest = left + 1
        if left < heapSize and array[left] > array[largest]:
            largest = left
        if largest == i:
            break
        i = largest
        left = 2 * i + 1


def buildMaxHeap(array):
    for i in range(len(array) // 2, -1, -1):
        maxHeapify(array, i, len(array))
    # print(array)


def buildMaxHeapNew(array):
    for i in range(1, len(array)):
        p = (i - 1) // 2
        while array[i] > array[p]:
            array[p], array[i] = array[i], array[p]
            i = p
            p = (i - 1) // 2


def heapSort(array):
    buildMaxHeapNew(array)
    heapSize = len(array)
    for i in range(len(array) - 1, 0, -1):
        # print(i)
        array[0], array[i] = array[i], array[0]
        heapSize = heapSize - 1
        maxHeapify(array, 0, heapSize)


def generalRandomArray(maxsize: int, maxValue: int):
    list = [random.randint(0, maxValue) - random.randint(0, maxValue)
            for i in range(random.randint(1, maxsize))]
    # print(list)
    return list


def comparator(array):
    array.sort()


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


def main():
    testTimes = 500000
    maxSize = 10
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        randList = generalRandomArray(maxSize, maxValue)
        copyList = randList.copy()
        heapSort(randList)
        comparator(copyList)
        succeed = compare(randList, copyList)
        if not succeed:
            print(randList)
            print(copyList)
            break
    if not succeed:
        print("not same")
# array = [16, 14, 3, 8, 6, 7]
# heapSort(array)
# print(array)