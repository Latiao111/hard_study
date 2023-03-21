#公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print('x=%d,y=%d,z=%d'%(x,y,z))

#the above is the stander answer






