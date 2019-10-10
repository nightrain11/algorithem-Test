def reverseCount(array):
    if array is None or len(array) <= 1:
        return 0
    return mergeReverse(array, 0, len(array) - 1)


def mergeReverse(array, left, right):
    if left == right:
        return
    mid = left + (right - left) // 2
    mergeReverse(array, left, mid)
    mergeReverse(array, mid + 1, right)
    merge(array, left, mid, right)


def merge(array, left, mid, right):
    p1 = left
    p2 = mid + 1
    temp = []
    while p1 <= mid and p2 <= right:
        if array[p2] < array[p1]:
            for i in range(p1, mid + 1):
                print(array[i], array[p2])
            temp.append(array[p2])
            p2 += 1
        else:
            temp.append(array[p1])
            p1 += 1
    if p1 <= mid:
        temp.extend(array[p1:mid + 1])
    if p2 <= right:
        temp.extend(array[p2:right + 1])
    array[left:right + 1] = temp


array = [6,3,9,1,4,5]
reverseCount(array)