import numpy as np
import matplotlib.pyplot as plt

def gauss(A,b):
    Ab = np.concatenate((A,b),axis=1)
    nl,nc = A.shape
    
    for j in range(nl-1):
        pivo = Ab[j,j]  
        for i in range(j+1,nc):
            f = Ab[i,j]/pivo
            Ab[i,:] = Ab[i,:] - f*Ab[j,:]
            
    return Ab[:,:-1], Ab[:,-1:], retroativa(Ab[:,:-1],Ab[:,-1:],nl,nc)


def retroativa(A,b,nl,nc):
    x = np.array([0] * nl)

    for i in range(nl-1,-1,-1):
        soma = 0
        for j in range(i+1,nc):
            soma = soma + x[j] * A[i,j]
        x[i] = (b[i] - soma )/A[i,i]
    return x.reshape(nl,1)

def show_result(A,b):
    
    A, b, x = gauss(A,b)
    
    plt.figure(1)
    plt.imshow(A,cmap="Reds")
    plt.title("Matriz A")
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            plt.text(j,i,A[i,j],ha="center",color="black")
            
    plt.figure(2)
    plt.imshow(b,cmap="Reds")
    plt.title("matriz B")
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            plt.text(j,i,b[i,j],ha="center",color="black")
            
    plt.figure(3)
    plt.imshow(x,cmap="Greens")
    plt.title("[X] encontrados")
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            plt.text(j,i,x[i,j],ha="center",color="black")
    
    plt.show()

if __name__ == "__main__":
    A = np.matrix([[1, 2, 3], [1, 3, 4],[4,2,10]])
    b = np.matrix([[10], [5],[3]])
    show_result(A,b)
