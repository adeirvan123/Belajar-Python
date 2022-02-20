from matplotlib.lines import _LineStyle
import numpy as np
import matplotlib.pyplot as plt

def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t = np.arange(0, t_akhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinus_generator(1,1,4,0)
t2,y2 = sinus_generator(1,1,4,90)
t3,y3 = sinus_generator(1,1,4,180)

dataPlot1 =  plt.plot(t1,y1)
dataPlot2 = plt.plot(t2,y2)
dataPlot3 = plt.plot(t3,y3)

# set properti
plt.setp(dataPlot1, color='r', _LineStyle='--', linewidth=3)
plt.setp(dataPlot2, color='b', _LineStyle='--', linewidth=4)
plt.setp(dataPlot3, color='g', _LineStyle='-.', linewidth=2)

plt.show()