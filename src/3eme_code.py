from random import *
from numpy import *
from matplotlib.pyplot import *
from numpy import linalg as LA
def VITESSE_LIMITE(lambda1,lambda2,K,Vlim):
    #Nombre d’itération
    n=600
    #Nombre de Boids
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
    B[ :,0]=B0
    #direction de la vitesse limite
    Ulim=Vlim/LA.norm(Vlim)
    #Boucle de calcul des positions succesives
    for i in range(n-1):
        if LA.norm(V[:,0])> LA.norm(Vlim) or LA.norm(V[:,1])> LA.norm(Vlim):
            V[:,0]=V[ :,0]/K+(lambda1-(4*alpha)/LA.norm(A[:,i]-B[:,i])**2)*(B[:,i]-A[:,i])/2
            V[:,1]=V[ :,1]/K+(lambda1-(4*alpha)/LA.norm(A[:,i]-B[:,i])**2)*(A[:,i]-B[:,i])/2
            A[:,i+1]=A[:,i]+V[ :,0]
            B[:,i+1]=B[ :,i]+V[ :,1]
        elif LA.norm(V[:,0])<= LA.norm(Vlim) or LA.norm(V[:,1])<= LA.norm(Vlim):
            V[:,0]=V[ :,0]/K+(lambda1-(4*alpha)/LA.norm(A[:,i]-B[:,i])**2)*(B[:,i]-A[:,i])/2+[LA.norm(Vlim)-LA.norm(V[:,0])]*Ulim
            V[:,1]=V[ :,1]/K+(lambda1-(4*alpha)/LA.norm(A[:,i]-B[:,i])**2)*(A[:,i]-B[:,i])/2 + [LA.norm(Vlim)-LA.norm(V[:,0])]*Ulim
            A[:,i+1]=A[:,i]+V[ :,0]
            B[:,i+1]=B[ :,i]+V[ :,1]
    #Afﬁchage direct des trajectoires
    plot(A[0,:],A[1,:],'r')
    plot(B[0,:],B[1,:],"b")
    show()

