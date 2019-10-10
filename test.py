def get_smallSum(arr):
    #主函数
    if not arr or len(arr)<2:
        return 0
    return smallSum(arr,0,len(arr)-1)
 
def smallSum(arr,l,r):
    # 求范围上的小和，在原数组上进行操作，不用切片
    if l==r:
        return 0
    #负责递归的终止条件，并且是最后一层子函数的返回值
    mid = (l+r)>>1
    #注意 （l+r)//2 比 len/2 少1
    left_sum = smallSum(arr,l,mid)
    right_sum = smallSum(arr,mid+1,r)
    all_sum = merge_sum(arr,l,mid,r)
    #没一个子函数都包括三部分
    #头两个负责给第三个产生下标没并且接受三个相加的值
    #后一个负责在merge的过程中利用外排计算小河，
    # 并且在原数组进行操作，姚旭中间的参数才能找到第二个数组的第一个
    return left_sum+right_sum+all_sum
    #作为出最后一层外所有子函数层的返回值
 
def merge_sum(arr,l,mid,r):
    #负责在和的过程中进行榨取小和
    left = l
    right = mid+1
    res = []
    sum = 0
    while left<=mid and right<=r:
        if arr[left]<=arr[right]:
            res.append(arr[left])
            sum+=arr[left]*(r-right+1)
            left+=1
        else:
            res.append(arr[right])
            right+=1
    #把余下的复制过来，并且改变一下原有数组
    res+=arr[left:mid+1]
    res+=arr[right:r+1]
    for i in range(l,r+1):
        arr[i] = res.pop(0)
    #
    return sum
 
if __name__ == '__main__':
    li = [1,3,4,2,5]
    print(get_smallSum(li))
