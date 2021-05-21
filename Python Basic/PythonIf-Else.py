import math

n= int(input().strip())
x=float(math.fmod(n,2))

if x==1:
    print("Weird")
elif 2<= n <=5:
    print("Not Weird")
elif 6<= n <=20:
    print("Weird")
else:
    print("Not Weird")
