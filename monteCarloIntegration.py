#Recommended to run in jupyter Notebook
import random as rd
import math as mt
import matplotlib.pyplot as plt
n=100000
arr=[]
nsamp=10000       #increase sample size for better accuracy
while nsamp>0:
    j=0
    for i in range(n):
        x=mt.pi*rd.random()
        y=6*rd.random()
        fx=(x**2)*(mt.sin(x))
        if y<=fx:
            j+=1
    ifx=6*mt.pi*j/n
    nsamp-=1
    arr.append(ifx)
plt.hist(arr)
