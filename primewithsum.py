def sum_of_digits(no):
    total = 0
    while no > 0:
        total = total + no%10
        no = no //10
    return total

def find_prime(no): #12
    div = 2
    while div <= no//2:     #10 Times 
        if no % div == 0:
            return False 
        div+=1
    else:
        return True


no = 11
while no <= 99:
    result = find_prime(no) #Calling Statement
    if result == True: 
        print("Prime Number", no)
        total = sum_of_digits(no)
        if total == 10:
            if 57 % no == 0:
                print("Yes, I found", no)
    no+=2