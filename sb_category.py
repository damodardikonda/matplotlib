import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb


#stripplot() is used when one of the variable under study is categorical.
#It represents the data in sorted order along any one of the axis.

df=sb.load_dataset('iris')
sb.stripplot(x='species', y='petal_length', data=df ,jitter=True)
plt.show()

#jitter:-it is used for specifing exact location of data.

#insted of using jitter we can use swarmplot()
#swarmplot():=this function plot every point in perticulr way that it doesnt overlap each other

df1=sb.load_dataset('iris')
sb.swarmplot(x='species',y='petal_length',data=df)
plt.show()

#it does not requires jitter function
