import math 
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<=y:
        print(0)
    else:
        b=x-y
        a=b/4
        print(math.ceil(a))
