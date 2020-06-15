import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt

df=sb.load_dataset('iris')
sb.distplot(df['petal_length'] , kde=False)
#distplot :- it is an function which combines matplotlib histogram with the seaborn kdeplot() and rugplot()
#kde:- kernal estimation plot
plt.show()
