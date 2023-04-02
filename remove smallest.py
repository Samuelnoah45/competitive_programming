test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int ,input().split()))
    arr.sort()
    r = 1
    l = 0
    ans = "YES"
    while r < n:
        if arr[r] - arr[l] > 1:
            ans = "NO"
            break
        r += 1
        l += 1
        
    print(ans)