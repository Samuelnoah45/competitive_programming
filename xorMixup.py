test = int(input())
 
for i in range(test):
    n = int(input())
    nums = list(map(int , input().split()))
    count = 0
    for idx , num in enumerate(nums):
        r = 0
        ans = 0
        new = nums[:idx] + nums[idx+1:] 
        r = 0
        while r < len(new):
            ans ^=new[r]
            r += 1
        if ans == num:
            print(ans)
            break