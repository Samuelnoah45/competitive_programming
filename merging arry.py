n , m = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

rg = max(n ,m)
ans = []
p1 = 0
p2 = 0
while p1 < n or p2 < m:

    if p1 < n and p2 < m:
        if arr1[p1] <= arr2[p2]:
            ans.append(arr1[p1])
            p1 += 1
        else:
            ans.append(arr2[p2])
            p2 += 1
    elif p1 < n:
            ans.append(arr1[p1])
            p1 +=1
    elif p2 < m:
            ans.append(arr2[p2])
            p2 += 1
print(*ans)

