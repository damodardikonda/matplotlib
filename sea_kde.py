import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

#df=sb.load_dataset('iris')
#sb.distplot(df['petal_length'],hist=False)

#distplot :- it is an function which combines matplotlib histogram with the seaborn kdeplot() and rugplot()
#kde:- kernal estimation plot

#plt.show()


print('with both  hist and kde')
#df1=sb.load_dataset('iris')
#sb.distplot(df1['petal_length'])
#plt.show()



print('Bivariate distribution')# it shows the relationship between 2 variables
#df2=sb.load_dataset('iris')
#sb.jointplot(x='petal_length',y='petal_width',data=df2)
#Jointplot creates a multi-panel figure that projects the bivariate relationship between two
#variables and also the univariate distribution of each variable on separate axes.
#plt.show()



print('hexbin plot')# it is used when data is very scattered(vikhurlela) and unable to plot with scattered
#df3=sb.load_dataset('iris')
#sb.jointplot(x='petal_length',y='petal_width',data=df3,kind='hex')
#plt.show()



df4 = sb.load_dataset('iris')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df4,kind = 'hex')
plt.show()
