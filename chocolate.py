amount = 100
cost=5
count=0

while(amount>=cost):
  count += 1
  amount -= cost 

  if(count % 3 == 0):
    amount += 5

print('The maximum number of chocolates you can have with Rs. 100 is : ',count)

  
