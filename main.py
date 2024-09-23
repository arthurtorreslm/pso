import random as ran
import numpy as np

class  particula:
    def __init__(self, boundry):
        self.posi=[]
        self.velo=[]
        for i in range(len(boundry)):
            self.posi.append(ran.uniform(boundry[i][0], boundry[i][1]))
            self.velo.append(ran.uniform(-0.1, 0.1))
        self.bestposi=self.posi
        self.bestvalor=float("-inf")
        self.valor=float("-inf")
        self.boun=boundry
    def avaliar(self, f):
        self.valor=f(self.posi)
        if self.valor>self.bestvalor:
            self.bestvalor=self.valor
        return self.valor
    def mover(self, cc, cs, w, vmax, melhor):
        for i in range(len(self.posi)):
            self.posi[i]=self.posi[i]+self.velo[i]
            if self.posi[i]>self.boun[i,1]:
                self.posi[i]=self.boun[i,1]
            if self.posi[i]<self.boun[i,0]:
                self.posi[i]=self.boun[i,0]
            self.velo[i]=w*(self.velo[i]) + ran.uniform(0, 1)*cc*(self.bestposi[i] - self.posi[i]) + ran.uniform(0, 1)*cs * (melhor[i] - self.posi[i])
            if self.velo[i]>vmax:
                self.velo[i]=vmax
            if self.velo[i]<-vmax:
                self.velo[i]=-vmax
class pso:
    swarm= []
    dim=0
    seed=0
    space=[]
    melhor=float("-inf")
    melhorposi=[]
    ccrange=[0.4, 0.9]
    csrange=[0.9, 0.4]
    wrange=[0.7, 0.1]
    vmax=2.0
    def __init__(self, seed):
        self.seed=seed
        ran.seed(self.seed)
    def makeswarm(self, dim, n, space):
        self.dim=dim
        self.swarm=[]
        self.melhor = float("-inf")
        self.melhorposi = []
        for i in range(n):
            self.swarm.append(particula(space))
        for i in range(dim):
            self.melhorposi.append(float(-np.inf))
    def setcc(self, cc):
        self.ccrange=cc
    def setcs(self, cs):
        self.csrange=cs
    def setw(self, w):
        self.wrange=w
    def setspace(self, s):
        self.space=s
    def setvmax(self, v):
        self.vmax=v
    def atualizarpesos(self, i, n):
        cc = (self.ccrange[1] - self.ccrange[0]) * i / n + self.ccrange[0]
        cs = (self.csrange[1] - self.csrange[0]) * i / n + self.csrange[0]
        w = self.wrange[0] + (self.wrange[1] - self.wrange[0]) * (n - i) / n
        return cc, cs, w
    def run(self, f, n):
        cc=self.ccrange[0]
        cs=self.csrange[0]
        w=self.wrange[0]
        for i in range(n):
            for j in range(len(self. swarm)):
                self.swarm[j].avaliar(f)
                if(self.swarm[j].valor>self.melhor):
                    self.melhor=self.swarm[j].valor
                    self.melhorposi=self.swarm[j].posi
                self.swarm[j].mover(cc, cs, w, self.vmax, self.melhorposi)
            cc,cs,w=self.atualizarpesos(i, n)
        return self.melhor, self.melhorposi
#use funcao com argumento array ou similar.
