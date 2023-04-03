test = int(input())

for _ in range(test):
    x = int(input())
    y = x&(-x)
    if x==y:
        y += 1 
    if x&y == 0:
        y+= 1
        
    print(y)