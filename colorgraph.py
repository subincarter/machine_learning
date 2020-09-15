import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.markers

label=(0,20,40,60,80,100,120,140,160)
positions=(0,2,4,6,8,10,12,14,16)
plt.xticks(positions,label)
plt.xticks(np.arange(0,18,step=2))
plt.xlim([0,16.5])

label=(0,200,400,600,800,1000)
positions=(0,3,6,9,12,15)
plt.yticks(positions,label)
plt.yticks(np.arange(0,18,step=3))
plt.ylim([0,16.5])


x1=[0.04,2.90,2.98,3.22,3.10,3.42,3.83,3.83,4.46,4.57,4.90,4.86,7.08]
y1=[7.46,7.51,5.71,5.66,3.61,3.03,2.59,2.35,2.20,0.84,0.89,0.06,0.06]

plt.plot(x1,y1 ,color='red',marker='v', markerfacecolor='red', markersize=6,label=" ICA optimized FTIDF-II",linewidth=4)

x2=[0.04,2.90,2.98,3.22,3.10,3.42,3.83,3.83,4.46,4.57,5.55,5.92,7.08,7.91]
y2=[8.46,8.51,6.71,6.66,4.61,4.03,3.59,3.35,3.20,0.84,1.01,0.69,0.06,0.06]

plt.plot(x2,y2,color='blue',marker='o', markerfacecolor='blue', markersize=6,label="ICA optimized CFFOPI-FOPID",linewidth=4)

x3=[0.04,2.90,2.98,3.22,3.10,3.42,3.83,3.83,4.46,4.57,5.55,5.92,6.24,6.60,7.08,7.81]
y3=[9.26,9.51,7.71,7.66,5.61,5.03,4.59,4.35,4.20,3.27,3.21,2.05,1.76,1.03,0.06,0.36]

plt.plot(x3,y3,color='green',marker='^', markerfacecolor='green', markersize=6,label=" ICA optimized FPIDF-(I+PI)",linewidth=4)

x4=[0.04,3.56,3.70,4.61,4.65,5.19,5.66,6.46,6.71,7.26,7.33,10.00]
y4=[9.85,10.24,7.56,7.46,6.83,6.78,5.61,5.42,1.81,1.62,0.85,0.01]
plt.plot(x4,y4,color='lightblue',marker='D', markerfacecolor='lightblue', markersize=6,label=" ICA optimized FFOPI-FOPD",linewidth=4)

x5=[0.04,3.86,4.00,4.91,4.95,6.06,5.96,6.90,7.15,7.26,7.87,8.27,10.00]
y5=[10.85,10.82,8.86,8.76,8.50,8.52,5.91,5.71,2.15,1.62,1.57,0.50,0.01]
plt.plot(x5,y5,color='black',marker='*', markerfacecolor='black', markersize=6,label="ICA optimized FPIDN-FOI",linewidth=4)

x6=[0.04,3.44,4.57,5.81,7.04,7.11,7.26,8.13,8.17,8.71,8.60,8.96,9.94,10.52]
y6=[11.50,11.50,10.57,9.94,8.58,8.52,6.88,5.61,4.10,3.27,1.42,0.64,0.30,0.25]
plt.plot(x6,y6,color='pink',marker='+', markerfacecolor='pink', markersize=6,label=" ICA optimized PFFPID",linewidth=4)


x7=[0.04,4.44,4.87,6.11,7.54,7.61,7.76,8.63,8.67,8.99,8.95,9.26,9.94,10.52,11.18]
y7=[12.07,12.00,10.87,10.24,8.98,8.92,7.28,5.91,4.60,3.77,1.82,1.04,0.30,0.25,0.06]
plt.plot(x7,y7,color='orange',marker='3', markerfacecolor='orange', markersize=6,label="EVI optimized FTIDF-II",linewidth=4)


x8=[0.04,4.94,5.10,6.50,7.94,7.91,7.96,8.93,8.97,9.30,9.20,9.76,10.24,10.92,11.18]
y8=[12.67,12.50,11.10,10.74,9.28,9.22,7.78,6.21,4.90,4.10,1.50,0.89,0.50,0.40,0.06]
plt.plot(x8,y8,color='purple',marker='8', markerfacecolor='purple', markersize=6,label=" EVI optimized CFFOPI-FOPID",linewidth=4)

x9=[0.04,5.20,5.50,7.20,8.30,8.41,8.30,9.20,9.20,9.80,9.70,10.00,10.84,11.22,11.88]
y9=[13.50,13.20,11.60,10.99,9.80,9.92,8.10,6.80,5.30,4.60,2.60,1.94,0.55,0.45,0.06]
plt.plot(x9,y9,color='grey',marker='s', markerfacecolor='grey', markersize=6,label=" EVI optimized FPIDF-(I+PI)",linewidth=4)

x10=[0.04,1.38,3.99,2.69,  5.20,5.90,      7.80,8.90,8.91,8.90,9.70,9.92,10.10,9.99,10.30,10.84,11.22,11.88]
y10=[13.99,13.89,13.89,13.89, 13.90,11.99, 11.39,10.20,10.22,8.60,7.20,5.95,5.00,2.95,2.14,0.55,0.45,0.06]
plt.plot(x10,y10,color='lightgreen',marker='p', markerfacecolor='lightgreen', markersize=6,label="EVI optimized FFOPI-FOPD",linewidth=4)

x11=[0.04,1.38,3.99,2.69,  5.20,5.28,      5.28, 6.06 ,7.46, 8.11,8.99,9.10,9.90,9.92,10.40,9.99,10.60,10.84,11.62,11.88]
y11=[14.90,14.96,14.96,14.96, 14.99,14.39, 14.39,13.05 ,12.68, 12.69,10.80,8.80,7.70,5.95,5.40,2.95,2.54,0.55,0.475,0.06]
plt.plot(x11,y11,color='brown',marker='H', markerfacecolor='brown', markersize=6,label="EVI optimized FPIDN-FOI",linewidth=4)

x12=[0.04,1.38,3.99,2.69,  5.20,5.28,      5.28, 6.06 ,7.46, 8.11,8.99,9.10,9.90,9.92,10.40,9.99,10.60,10.84,11.62,11.88]
y12=[15.68,15.96,15.96,15.96, 15.99,15.39, 15.39,14.05 ,13.68, 13.69,11.80,9.80,6.70,6.95,6.40,3.95,2.54,0.55,0.475,0.06]
plt.plot(x12,y12,color='yellow',marker='H', markerfacecolor='yellow', markersize=6,label="EVI optimized PFFPID",linewidth=4)
# legend.reverse()
# leg=plt.legend()
current_handles, current_labels = plt.gca().get_legend_handles_labels()
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))
plt.legend(reversed_handles,reversed_labels)

plt.xlabel('Iterations')
plt.ylabel('Objective value')
plt.show()