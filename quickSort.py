import random


def partition(array, left, right):
    pivot = left
    lessIndex = left - 1
    for curIndex in range(left, right + 1):
        if array[curIndex] <= array[pivot]:
            lessIndex = lessIndex + 1
            array[lessIndex], array[curIndex] = array[curIndex], array[lessIndex]
    array[lessIndex], array[pivot] = array[pivot], array[lessIndex]
    # print(array)
    return lessIndex


def partitionNew(array, left, right):
    pivot = left
    lessIndex = left - 1
    greater = right + 1
    curIndex = left
    while curIndex < greater:
        if array[curIndex] < array[pivot]:
            lessIndex = lessIndex + 1
            array[curIndex], array[lessIndex] = array[lessIndex], array[curIndex]
            curIndex = curIndex + 1
        elif array[curIndex] == array[pivot]:
            curIndex = curIndex + 1
        else:   
            greater = greater - 1
            array[curIndex], array[greater] = array[greater], array[curIndex]
    return lessIndex, greater


def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        mid = array[0]
        less = [i for i in array[1:] if i <= mid]
        greater = [j for j in array[1:] if j > mid]
    return quickSort(less) + [mid] + quickSort(greater)


def quickSortNew(array):
    if len(array) <= 1:
        return
    else:
        quickMergeNew(array, 0, len(array) - 1)


def quickMerge(array, left, right):
    if left >= right:
        return
    temp = random.randint(left, right)
    array[left], array[temp] = array[temp], array[left]
    index = partition(array, left, right)
    quickMerge(array, left, index - 1)
    quickMerge(array, index + 1, right)


def quickMergeNew(array, left, right):
    if left >= right:
        return
    temp = random.randint(left, right)
    array[left], array[temp] = array[temp], array[left]
    lessIndex, greaterIndex = partitionNew(array, left, right)
    quickMerge(array, left, lessIndex)
    quickMerge(array, greaterIndex, right)


array = [0, 5, 2, 7, 2, 3, 3, 4, 6]
quickSortNew(array)
print(array)