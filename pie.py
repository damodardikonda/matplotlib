from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')


#plt.title("My basic pie chart")
#slices=[60,40]
#label=['python','java']
#plt.pie(slices,labels=label)# it is not necessary that pychart will be 100. it may be 90 sometime ao more then it


#plt.title("want to show limit is not 100")
#s=[90,40,30,40]
#lab=['python','java','mongoDB','JavaScript']
#color=['Blue','yellow','red','orange']
#plt.pie(s,labels=lab,colors=color,wedgeprops={'edgecolor':'black'})#wedgeprop is used to color  border of line



#plt.title("how many user thet lnguage");
#slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
#labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

#plt.pie(slices, labels=labels,  wedgeprops={'edgecolor':'black'})


plt.title("slicing one part")
s=[90,40,30,40]
lab=['python','java','mongoDB','JavaScript']
color=['Blue','yellow','red','orange']
exp=[0,0,0.5,0]# if you want to denote a slide. it explods mongo db

plt.pie(s,labels=lab,colors=color,explode=exp,shadow=True,startangle=90,autopct='%1.1f%%')#wedgeprop is used to color  border of line
#autopct :- it is used to show a percentage with it. if we increase value then it increases a points



plt.tight_layout()
plt.show()
