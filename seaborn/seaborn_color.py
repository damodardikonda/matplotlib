#color_palette() which can be used to give colors to plots and adding more aesthetic value to it.
# syntax= seaborn.color_palette(palette=None ,n_color=None, desat=None)
from matplotlib import pyplot as plt
import seaborn as sb
current_palette = sb.color_palette()
sb.palplot(current_palette)
plt.show()
