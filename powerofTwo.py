from collections import deque
n , k = list(map(int ,input().split()))
n2 = n
Hash = {}
count = 0
while n != 0:
    if n&1 == 1:
        
        Hash[count] =Hash.get(count ,0) +1
    n >>=1
    count += 1
MIN = len(Hash)
MAX = 0
arr = deque()
for idx in Hash:
    arr.append(2**idx)



if k < MIN or k > n2:
    print("NO")
else:
    print("YES")
    while len(arr) < k:
       cur = arr.popleft()
       if cur % 2 == 0:
           arr.append(cur // 2)
           arr.append(cur // 2)
       else:
           arr.append(cur)
    
    print(*arr)
       
        
                
                


    
        
        
    
        
    
    






    