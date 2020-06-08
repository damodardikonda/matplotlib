import pandas as pd
from itertools import count
import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

#x_vals = [0, 1, 2, 3, 4, 5]
#y_vals = [0, 1, 3, 2, 3, 5]

#plt.plot(x_vals,y_vals)


#x=[]
#y=[]

#index=count()
#def animate(i):
#    x.append(next(index))
#    y.append(random.randint(0,5))
#    plt.cla()#it gives in sequence values
#    plt.plot(x,y)


def animate(i):

    da=pd.read_csv('data5.csv')
    x=da['x']
    d1=da['d1']
    d2=da['d2']

    plt.cla();
    plt.plot(x,d1,label='channel1');
    plt.plot(x,d2,label='channel2');

    plt.tight_layout();
    plt.legend();



fun=FuncAnimation(plt.gcf(),animate,interval=1000)#gcf= get current figure

#plt.plot(x,y)
plt.show();
