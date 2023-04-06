
from collections import defaultdict
vertex = int(input())
Hash = defaultdict(list)
matrix = []
for _ in range(vertex):
  row = list(map(int ,input().split()))
  matrix.append(row)

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if Hash[i+1]:
        Hash[i+1][0] +=matrix[i][j]
    else:
       Hash[i+1]=[matrix[i][j],0]
    if Hash[j+1]:
        Hash[j+1][1] +=matrix[i][j]
    else:
       Hash[j+1]=[0 ,matrix[i][j]]
source = [0]
sink = [0]
for key in Hash:
    if Hash[key][0] == 0:
      sink[0] += 1
      sink.append(key)
    if Hash[key][1] == 0:
       source[0] += 1
       source.append(key)
source = source[:1] + sorted(source[1:])
sink = sink[:1] + sorted(sink[1:])
print(*source)
print(*sink)

    
        


    


