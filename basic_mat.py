#backend without using mat.use() command
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# create a new figure
fig=Figure()

#add a new figure to backend
can=FigureCanvasAgg(fig)

#add a subplot to figure
ax=fig.add_subplot(111)

#plot a point
ax.plot(3,2)

#printing an image
can.print_png('test.png')

plt.figure()

plt.plot(3,2,'o')

ax=plt.gca()# want to set xaxis manually

ax.axis([0,6,0,10])#min,max values for x and y 

ax.get_children()
