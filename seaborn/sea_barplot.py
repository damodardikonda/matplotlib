import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

#df=sb.load_dataset('titanic')
#sb.barplot(x='sex', y='survived',hue='class',data=df)#hue is used to differentiate a bar according to class
#plt.show()


#df1=sb.load_dataset('titanic')
#sb.countplot(x='class',data=df,palette='Blues')#hue is used to differentiate a bar according to class
#plt.show()


df2=sb.load_dataset('titanic')
sb.pointplot(x='sex', y='survived',hue='class',data=df2)#pointplot is denote only point rather than whole bar
plt.show()
