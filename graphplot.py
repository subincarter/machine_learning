import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import style


x = [0.40,0.46,0.50,0.54,0.60,0.65,0.71,0.79,0.87,1.05,1.11,1.25,1.25,1.47,1.53,1.69,1.69,1.75,1.79,1.83,1.94,2.06,2.30,2.50,2.58,
     2.60,2.64,2.66,2.72,2.80,2.86,2.98,3.00,3.04,3.12,3.17,3.29,3.35,3.47,3.51,3.53,3.57,3.67,3.77,3.83,3.97,3.99,4.07,4.11,4.23,
     4.29,4.29,4.42,4.46,4.52,4.56,4.62,4.62,4.68,4.68,4.74,4.76,4.84,4.86,4.92,4.98,4.96,5.08,5.10,5.16,5.32,5.38,5.42,5.52,5.56,
     5.65,5.67,5.77,5.75,5.81,5.97,5.97,6.15,6.19,6.27,6.31,6.57,6.79,6.90,6.94,7.04,7.12,7.22,7.24,7.54,7.64,7.72,7.90,8.00,8.15,
     8.15,8.25,8.33,8.53,8.53,8.69,8.73,8.81,8.83,9.01,9.15,9.29,9.48]


y = [3.26,2.45,3.04,2.40,2.77,1.93,2.31,1.49,1.66,1.09,0.65,1.09,1.55,1.28,1.52,1.03,1.39,1.09,1.41,1.09,1.66,1.20,3.58,3.36,2.87,
     3.23,3.14,3.47,3.50,4.31,3.96,5.17,4.48,5.55,6.26,5.61,6.26,5.80,6.12,5.98,6.12,6.01,6.85,5.98,5.93,5.17,5.52,4.15,4.47,2.17,
     2.47,2.03,3.82,3.66,3.96,3.69,3.87,3.66,3.85,3.60,3.79,3.55,3.74,3.38,3.58,3.41,3.90,3.72,3.09,3.44,3.25,2.68,2.92,2.17,2.79,
     2.44,2.68,2.68,3.03,2.93,3.09,2.87,3.09,2.85,3.28,3.09,3.66,3.93,3.52,3.74,3.33,3.52,2.39,3.06,3.55,3.09,3.41,3.70,3.34,3.63,
     3.96,3.26,3.58,3.63,4.26,3.23,3.66,3.31,3.60,3.71,3.06,3.71,2.36]


label=("mar 2000","mar 2005","mar 2010","mar 2015","mar 2020")
positions=(0,2,4,6,8)
# label=(2,3,4,5,6)
plt.xticks(positions,label)

plt.xticks(np.arange(0, 10, step=2))
plt.xlim([0,10])

ylabel=(-20,-10,0,10,20,30,40,50)
ypositions=(0,1,2,3,4,5,6,7)

plt.yticks(ypositions,ylabel)

plt.yticks(np.arange(0,8))
plt.ylim([0,7])
plt.plot(x,y)
plt.xlabel("date")
plt.ylabel("percentage")
plt.show()
