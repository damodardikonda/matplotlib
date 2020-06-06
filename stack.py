from matplotlib import pyplot as plt

matches=[1,2,3,4,5,6]

player1=[90,56,125,30,2,88]
player2=[100,120,163,20,10,1]
player3=[20,14,5,142,120,76]

label=['player1','player2','player3']


plt.stackplot(matches,player1,player2,player3,labels=label);

plt.title("players score in perticular matches");
plt.xlabel("matches");
plt.ylabel("players");

plt.legend(loc='upper left');#we can give a tuple of co-ordinator of location
plt.tight_layout();

plt.show();
