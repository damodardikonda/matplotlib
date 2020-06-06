#To construct a histogram, the first step is to “bin” the range of values — that is, divide the entire range of values into a series of intervals — and then count how many values fall into each interval.
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#Age=[18,20,24,25,29,33,36,38,39,42,45,48,51,53,55]

#plt.hist(Age,bins=5,edgecolor='Black')

#print("we can define our own bins range");

#plt.hist(Age,bins=bins,edgecolor='Black')

data=pd.read_csv('data2.csv')
Age=data['Age']
All_Devs=data['All_Devs']
bins=[10,20,30,40,50,60,70,80,90,100]

plt.hist(All_Devs,bins=bins,edgecolor='Black',log=True)

med_age=30

plt.axvline(med_age,color="Black")

plt.title("histogram")
plt.legend()
plt.show()
