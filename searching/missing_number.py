def missingNumber(nums):
    n = len(nums)+1
    p = 2 * n
    flag = 0
    for i in range(len(nums)):
        if nums[i] % n == 0:
            flag = 1
        else:
            nums[(nums[i] % n) -1] += nums[(nums[i] % n) -1] * p
    if flag == 0:
        return 0
    else:
        for i in range(len(nums)):
            if nums[i] // n <= nums[i] % n:
                return i+1

nums = list(map(int,input().split()))
print(missingNumber(nums))