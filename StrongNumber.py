def factorial(no):
    i=1
    fact=1
    while i<=no:
          fact *= i
          i += 1
    return fact



result=factorial(5)
print(result)