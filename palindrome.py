number = 12231
temp = number
rev=0

while number > 0:
      rev = rev*10 +  number%10
      number //= 10 



if(rev == temp):
   print(temp , ' is a Palindrome Number')

else:
   print(temp , ' is not  a Palindrome Number')
