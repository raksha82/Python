List_L1 = [10,20,30]

for element in List_L1:
    print(element , " ")


l2=[40,50,60]


# List of List
# A list can store boolean , int , String , Float , we can also store another list in list
l3=[List_L1 , l2]
print(l3)
print("Length  of List l3 : " ,len(l3))

for each_list in l3:
    print(each_list)


for inner_list in l3:
    for each_element in inner_list :
        print(each_element , end = " ")

