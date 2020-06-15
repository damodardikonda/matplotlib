import numpy as np
import pandas as pd
from matplotlib import pyplot as pyplot
import seaborn as sns
#%matplotlib inline


df=sns.load_dataset('tips')
#sns.barplot(x='day',y='tip', data=tips)
print(df.head())


print("for seeing present data set in seaborn")
#print(sns.get_dataset_names())
#['anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'exercise',
#'flights', 'fmri', 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 'planets', 'tips', 'titanic']

gamm=sns.load_dataset('gammas')
print(gamm.head())

pla=sns.load_dataset('planets');
print(pla.head())
