#1.
#*****
#*****
#*****
#*****
#*****

'''for i in range(3):
    for j in range(3):
        print("*",end="")
    print()'''

'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()'''


for i in range(10):
    for j in range(10):
        if(i==j):
            print("",end="")
        else:
            print("*",end="")
    print()