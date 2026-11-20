def perfect_no(no) :
          if no <= 1:  # if the number is less than or equal to 1 , it returns 0
             return 0 
          temp = no // 2  # dividing the number to reduce the unwanted execution of loop
          i=1
          sum=0
          while temp>=i:
             if no % i == 0 :
                sum += i  #if the no is divide by i , then adding the i to sum
             i +=1
          return sum  # return sum of the factors
          
       
                
no=28      
result=perfect_no(no)
if result == no :
   print(no," is a Perfect Number ")
else:
   print(no," is Not a Perfect Number ")

    