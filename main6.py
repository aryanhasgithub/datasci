import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(1,20)
y1= x*x
y2 =x*x*x
plt.plot(x,y1,'r',linewidth=3,label="x^x")
plt.plot(x,y2,'b',linewidth = 4,label="x^x^x")
plt.show()
