# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:29:08 2026

@author: talal
"""

from matplotlib import pyplot as plt
import numpy as np

#Problem 1
A = 10
a = 2
k = 0.41
xs = 0.1
Spacing = int(20/xs)
x = np.linspace(0,20,Spacing)
def E(x):
    return A * np.cos((np.pi*x)/a) * np.exp(-k*x)
e = list(E(x))
plt.figure(1)
plt.plot(x, E(x), label = "Electric Field")
plt.xlabel("Position x (m)")
plt.ylabel("Electric Field E (V/m)")
plt.title("Electric Field vs. Position")
#print(e)

#Problem 2
h = xs
d = 2 * h

i = 0
FDerivative = []
CDerivative = []
while i <= (len(x) - 2):
    FDerivative1 = (e[i+1] - e[i])/h 
    CDerivative1 = (e[i+1] - e[i-1])/d
    FDerivative.append(FDerivative1)
    CDerivative.append(CDerivative1)
    i += 1
    
Analytical = (-A * (np.pi/a) * np.sin((np.pi*x)/a) * np.exp(-k*x)) + ( -k * A * np.cos((np.pi*x)/a) * np.exp(-k*x))
plt.figure(2)
plt.plot(x[:-1], FDerivative, label = "Forward Differencing")
plt.plot(x[:-1], CDerivative, label = "Central Differencing")
plt.plot(x, Analytical, label = "Analytical")
plt.xlabel("Position x (m)")
plt.ylabel("Electric Field Derivative E (V/m^2)")
plt.title("Electric Field Derivative vs. Position")
plt.legend()

plt.figure(3)
Diff_Btw_For_and_Antly = []
Diff_Btw_Cen_and_Antly = []
for xx in range(len(x) - 1):
    diff1 = abs(FDerivative[xx] - Analytical[xx])
    Diff_Btw_For_and_Antly.append(diff1)
    diff2 = abs(CDerivative[xx] - Analytical[xx])
    Diff_Btw_Cen_and_Antly.append(diff2)

    
plt.plot(x[:-1], (Diff_Btw_For_and_Antly), label = "Forward Differencing") 
plt.plot(x[:-1], (Diff_Btw_Cen_and_Antly), label = "Central Differencing") 
plt.yscale("log")
plt.xlabel("Position x (m)")
plt.ylabel("Difference Compared to Analytical")
plt.title("Error vs. Position")
plt.legend()

xs_xaxis = np.linspace(10e-1, 10e-15, 10000)
FDerv = (E(1 + range(len(xs_xaxis))) - E(1))/xs_xaxis
Analytical2 = (-A * (np.pi/a) * np.sin((np.pi*1)/a) * np.exp(-k*1)) + ( -k * A * np.cos((np.pi*1)/a) * np.exp(-k*1))
Diff_Btw = abs(FDerv - Analytical2)
plt.figure(4)
plt.plot(xs_xaxis, Diff_Btw)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Delta_x (m)")
plt.ylabel("Difference Compared to Analytical")
plt.title("EXTRA CREDIT!!!")



# Problem 3
yaxis = np.loadtxt('Assignment5.txt')
time = np.linspace(0, 24, len(yaxis))
plt.figure(5)
plt.plot(time, yaxis)
plt.title("EUV Spectrum vs Time")
plt.xlabel("Time (Hours)")
plt.ylabel("EUV Spectrum (W/m^2/nm)")
plt.show()

