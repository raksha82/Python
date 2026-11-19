

def perfect_no(no) :
          temp = no // 2
          print('temp' , temp)
          num = no
          i=1
          sum=0
          while temp>=i:
             if num % i == 0 :
                sum += i
                print('i',i)
                print("sum" , sum)
                i +=1
             if sum == no :
                print("Perfect Number ", no)
                break
             else:
                print("Not a Perfect Number ", no)
                
             

print("Not perfect Number")


perfect_no(24)
    