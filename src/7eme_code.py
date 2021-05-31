from matplotlib.pyplot import *
from numpy import linalg as LA
import numpy as np
from numpy import *
def MODELE_GENERAL(n,nbr,lambda1,lambda2,alpha,R0,K,Vlim,lambdap,xp,yp): #nbr = nombre de boids et n =nombre d'itération
    #Conditions initiales
    Boids0=20*np.random.rand(2,nbr)
    Vboids0=0.2*np.random.rand(2,nbr)
    #Initialisation
    Boids=zeros((2,n,nbr))
    Vboids=zeros((2,nbr))
    Fatt=zeros((2,nbr))
    Frep=zeros((2,nbr))
    Boids[:,0,:]=Boids0
    Vboids=Vboids0
    P0=array([xp,yp])#position du poteau
    Vinfty=array([1,Vlim])#Vlim vitesse à partir de laquel on tend vers Vinfty
    for i in range (n-1) : # i nombre de tour
        Fatt=zeros((2,nbr)) #on remet à zéro à chaque tour
        Frep=zeros((2,nbr))
        for j in range (nbr):# j numéro de boids
            k=0
            while (k<nbr):
                if(k!=j): # on cumule les interractions pour chaques boids
                    dist=Boids[:,i,k]-Boids[:,i,j]
                    norme=LA.norm(dist)
                    Fatt[:,j]=Fatt[:,j]+lambda1*np.exp(-((norme-R0/2)/lambda2)**2)*(dist/norme)
                    Frep[:,j]=Frep[:,j]-(alpha/norme)*(dist/norme)
                k=k+1
            distp=P0-Boids[:,i,j]
            if LA.norm(distp)<5:
                FpoteaujP=-(lambdap/LA.norm(distp)**2)*distp
            else :
                FpoteaujP =0
            Vboids[:,j]=Vboids[:,j]/K+Frep[:,j]+Fatt[:,j]+ FpoteaujP #mise en place de la vitesse
            if(LA.norm(Vboids[:,j])<Vlim): #recherche d’une vitesse inférieur à vlim
                Vboids[:,j]=Vboids[:,j]+[Vlim-LA.norm(Vboids[:,j])]*Vinfty
            Boids[:,i+1,j]=Boids[:,i,j]+Vboids[:,j]#calcul de la position
            plot(Boids[0,0 :i,j],Boids[1,0 :i,j],linewidth=0.1) #afﬁchage des boids
    if lambdap!=0 :
        plot(xp,yp,"v")
    show()
