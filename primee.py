def find_prime(no): #12
    div = 2
    while div <= no//2:     #10 Times 
        if no % div == 0:
            return False 
        div+=1
    else:
        return True

no = 11
count =0 
while no <= 99 :
    result = find_prime(no) #Calling Statement
    if result == True: 
        count += 1
        print("Prime Number", no)
    no+=1

print('No of Prime' , count)