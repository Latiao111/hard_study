
for num in range(1,500):
    prime = True
    for a in range(2,num-1):
       if num%a==0:
        prime=False
    if prime:
     print(num)

#prime nice try
