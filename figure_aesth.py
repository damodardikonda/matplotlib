import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

#print("print sinewave for matplotlib library")
#def sinplot(flip=1):# flip is nothing but the curve 1=yes it curves , o0=no curve
#    x=np.linspace(0,14,100)
#    for i in range(1,5):
#        plt.plot(x,np.sin(x+i *.5) * (7-i) * flip)

#sinplot()# not a predefine function
#plt.show()


#print("To change the same plot to Seaborn defaults, use the set() function −")

#print("print sinewave for seaborn library")
#def sea_sinplot(flip=1):# flip is nothing but the curve 1=yes it curves , o0=no curve
#    x=np.linspace(0,14,100)
#    for i in range(1,5):
#        plt.plot(x,np.sin(x+i *.5) * (7-i) * flip)

#sb.set()#set() is used to convert an matplotlib to seaborn
#sea_sinplot()# not a predefine function
#plt.show()

#The above two figures show the difference in the default Matplotlib and Seaborn plots.
#The representation of data is same, but the representation style varies in both.


print("setting theme")
def sea_sinplot(flip=1):
    x=np.linspace(0,14,100)
    for i in range(1,5):
        plt.plot(x,np.sin(x+i *.5) * (7-i) * flip)

sb.set_style('dark')
sea_sinplot()
plt.show()
