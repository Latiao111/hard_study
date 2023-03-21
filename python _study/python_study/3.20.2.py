num=int(input('num='))
aim_num=0
while num>0:
    aim_num=num%10+aim_num*10
    num//=10
    print(aim_num)

#concise and powerful code