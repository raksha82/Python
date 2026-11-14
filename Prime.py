no = 3
start=2

while start <= no // 2:
      if no % start == 0:
         print(no , ' is not a prime')
         break
      start += 1
else:
     print(no, 'Prime Number')