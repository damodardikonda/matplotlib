import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

#print("Removing Axes Spins from figures")
#def rem_spins(flip=1):
#    x=np.linspace(0,15,100)
#    for i in range(1,4):
#        plt.plot(x,np.sin(x + i*.5)*(7-i) * flip)

#sb.set()
#rem_spins()
#sb.despine()
#plt.show()

#print('overriding element')

#print(sb.axes_style)

print("Adding axes to figures")
def rem_spins(flip=1):
    x=np.linspace(0,15,100)
    for i in range(1,4):
        plt.plot(x,np.sin(x + i*.5)*(7-i) * flip)

sb.set_style('darkgrid',{'axes.axisbelow':True})
rem_spins()
sb.despine()
plt.show()
