# 1. the last num less than target. return -1 if it doesn't exist
# 2. the first num greater than target. return n if it doesn't exist
# 3. the first index of num equal to target. return None if it doesn't exist
# 4. the first num greater than or equal to target. return n if it doesn't exist
def linear_search(arr,target,left=None,right=None):
    if left is None:
        left=0
    if right is None:
        right=len(arr)-1
    for i,e in enumerate(arr[left:right+1]):
        if e>=target:
            return i
    return len(arr)
def binary_search(arr,target,left=None,right=None,end_th=None):
    if left is None:
        left=0
    if right is None:
        right=len(arr)-1
    
    if end_th is None:
        def break_func(left,right):
            return left<=right
    else:
        def break_func(left,right):
            return right-left>end_th
    while break_func(left,right):
        mid=(left+right)//2
        if arr[mid]>=target:
            right=mid-1
        else:
            left=mid+1
    return left if end_th is None else linear_search(arr,target,left,right)
# 5. the last index of num equal to target. return None if it doesn't exist
# 6. the last num less than or equal to target. return -1 if it doesn't exist 