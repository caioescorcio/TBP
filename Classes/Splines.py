import pandas as pd   
import numpy as np
import pandas as pd   
import numpy as np
        
class CubicSpline():
    def __init__(self, x, y):
        assert len(x) == len(y), "x e y devem ter o mesmo tamanho!"
        self.x = x
        self.y = y
        self.n = len(x) #tamanho do array
        
        #ALGORITMO DO SPLINE NATURAL: LIVRO DO BURDEN PAG 149
        #PASSO 1
        self.h = np.diff(x) #deltas x (h[0] = x[1] - x[0])
        
        #PASSO 2
        self.alpha = np.zeros(self.n)
        self.alpha[1:-1] = (3/self.h[1:])*(self.y[2:] - self.y[1:-1]) - (3/self.h[:-1])*(self.y[1:-1] - self.y[:-2])
            
        #PASSO 3
        self.l = np.zeros(self.n)
        self.mu = np.zeros(self.n)
        self.z = np.zeros(self.n)
        self.l[0] = 1
        self.mu[0] = 0
        self.z[0] = 0
        
        # PASSO 4
        for i in range(1, self.n-1):
            self.l[i] = 2*(self.x[i+1] - self.x[i-1]) - self.h[i-1]*self.mu[i-1]
            self.mu[i] = self.h[i]/self.l[i]
            self.z[i] = (self.alpha[i] - self.h[i-1]*self.z[i-1])/self.l[i]

        #PASSO 5
        self.l[-1] = 1
        self.z[-1] = 0
        self.c = np.zeros(self.n)
        
        #PASSO 6
        self.b = np.zeros(self.n)
        self.d = np.zeros(self.n)
        
        self.c[self.n-2::-1] = self.z[self.n-2::-1] - self.mu[self.n-2::-1]*self.c[self.n-1::-1]
        self.b[self.n-2::-1] = (self.y[self.n-1:self.n-1:-1] - self.y[self.n-2::-1])/self.h[self.n-2::-1] - self.h[self.n-2::-1]*(self.c[self.n-1::-1] + 2*self.c[self.n-2::-1])/3
        self.d[self.n-2::-1] = (self.c[self.n-1::-1] - self.c[self.n-2::-1])/(3*self.h[self.n-2::-1])

        #PASSO 7
        self.splines = np.vstack((self.y, self.b, self.c, self.d)).T
        
    def __call__(self, x): #recebe um vetor X para devolver um vetor Y interpolado pelo spline cubico
        y = x.apply(self.Substitui)
        return y
        
    def Substitui(self, x):
        idx = np.searchsorted(self.x, x, side="right") - 1 #encontra o indice do intervalo no qual x esta contido
        return self.splines[idx][0] + self.splines[idx][1]*(x-self.x[idx]) + self.splines[idx][2]*(x-self.x[idx])**2 + self.splines[idx][3]*(x-self.x[idx])**3
        
        
        
            
        

        
        
        