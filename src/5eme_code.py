from random import *
from matplotlib.pyplot import *
from numpy import linalg as LA
import numpy as np
def GENERALISATION_FORCES(lambda1,lambda2,alpha,R0,K,Vlim):
    n=600
    nbr=2
    A0=array([-10,3])
    B0=array([10,0])
    A=zeros((2,n))
    B=zeros((2,n))
    j1=random.random()
    j2=random.random()
    V=array([[cos(j1*2*pi),cos(j2*2*pi)],[sin(j1*2*pi),sin(j2*2*pi)]])
    Ulim=Vlim/LA.norm(Vlim)
    A[:,0]=A0
    B[:,0]=B0
    for i in range(n-1):
        distAB=(B[:,i]-A[:,i])/2
        distBA=(A[:,i]-B[:,i])/2
        FattrAB=lambda1*np.exp(-((LA.norm(distAB)-R0/2)/lambda2)**2)*distAB/LA.norm(distAB)#Force d'attraction en A par B
        FattrBA=lambda1*np.exp(-((LA.norm(distBA)-R0/2)/lambda2)**2)*distBA/LA.norm(distBA)#Force d'attraction en B par A
        #on annule la répulsion pour une certaines distance
        if LA.norm(distAB)<10 :
            FrepAB=-(alpha/LA.norm(distAB)**2)*distAB
        else :
            FrepAB=0
        if LA.norm(distBA)<10 :
            FrepBA=-(alpha/LA.norm(distBA)**2)*distBA
        else:
            FrepBA=0
        V[:,0]=V[:,0]/k+FattrAB+FrepAB
        V[:,1]=V[:,1]/k+FattrBA+FrepBA
        if LA.norm(V[:,0])> LA.norm(Vlim) or LA.norm(V[:,1])> LA.norm(Vlim):
            V[:,0]=V[:,0]/K+FattrAB+ FrepAB
            V[:,1]=V[:,1]/K+FattrBA+ FrepBA
            A[:,i+1]=A[:,i]+V[:,0]
            B[:,i+1]=B[:,i]+V[:,1]
        elif LA.norm(V[:,0])<= LA.norm(Vlim) or LA.norm(V[:,1])<= LA.norm(Vlim):
            V[:,0]=V[:,0]/K+FattrAB+ FrepAB + [LA.norm(Vlim)-LA.norm(V[:,0])]*Ulim
            V[:,1]=V[:,1]/K+FattrBA+ FrepBA + [LA.norm(Vlim)-LA.norm(V[:,0])]*Ulim
            A[:,i+1]=A[:,i]+V[:,0]
            B[:,i+1]=B[:,i]+V[:,1]
        A[:,i+1]=A[:,i]+V[:,0]
        B[:,i+1]=B[:,i]+V[:,1]
    plot(A[0,:],A[1,:],"r")
    plot(B[0,:],B[1,:],"b")
    show()
