no=1013
divisor=2
count = 0
n=0

while divisor <= no // 2:
      if no % divisor == 0:
         count += 1;
         print(divisor)
      divisor += 1
      n += 1;
     
print('No of Divisor:',count)
print(n)

if count == 0:
   print(count , ' is a prime number')

else:
   print(count , ' is not a prime number')
