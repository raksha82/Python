
def duck(no):
    count=0
    temp=no
    while no>9:
          if(no%10 == 0):
             count +=1 
          no = no // 10
    if count > 0 and no % 10 != 0:
       print(temp,' is a Duck Number')
    else:
       print(temp,' is not a Duck Number')


duck(120340)
    
          