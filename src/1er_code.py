from random import *
from numpy import *
from matplotlib.pyplot import *
from numpy import linalg as LA
#constantes : lambda1 (paramètre de la Fatt) et alpha (paramètre de la Frep)
def MODELE_SIMPLE(lambda1,alpha):
    #Nombre d’ite´ration
    n=600
    #Nombre de Bo¨ıds
    nbr=2
    #Position initiale
    A0=array([-10,3])
    B0=array([10,0])
    #initialisation des matrices de stockage de position
    A=zeros((2,n))
    B=zeros((2,n))
    #initialisation de la vitesse initiale aléatoire
    j1=random.random()
    j2=random.random()
    V=array([[cos(j1*2*pi),cos(j2*2*pi)],[sin(j1*2*pi),sin(j2*2*pi)]])
    #Affectation des positions initiales
    A[:,0]=A0
    B[:,0]=B0
    #Boucle de calcul des positions succesives
    for i in range(n-1):
        V[:,0]=V[:,0]+(lambda1-(4*alpha)/LA.norm(A[:,i]-B[:,i])**2)*(B[:,i]-A[:,i])/2
        V[:,1]=V[:,1]+(lambda1-(4*alpha)/LA.norm(A[:,i]-B[:,i])**2)*(A[:,i]-B[:,i])/2
        A[:,i+1]=A[:,i]+V[ :,0]
        B[:,i+1]=B[:,i]+V[ :,1]

    #Afﬁchage direct des trajectoires
    plot(A[0,:],A[1,:],'r')
    plot(B[0,:],B[1,:],"b")
    show()
