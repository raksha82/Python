def perfect_no(no) :
          temp = no // 2
          num = no
          i=1
          sum=0
          while temp>=i:
             if num % i == 0 :
                sum += i
             i +=1
          if sum == no :
             print("Perfect Number ", no)
          else:
             print("Not a Perfect Number ", no)
       
                
            
perfect_no(28)

    