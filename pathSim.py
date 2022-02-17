import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#in payoff calc section: include strike, barrier, american = True, long = True
#Utility function for simulating paths
def pathSimulator(spot, dte, iv, rho, iters, dt = 0.05):
    #Scale iv to daily
    iv/= (252**0.5)
    #Scale risk free rate to daily
    rho+=1
    rho**=(1/252)
    rho-=1
    paths = []
    for i in range(iters):
        prices = [spot]
        for step in range(int(dte/dt)):
            #Geometric Brownian Motion
            prices.append(prices[-1] * (1 + ((rho * dt) + (iv * np.sqrt(dt) * np.random.normal(0,1)))))
        paths.append(prices)
    return paths
times = [0.05 * i for i in range(2001)]
pths = pathSimulator(100, 100,0.25, 0.04, 100)
for pth in pths:
    plt.plot(times, pth, markersize = 1)
plt.show()
