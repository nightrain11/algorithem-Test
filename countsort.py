
'''
    有20个随机数，取值范围是0到10，用最快的速度来进行排序
    1.根据待排序集合中最大元素和最小元素的差值范围，申请额外空间的大小Max-Min+1
    2.遍历待排序集合，记录没一个数出现的次数
    3.对额外空间内统计的次数进行计算，得到每一个元素的正确位置
    4.对待排序集合后向前遍历，借助额外内存将数据移动到正确的位置。
    3，4两步目的是保持原来数据的稳定性。
    使用offset的目的是为了解决当数据并非从0开始，导致浪费空间，如数据范围9000-10000，如果是从0开始，则需要10000个空间，
    而从9000开始，只需要1001个空间。
    缺点：
    1.当数列最大最小值差距过大时，并不适用计数排序。
    2.当数列元素不是整数，并不适用计数排序。
'''


def countsort(array):
    maxValue = max(array)
    minValue = min(array)
    tempArray = [0 for i in range(maxValue - minValue + 1)]
    tempArray2 = [0 for i in range(len(array))]
    for i in range(len(array)):
        offset = array[i] - minValue
        tempArray[offset] = tempArray[offset] + 1
    
    for i in range(1, len(tempArray)):
        tempArray[i] = tempArray[i - 1] + tempArray[i]

    for i in range(len(array) - 1, -1, -1):
        offset = array[i] - minValue
        tempArray2[tempArray[offset] - 1] = array[i]
        tempArray[offset] = tempArray[offset] - 1


array = [5, 3, 2, 9, 8, 7]
countsort(array)

