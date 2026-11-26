q = [90,80, 67, 58, 49]
h = [87,89, 99, 47, 36]
a = [56,78, 46, 67, 69]


highest=0

exams_list = [q,h,a]
for each_exam in exams_list:
    total = 0
    for each_mark in each_exam:
        total += each_mark
        if total > highest :
           highest = total
    print(total)

print("Highest Total : " , highest)