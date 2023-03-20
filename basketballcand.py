cand , Def = list(map(int ,input().split()))
nums = list(map(int ,input().split()))
nums = sorted(nums)
l = 0 
r = len(nums) -1
count = 1 
ans = 0
 
while l <= r:
    if nums[r]*count > Def:
        # print(nums[r] ,count)
        ans += 1
        r -= 1
        count = 1
    else:
        l += 1
        count += 1
if len(nums) == 1 and nums[0] > Def:
    ans = 1    
print(ans)