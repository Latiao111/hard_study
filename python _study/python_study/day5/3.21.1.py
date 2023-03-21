#输出斐波那契数列的前20个数
a=0
b=1
for _ in range(0,20):
    a,b=b,a+b
    print(a,end=" ")