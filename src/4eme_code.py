import numpy as np
import matplotlib.pyplot as plt
from math import *
def FattrGaussA(lambda1,lambda2,R0):
    t=np.linspace(0,10,1000)
    Fattr = lambda1*np.exp(-(((t/2)-R0/2)/lambda2)**2)
    plt.plot(t,Fattr)
    plt.xlabel("distance")
    plt.ylabel("intensité de la force")
    plt.show()
