def find_prime(no): 
    div = 2
    while div <= no//2:  
        if no % div == 0:
            return False 
        div+=1
    else:
        return True

no = 11
first = True 
last_prime = no 
while no <= 99 :
    result = find_prime(no) #Calling Statement
    if result == True and first == True: 
        print("First Prime Number", no)
        first = False 
    elif result == True:
        last_prime = no  
    no+=1


print("Last Prime Number" , last_prime)