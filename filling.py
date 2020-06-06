import pandas as pd
from matplotlib import pyplot as plt



datas=pd.read_csv('data1.csv')

Age=datas['Age'];
All_Devs=datas['All_Devs'];
python=datas[Python];
JavaScript=datas[JavaScript];

plt.plot(ages,All_Devs,labels='All_Devs',linestyle='--')

overall_median=70000

plt.fill_between(Age,python,overall_median, where=(python>overall_median),interpolate=True,alpha=0.25,color='Blue')#interpolate is used to only highlight upper area of that point

plt.fill_between(Age,python,overall_median, where=(python<=overall_median),interpolate=True,alpha=0.25,color="Red")#interpolate is used to only highlight upper area of that point



#print('printingg an area between All_Devs and python')
#plt.fill_between(Age,python,All_Devs, where=(python>All_Devs),interpolate=True,alpha=0.25)#interpolate is used to only highlight upper area of that point 


plt.legend();
plt.title()
