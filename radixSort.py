'''
基数排序
    原理：先排元素的最后一位，再排倒数第二位，直到所有位数都排完。这里并不能先排第一位，那样最后依然是无序。
    基于桶排序，时间复杂度O(N+M)其中，N为待排序的个数，M为数据的长度
    数据的位数可以不同，只需要尾部对齐，高位补0就行。
    步骤：1.找到最大数值，求出位数M
    2.根据数据的进制来确定桶的个数，10进制需要10个桶。
    3.对数据每一位进行排序，从后向前进行排序，相同的位放在同一个桶里。
缺点：1.基数排序只针对正整数，负数以及小树都不行，必须进行转化。
      2.需要额外的内存
'''


def radixSort(array):
    maxVale = max(array)
    maxLenth = len(str(maxVale))
    begin = 0
    while begin < maxLenth:
        bucket = [[] for i in range(10)]
        for value in array:
            bucket[int(value / 10 ** begin % 10)].append(value)

        array.clear()

        for bucketItem in bucket:
            for item in bucketItem:
                array.append(item)
        begin += 1


if __name__ == '__main__':
    a = [17615019049, 17093, 4937309, 17615109049]
    radixSort(a)
    print(a)