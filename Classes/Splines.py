  

import numpy as np
        
class CubicSpline():
    def __init__(self, x, y, FP0 = None, FPN = None, bc_type = "natural"):
        """Interpolação por splines cúbicos.
        Se for natural: bc_type = 'natural'. Se vinculado, bc_type = 'clamped'.
        FP0 = y'(x0) (derivada de y em x0) se bc_type = 'clamped'."""
        
        assert len(x) == len(y), "x e y devem ter o mesmo tamanho!"
        assert bc_type == "natural" or bc_type == "clamped", "bc_type deve ser 'natural' ou 'clamped'!"
        assert (FP0 != None and FPN != None) or bc_type == "natural", "FP0 deve ser fornecido se bc_type = 'clamped'!"
        
        self.x = x
        self.y = y
        self.n = len(x) #tamanho do array (OBS: self.n = 'n' + 1 do livro!)
        
        
        #PASSO 1
        self.h = np.diff(x) #deltas x (h[0] = x[1] - x[0])
                            #h vai de 0 ate n-1
        if bc_type == "natural":
            #ALGORITMO DO SPLINE NATURAL: LIVRO DO BURDEN PAG 149
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
            
            for i in range(self.n-2, -1, -1):
                self.c[i] = self.z[i] - self.mu[i]*self.c[i+1]
                
                self.b[i] = (self.y[i+1] - self.y[i])/self.h[i] - self.h[i]*(self.c[i+1] + 2*self.c[i])/3
                
                self.d[i] = (self.c[i+1] - self.c[i])/(3*self.h[i])

            #PASSO 7
            self.splines = np.vstack((self.y[0:-1], self.b[0:-1], self.c[0:-1], self.d[0:-1])).T
            
        elif bc_type == "clamped":
            #ALGORITMO DO SPLINE CUBICO: LIVRO DO BURDEN PAG 155
            #PASSO 2
            self.alpha = np.zeros(self.n)
            self.alpha[0] = 3*(self.y[1] - self.y[0])/self.h[0] - 3*FP0
            self.alpha[-1] = 3*FPN - 3*(self.y[-1] - self.y[-2])/self.h[-1]
            
            #PASSO 3
            self.alpha[1:-1] = (3/self.h[1:])*(self.y[2:] - self.y[1:-1]) - (3/self.h[:-1])*(self.y[1:-1] - self.y[:-2])
                
            #PASSO 4
            self.l = np.zeros(self.n)
            self.mu = np.zeros(self.n)
            self.z = np.zeros(self.n)
            self.l[0] = 2*self.h[0]
            self.mu[0] = 0.5
            self.z[0] = self.alpha[0]/self.l[0]
            
            # PASSO 5
            for i in range(1, self.n-1):
                self.l[i] = 2*(self.x[i+1] - self.x[i-1]) - self.h[i-1]*self.mu[i-1]
                self.mu[i] = self.h[i]/self.l[i]
                self.z[i] = (self.alpha[i] - self.h[i-1]*self.z[i-1])/self.l[i]

            #PASSO 6
            self.l[-1] = self.h[-1]*(2 - self.mu[-2])
            self.z[-1] = (self.alpha[-1] - self.h[-1]*self.z[-2])/self.l[-1]
            self.c = np.zeros(self.n)
            self.c[-1] = self.z[-1]
            
            #PASSO 7
            self.b = np.zeros(self.n)
            self.d = np.zeros(self.n)
            
            for i in range(self.n-2, -1, -1):
                self.c[i] = self.z[i] - self.mu[i]*self.c[i+1]
                
                self.b[i] = (self.y[i+1] - self.y[i])/self.h[i] - self.h[i]*(self.c[i+1] + 2*self.c[i])/3
                
                self.d[i] = (self.c[i+1] - self.c[i])/(3*self.h[i])

            #PASSO 8
            self.splines = np.vstack((self.y[0:-1], self.b[0:-1], self.c[0:-1], self.d[0:-1])).T
            
        
    def __call__(self, x): #recebe um vetor X para devolver um vetor Y interpolado pelo spline cubico
        y = np.vectorize(self.Substitui)(x)
        return y
        
    def Substitui(self, x):
        if x == self.x[-1]:
            return self.y[-1]
        else:
            idx = np.searchsorted(self.x, x, side="right") - 1 #encontra o indice do intervalo no qual x esta contido
            return self.splines[idx][0] + self.splines[idx][1]*(x-self.x[idx]) + self.splines[idx][2]*(x-self.x[idx])**2 + self.splines[idx][3]*(x-self.x[idx])**3
        
        
        
            
        

        
        
        