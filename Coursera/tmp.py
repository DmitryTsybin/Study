import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 3], [0.2, 0.1, 0.3, 0.4], 'ro')
plt.axis([-1, 4, 0, 1])
plt.ylabel('distribution values')
plt.xlabel('degrees')
plt.title('in degree distribution')
#plt.grid(True)
print '2'
plt.show()
