num = int(input())
count = 0
while num != 0:
    if num & 1 == 1:
        count += 1
    num>>=1
print(count)