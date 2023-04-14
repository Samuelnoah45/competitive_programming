test = int(input())


for _ in range(test):
    n = int(input())
    nums = list(map(int ,input().split()))
    sigh = ""
    maxVal = float("-inf")
    i = 0
    ans = 0
    while i < n :
        while  i < n and sigh != "+" and nums[i] < 0:
            maxVal = max(maxVal , nums[i])
            i += 1
            
        if maxVal != float("-inf") and sigh != "+":
            sigh = "+"
            ans += maxVal 
            maxVal = float("-inf") 
        
        while  i < n and sigh != "-" and nums[i] >= 0:
            maxVal = max(maxVal , nums[i])
            i += 1

        if maxVal != float("-inf") and sigh != "-":
            sigh = "-"
            ans += maxVal 
            maxVal = float("-inf") 
    print(ans)

        

        



