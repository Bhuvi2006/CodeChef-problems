t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print("CAR")
    elif x==y:
        print("SAME")
    else:
        print("BIKE")
        
