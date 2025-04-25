import matplotlib.pyplot as plt
x = [5,6,9,10,12]
y = [10,12,15,20,25]
y1 = [15,18,20,25,30]
plt.plot(x ,y,linestyle='dashed',marker='D')
plt.plot(x ,y1,linestyle='dashed',marker='D')
plt.title('Velocity-Time Graph')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.xlim(0,15)
plt.ylim(0,35)
plt.legend()
plt.show()
