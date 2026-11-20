def neon(no):
    square=no*no
    sum=0
    while square>0:
          sum = sum + square % 10
          square = square // 10
    return sum
    

no=9
result=neon(no)
if result == no:
   print(no , " is a Neon Number")
else:
   print(no, " is not a Neon Number")