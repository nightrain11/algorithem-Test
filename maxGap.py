
'''
    求一组数的最大差值，借助的是桶排序思想，将数据均匀分布在len+1数组内，则最大的差值一定不会来自同一个桶。
    借助这个来进行求解。
    关键：如何将数据均匀分布在len+1个桶。
    将数据归一化到任意区间[a, b]的方法
    1.计算系数k=（b-a)/(Max-Min)
    2.得到归一化到[a,b]区间的数据：Y=a+k(X-Min)

    本题需要将数据归一化到[0, arrlen]区间中。
'''


def maxGap(array):
    if array is None or len(array) < 2:
        return 0
    
    # max = float("-inf")
    # min = float("inf")
    # for i in range(len(array)):
    #     min = min(min, array[i])
    #     max = max(max, array[i])
    maxValue = max(array)
    minValue = min(array)
    if minValue == maxValue:
        return 0
    arrayLen = len(array) + 1
    hasNum = [False] * arrayLen
    maxArray = [None] * arrayLen
    minArray = [None] * arrayLen
    bid = 0
    for i in range(len(array)):
        bid = bucket(array[i], len(array), minValue, maxValue)
        minArray[i] = hasNum[i] and min(array[i], minArray[bid]) or array[i]
        maxArray[i] = hasNum[i] and max(array[i], maxArray[bid]) or array[i]
        hasNum[i] = True
    res = 0
    lastMax = maxArray[0]
    for i in range(1, arrayLen):
        if hasNum[i]:
            res = max(res, minArray[i] - lastMax)
            lastMax = maxArray[i]
    return res


def bucket(num, len, mins, maxs):
    return (num - mins) * len // (maxs - mins)


array = [3, 1, 6, 2, 7]
print(maxGap(array))