train1=1;
train2=1;
count=1
last_station=0
first_station=True

while count<=100 :
     
     if train1 % 3 == 0 and train2 % 5==0 :
        if first_station == True:
           print('First Station',train1)
           first_station = False
        else:
           print('Common Stations' ,train1)
           last_station=train1
     train1 += 1
     train2 += 1
     count += 1


print('Last Station:',last_station) 
