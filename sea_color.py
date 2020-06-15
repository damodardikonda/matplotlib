from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np
#current_palette = sb.color_palette()
#sb.palplot(current_palette)
#plt.show()

#color_palette() which can be used to give colors to plots and adding more aesthetic value to it.
# syntax= seaborn.color_palette(palette=None ,n_color=None, desat=None)


#print('sequential color plot')
#curr_palette=sb.color_palette()
#sb.palplot(curr_palette(green))
#plt.show()



print("Diverging 2 color")
c_palette=sb.color_palette()
sb.palplot(sb.color_palette('BrBG',7))
plt.show()

print("setting a default color palette")
def rem_spins(flip=1):
    x=np.linspace(0,15,100)
    for i in range(1,4):
        plt.plot(x,np.sin(x + i*.5)*(7-i) * flip)

sb.set()
rem_spins()
sb.set_palette("husl")
plt.show()
