def Left_rotation(arr,d):
    d=d%len(arr)
    return arr[-d:]+arr[:-d]
arr=[1,2,3,4,5]
d=2
result=Left_rotation(arr,d)
print(result)
