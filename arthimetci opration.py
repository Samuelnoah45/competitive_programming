print("insert number of students")
N= int(input())
print("insert number of subject")
X=int(input())
for i in range(N):
    sums=0
    for j in range(X):
      print("Enter subject "+str(j+1))
      sub=float(input()) 
      sums+=sub; 
    print( (sums/X).round(2))

