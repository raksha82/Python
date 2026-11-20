def sum(no):
    total=0
    while no>0:
          total += no % 10
          no = no // 10
    return total


def product(no):
    pro = 1
    while no>0:
          pro *= no % 10
          no = no // 10
    return pro

no=1412
pro_result=product(no)
sum_result=sum(no)

if(pro_result==sum_result):
   print(no , 'is a Spy number')

else:
   print(no , 'is not  a Spy number')



 