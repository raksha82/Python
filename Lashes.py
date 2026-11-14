lashes=1024
guard=0

while lashes > 1 :
   
    each_lashes = lashes // 2;
    guard += 1;
    lashes -= each_lashes
    print(guard , each_lashes)


print("No of Guards")
print(guard)
print("Remaining Lashes")
print(lashes);