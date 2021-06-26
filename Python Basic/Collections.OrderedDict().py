from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    name,blank,price = input().rpartition(" ") 
    
    d[name]= d.get(name,0)+int(price)
    
    print (d[name])
# for i in d.items():
#     print(*i)