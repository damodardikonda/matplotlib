import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

#violine():-is an combination of box-plot and  kernal density estimates

df=sb.load_dataset('tips')
sb.violinplot(x = "day", y = "total_bill", data=df)
plt.show()
