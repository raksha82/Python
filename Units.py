units_consumed = 100

if units_consumed <= 100:
    print("Free Electricity")
elif units_consumed <= 400:
    amount = units_consumed * 4.7
    print(amount)
elif units_consumed <= 500:
    amount = units_consumed * 6.3
    print(amount)
elif units_consumed <= 600:
    amount = units_consumed * 8.4
    print(amount)