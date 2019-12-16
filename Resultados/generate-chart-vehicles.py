"""
Generate Chart from files genereted by simulations
with 95% CI

This program reads data from files:
 - broadcast-10m-vehicles.log.log
 - broadcast-5m-vehicles.log
 - R3G3M-10m-vehicles.log
 - R3G3M-5m-vehicles.log
"""

import numpy as np                                                         
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
#creates Broadcast-10Mb, Broadcast-5Mb, R3G3M-10Mb, R3G3M-5Mb lists
bcast10 = []
bcast5 = []
R3G3M10 = []
R3G3M5 = []

#reads Broadcast-10Mb file
fileBCast10 = open('./broadcast-10m-vehicles.log', 'r')
values = fileBCast10.readlines()
for line in values :
	bcast10.append(float(line));
fileBCast10.close()
#print(bcast10)

#reads Broadcast-5Mb file
fileBCast5 = open('./broadcast-5m-vehicles.log', 'r')
values = fileBCast5.readlines()
for line in values :
	bcast5.append(float(line));
fileBCast5.close()
#print(bcast5)

#reads R3G3M-10Mb file
fileR3G3M10 = open('./R3G3M-10m-vehicles.log', 'r')
values = fileR3G3M10.readlines()
for line in values :
	R3G3M10.append(float(line));
fileR3G3M10.close()
#print(R3G3M10)

#reads R3G3M-5Mb file
fileR3G3M5 = open('./R3G3M-5m-vehicles.log', 'r')
values = fileR3G3M5.readlines()
for line in values :
	R3G3M5.append(float(line));
fileR3G3M5.close()
#print(R3G3M5)

#creates np.array
arrayBCast10 = np.array([bcast10])
arrayBCast5  = np.array([bcast5])
arrayR3G3M10   = np.array([R3G3M10])
arrayR3G3M5    = np.array([R3G3M5])

#computes mean
meanBCast10 = arrayBCast10.mean()
meanBCast5  = arrayBCast5.mean()
meanR3G3M10   = arrayR3G3M10.mean()
meanR3G3M5   = arrayR3G3M5.mean()
print(meanBCast10)
print(meanBCast5)
print(meanR3G3M10)
print(meanR3G3M5)

#computes std deviation
devBCast10 = np.std(arrayBCast10)
devBCast5  = np.std(arrayBCast5)
devR3G3M10   = np.std(arrayR3G3M10)
devR3G3M5    = np.std(arrayR3G3M5)
print(devBCast10)
print(devBCast5)
print(devR3G3M10)
print(devR3G3M5)

#computes confidence interval
#cIntRSA = [meanRSA-(1.96*(devRSA/(8**(1/2)))), media+(1.96*(devRSA/(8**(1/2))))]
Z=1.96
cIntBCast10 = (Z*(devBCast10/(arrayBCast10.size**(1/2))))
cIntBCast5  = (Z*(devBCast5/(arrayBCast5.size**(1/2))))
cIntR3G3M10   = (Z*(devR3G3M10/(arrayR3G3M10.size**(1/2))))
cIntR3G3M5    = (Z*(devR3G3M5/(arrayR3G3M5.size**(1/2))))
print(cIntBCast10)
print(cIntBCast5)
print(cIntR3G3M10)
print(cIntR3G3M5)

#creates chart
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 14

N = 2
fig, ax = plt.subplots()
ind = np.arange(N)
barWidth = 0.25

g10m   = [meanBCast10, meanBCast5]
gCI10m = [cIntBCast10, cIntBCast5]
g1 = ax.bar(ind, g10m, barWidth, yerr=gCI10m, hatch="/", capsize=7)

g5m    = [meanR3G3M10, meanR3G3M5]
gCI5m  = [cIntR3G3M10, cIntR3G3M5]
g2 = ax.bar(ind + barWidth, g5m, barWidth, yerr=gCI5m, color="tab:cyan", capsize=7)

#ax.set_title('Mensagens de 10Mb e 5Mb')
ax.set_xticks(ind + barWidth/2)
ax.set_xticklabels(('Mensagens de 10Mb', 'Mensagens de 5Mb'))
ax.legend((g1[0], g2[0]), ('Broadcast', 'ReG3M'))
#ax.yaxis.set_units(inch)
plt.ylabel('Número de veículos alcançados', fontsize=16)
ax.autoscale_view()

#########################################################################################3
# For each bar: Place a label
for rect in ax.patches:
    # Get X and Y placement of label from rect.
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2

    # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    va = 'bottom'

    # Use Y value as label and format number with one decimal place
    label = "{:.1f}".format(y_value)

    # Create annotation
    ax.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        fontsize=16,
        xytext=(-25, space),        # Vertically shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        ha='right',                 # Horizontally center label
        va=va)                      # Vertically align label differently for
                                    # positive and negative values.

plt.show()


