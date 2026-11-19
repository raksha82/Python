div=57
no=10

while no <=99:
    if div % no == 0:
       new_no=no
       sum=0
       while new_no>0:
          temp = new_no % 10
          sum += temp
          new_no =  new_no//10
       if sum == 10:
          print("Two digit number and factor of 57 and sum of digits is 10 , that number is:", no)
          break
    no += 1
    sum=0
    

