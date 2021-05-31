from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from numpy import linalg as LA
import numpy as np
from numpy import *
def MODELE_3D(n,nbr,lambda1,lambda2,alpha,R0,K,Vlim,lambdap,xp,yp,zp): #nbr = nombre de boids et n =nombre d'itération
    #Conditions initiales
    Boids0=20*np.random.rand(3,nbr)
    Vboids0=0.2*np.random.rand(3,nbr)
    #Initialisation
    Boids=zeros((3,n,nbr))
    Vboids=zeros((3,nbr))
    Fatt=zeros((3,nbr))
    Frep=zeros((3,nbr))
    Boids[:,0,:]=Boids0
    Vboids=Vboids0
    P0=array([xp,yp,zp])#position du poteau
    Vinfty=array([0,0,Vlim])#Vlim vitesse à partir de laquel on tend vers Vinfty
    for i in range (n-1) : # i nombre de tour
        Fatt=zeros((3,nbr)) #on remet à zéro à chaque tour
        Frep=zeros((3,nbr))
        theta1=random.rand()
        phi1=random.rand()
        if(random.rand()>0.5):# ajout d'une vitesse de direction aléatoire
            Vinfty=Vinfty+array([sin(pi*theta1)*cos(2*pi*phi1),sin(pi*theta1)*cos(2*pi*phi1),cos(pi*theta1)])/2
            Vinfty=Vinfty/LA.norm(Vinfty)
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
            if(LA.norm(Vboids[:,j])<Vlim):#recherche d’une vitesse inférieur à Vlim
                theta2=random.rand()
                phi2=random.rand()
                if(random.rand()>0.5):
                    Vboids[:,j]=Vboids[:,j]+array([Vlim-LA.norm(Vboids[:,j])])*array([Vinfty+array([sin(pi*theta2)*cos(2*pi*phi2),sin(pi*theta2)*cos(2*pi*phi2),cos(pi*theta2)])])/2
                else:
                    Vboids[:,j]=Vboids[:,j]+[Vlim-LA.norm(Vboids[:,j])]*Vinfty
            Boids[:,i+1,j]=Boids[:,i,j]+Vboids[:,j]#calcul de la position
            gca(projection='3d').plot(Boids[0,0 :i,j],Boids[1,0 :i,j],Boids[2,0 :i,j],"--",linewidth=0.5)
    if lambdap!=0 :
        gca(projection='3d').plot([xp],[yp],[zp],"v")
    show()
