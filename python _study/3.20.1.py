for num in range(100,10000):
    low=num%10
    mid=num//10%10
    high=num//100% 10
    best=num//1000
    if num==low**3+mid**3+high**3+best**3:
        print(num)

 #if num bigger than 1000,do not have world like this .
 #so we need not best

 