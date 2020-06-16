#The major advantage of using Seaborn for many developers in Python world is
# because it can take pandas DataFrame object as parameter.

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.boxplot(data = df, orient = "h")
plt.show()


df1 = sb.load_dataset('iris')
sb.boxplot(data = df1, orient = "h")
plt.show()
