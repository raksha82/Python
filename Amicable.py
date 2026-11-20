def factor(no):
    fact=1
    half=no//2
    sum=0
    while fact <= half:
          if no % fact == 0:
             sum += fact
          fact += 1
    return sum


no1=1184
no2=1210
result1=factor(no1)
result2=factor(no2)

if(no1 == result2 and no2 == result1):
   print(no1 , ' and ' , no2 , ' are Amicable Numbers')
    