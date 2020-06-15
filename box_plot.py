import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

print("Box-plot/Box and whisker plot/ Box and whisker diagram")
# whisker is an point which is present at the outside of diagram

df = sb.load_dataset('iris')
sb.boxplot(x = "species", y = "petal_length", data = df)
plt.show()
