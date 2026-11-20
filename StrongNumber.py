def factorial(no):
    i=1
    fact=1
    while i <= no :
          fact *= i
          i += 1
    return fact




def strong(no):
    sum=0
    while no>0:
          temp = no % 10
          no = no // 10
          fact=factorial(temp)
          sum += fact
    return sum
             





number=145
result=strong(number)

if number == result:
   print(number , ' is a Strong Number')
else:
   print(number , ' is a Strong Number')
