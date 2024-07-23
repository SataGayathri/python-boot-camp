# find the elements that is present in K+N index
 # k is given by the user k+1

list=list(map(int,input().split()))
k=int(input())
n=int(input())
c=k+n
if(c>len(list)):
    print("error")
else:
    for i in range(0,len(list)):
      a=(list[c])
    print(a)
