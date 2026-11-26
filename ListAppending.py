l1=[12,2,34,55,66]
l2=[78, 9 ,9.9 , 40 , 60 ,70 ,80 ]

small = len(l1) if len(l1) < len(l2) else len(l2)


l3=[]


i=0
while i< small :
      l3.append(l1[i] + l2[i])
      i += 1


while i<len(l2) :
      l3.append(l2[i])
      i += 1

print(l3)
print(i)
