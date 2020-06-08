import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

dat = pd.read_csv('data1.csv')
ages = dat['Age']
dev_salaries = dat['All_Devs']
py_salaries = dat['Python']
js_salaries = dat['JavaScript']

fig1, ax1 = plt.subplots()#sharex=True then it takes common x name
fig2, ax2 = plt.subplots()#sharey=True then it takes common y name
#fig,(ax1,ax2)=plt.subplot(sharex=True) it will create only 1 figurewith 2 axis
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

fig1.savefig('subplot1.png')
fig2.savefig('subplot2.png')
