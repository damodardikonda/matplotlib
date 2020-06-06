#Reading CSV file using pandas becausen it read csv file quickly

import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')


data=pd.read_csv('data.csv')
ids=data['Responder_id']
lang=data['LanguagesWorkedWith']


lang_counter=Counter()
for row in lang:
    lang_counter.update(row.split(';'))#it will split the languages with different part and store it into lang counter

    #print(lang_counter.most_common(15))it takes firt 15 no.

print("so here we want to split data into 2 list")

language=[]
popular=[]

for item in lang_counter.most_common(15):
    language.append(item[0])
    popular.append(item[1])


language.reverse()#for taking most popular lang at top instad of bottom
popular.reverse()#for taking most popular at top instad of bottom

plt.barh(language,popular)#for showing Bar Horizontal
plt.title("languages and their popularity");
plt.ylabel('language')
plt.xlabel('popular')


plt.tight_layout();
plt.show()



    # next() is used for printing current row.it is printing header file
    #row=next(csv_reader)
    #print(row)
   #if you want to print a spectific value then
    #print(row['LanguagesWorkedWith'].split(';'))
