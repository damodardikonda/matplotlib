#Factorplot draws a categorical plot on a FacetGrid. Using ‘kind’ parameter we
#can choose the plot like boxplot, violinplot, barplot and stripplot. FacetGrid uses pointplot by default.

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('exercise')
sb.factorplot(x = "time", y =" pulse", hue = "kind",data = df);
plt.show()


print('if you want to print as violine')
df1 = sb.load_dataset('exercise')
sb.factorplot(x = "time", y = "pulse", hue = "kind",kind="violine",data = df1);
plt.show()
