def neon(no):
    square=no*no
    sum=0
    while square>0:
          sum = sum + square % 10
          square = square // 10
    if sum == no:
          print(no , " is a Neon Number")
    else:
          print(no, " is not a Neon Number")


neon(9)