import csv
import random
import time


x=0;
d1=1000;
d2=1000;

fieldname=['x','d1','d2']

with open('data5.csv','w')as csv_file:
   csv_Writer=csv.DictWriter(csv_file,fieldnames=fieldname)
   csv_Writer.writeheader();


while True:

    with open('data5.csv','a')as csv_file:
        csv_Writer=csv.DictWriter(csv_file,fieldname)

        index={
               'x':x,
               'd1':d1,
               'd2':d2


        }

        csv_Writer.writerow(index);
        print(x,d1,d2)


        x=x+1;
        d1=d1+random.randint(0,10);
        d2=d2+random.randint(0,10);

    time.sleep(1)
