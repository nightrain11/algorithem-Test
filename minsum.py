# def minSum(array):
#     sum = 0
#     for i in range(1, len(array)):
#         for j in range(i, -1, -1):
#             if array[j] < array[i]:
#                 sum = sum + array[j]
#     return sum


# array = [1, 3]
# print(minSum(array))


# def minSum(array):
#     if len(array) <= 1 or array is None:
#         return 0
#     mid = len(array) // 2
#     return minSum(array[:mid]) + minSum(array[mid:]) + merge(array[:mid], array[mid:])


# def merge(left, right):
#     if left is None or right is None:
#         return 0
#     tempArray = []
#     indexL = 0
#     indexR = 0
#     sum = 0
#     while indexL < len(left) and indexR < len(right):
#         if left[indexL] < right[indexR]:
#             tempArray.append(left[indexL])
#             sum = sum + (len(right) - indexR - 1) * left[indexL]
#             indexL = indexL + 1
#         else:
#             tempArray.append(right[indexR])
#             indexR = indexR + 1
#     return sum

def smallSum(array):
    if array is None or len(array) <= 1:
        return 0
    return mergeSum(array, 0, len(array) - 1)


def mergeSum(array, left, right):
    if left == right:
        return 0
    mid = left + (right - left) // 2
    return mergeSum(array, left, mid) + mergeSum(array, mid + 1, right) + \
        merge(array, left, right, mid)


def merge(array, left, right, mid):
    if left == right:
        return 0
    tempArray = []
    p1 = left
    p2 = mid + 1
    sum = 0
    while p1 <= mid and p2 <= right:
        if array[p1] < array[p2]:
            sum = sum + (right - p2 + 1) * array[p1]
            tempArray.append(array[p1])
            p1 = p1 + 1
        else:
            tempArray.append(array[p2])
            p2 = p2 + 1
    if p1 <= mid:
        tempArray.extend(array[p1:mid+1])
    if p2 <= right:
        tempArray.extend(array[p2:right + 1])
    print(tempArray)
    array[left:right + 1] = tempArray
    print(array, sum)
    return sum


array = [6, 3, 9, 1, 4, 5]
print(smallSum(array))