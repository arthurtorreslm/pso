import numpy as np
import random as ran
import matplotlib.pyplot as plt

def func(x, y):
    return -(x*x)-(y*y)
'''class particula:
    posi=[0,0]
    velo=[0,0]
    valor=0
    melhor=[0,0,0]

    def __init__(self, xx, yy):
        self.posi[0] = xx
        self.posi[1] = yy
        self.melhor[0] = xx
        self.melhor[1] = yy
        self.melhor[2] = func(self.posi[0], self.posi[1])
        self.valor=self.melhor[2]
def pso(f, np, prange, ni, inter, ccrange, csrange, wrange, vmax):
    cc=ccrange[0]
    cs=csrange[0]
    w=wrange[0]
    best=[-99999,-99999,-99999]
    #criando particulas
    pontos=[-5, -2.5, 0, 2.5]
    particulas=[]
    for i in range(np+1):
        #z=particula(ran.randrange(-5,5), ran.randrange(-5, 5))
        #g = ran.randrange(-5, 5)
        #h = ran.randrange(-5, 5)
        particulas.insert(i, particula(pontos[i],pontos[i]))
        #particulas[i].valor=f(particulas[i].posi[0], particulas[i].posi[1])
        #print(particulas[i].posi[0], particulas[i].posi[1], particulas[i].valor)
        #particulas[i].valor=particulas[i].melhor[2]
    for i in range(np+1):
        if particulas[i].valor>best[2]:
            best[0]=particulas[i].posi[0]
            best[1] = particulas[i].posi[1]
            best[2] = f(particulas[i].posi[0], particulas[i].posi[1])
            print('novo global:', particulas[i].posi[0], particulas[i].posi[1], particulas[i].valor)
    for a in range(1, ni+1):
        #atualizando posicao e velocidade
        for i in range(np+1):
            particulas[i].posi[0]=particulas[i].posi[0]+particulas[i].velo[0]
            particulas[i].posi[1] = particulas[i].posi[1] + particulas[i].velo[1]
            particulas[i].velo[0]=w*(particulas[i].velo[0])+cc*(particulas[i].melhor[0] - particulas[i].posi[0]) +cs*(best[0]-particulas[i].posi[0])
            if particulas[i].velo[0]>vmax:
                particulas[i].velo[0] = vmax
            particulas[i].velo[1] = w * particulas[i].velo[1] + cc * (particulas[i].melhor[1] - particulas[i].posi[1]) + cs * (best[1] - particulas[i].posi[1])
            if particulas[i].velo[1]>vmax:
                particulas[i].velo[1] = vmax
            #atualizando maximos pessoais e globais
            if particulas[i].valor > best[2]:
                print('nomo melhor global:', particulas[i].posi[0], particulas[i].posi[1], particulas[i].valor)
                best[0] = particulas[i].posi[0]
                best[1] = particulas[i].posi[1]
                best[2] = particulas[i].valor
            if particulas[i].valor >= particulas[i].melhor[2]:
                #print('novo melhor pessoal')
                particulas[i].melhor[0]=particulas[i].posi[0]
                particulas[i].melhor[1] = particulas[i].posi[1]
                particulas[i].melhor[2] = particulas[i].valor
        #atualizando coeficientes
        cc=(ccrange[1]-ccrange[0])*a/ni + ccrange[0]
        cs = (csrange[1] - csrange[0]) * a / ni + csrange[0]
        w=wrange[0]+(wrange[1]-wrange[0])*(ni-a)/ni
    return best
print(pso(func,4, [-5,5], 10,[-5,5], [1.5,02.5], [2,4], [0.9,0.4], 0.01))
#print(ran.randrange(-5,5))'''
class  particula:
    def __init__(self, boundry):
        self.posi=[ran.uniform(boundry[0], boundry[1]), ran.uniform(boundry[0], boundry[1])]
        self.velo=[ran.uniform(-0.01, 0.01), ran.uniform(-0.01, 0.01)]
        self.bestposi=[self.posi[0], self.posi[1]]
        self.bestvalor=-999999
        self.valor=-999999
        self.boun=boundry
    def avaliar(self, f):
        self.valor=f(self.posi[0], self.posi[1])
        if self.valor>self.bestvalor:
            self.bestvalor=self.valor
        return self.valor
    def mover(self, w, cc, cs, melhor, vmax):
        for i in range(2):
            self.posi[i]=self.posi[i]+self.velo[i]
            if self.posi[i]>self.boun[1]:
                self.posi[i]=self.boun[1]
            if self.posi[i]<self.boun[0]:
                self.posi[i]=self.boun[0]
            self.velo[i]=w*(self.velo[i]) + ran.uniform(0, 1)*cc*(self.bestposi[i] - self.posi[i]) + ran.uniform(0, 1)*cs * (melhor[i] - self.posi[i])
            if self.velo[i]>vmax:
                self.velo[i]=vmax
            if self.velo[i]<-vmax:
                self.velo[i]=-vmax
swarm=[]
melhoresplot=[]
ccrange=[0.3,2]
csrange=[0.4,4]
wrange=[0.4,1.5]
vmax=0.75
cc=ccrange[0]
cs=csrange[0]
w=wrange[1]
melhor=-9999999
melhorposi=[-999999, -999999]
n=30
fig=plt.figure()
ax=plt.axes(projection='3d')
for i in range(n):
    swarm.append(particula([-5, 5]))
    swarm[i].avaliar(func)
for a in range(1, 300):
 for i in range(n):
     if swarm[i].valor>melhor:
         melhor=swarm[i].valor
         melhorposi[0]=swarm[i].posi[0]
         melhorposi[1] = swarm[i].posi[1]
 for i in range(n):
     swarm[i].mover(w, cc, cs, melhorposi, vmax)
     swarm[i].avaliar(func)
 cc = (ccrange[1] - ccrange[0]) * a / 20 + ccrange[0]
 cs = (csrange[1] - csrange[0]) * a / 20 + csrange[0]
 w = wrange[0] + (wrange[1] - wrange[0]) * (20 - a) / 20
 ax.scatter(melhorposi[0], melhorposi[1], melhor, 'green')
 #plt.show()
#ax.plot2d(melhoresplot, 'red')
plt.show()
print(melhorposi, melhor)

