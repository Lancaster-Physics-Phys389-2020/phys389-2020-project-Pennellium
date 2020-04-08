from Classsetup import Particle
from Classsetup import TotalBalls

import matplotlib.pyplot as plt
import numpy as np
import copy

Data = np.load("Data1.npy",allow_pickle=True)

Balls = [[] for _ in range(len(Data[0]))] 
Kineticenergy = []
SimulatedLostEnergy = []
TheoreticalLostEnergy = []
Momentum = []
SimulatedLostMomentum = []
TheoreticalLostMomentum = []
Time = []

for line in Data:
    Time.append(line[0][0])
    for i in range(0,len(Balls)):
        Balls[i].append(line[i][1])

def EnergyConservation():
    LostE1 = 0
    LostE2 = 0
    LostE3 = 0
    for k in range(len(Time)):
        KE = 0
        TotalE = 0
        for b in range(len(Balls)):
            KE += (np.linalg.norm(Balls[b][k].velocity)*np.linalg.norm(Balls[b][k].velocity)*Balls[b][k].mass*0.5)
            if k == 0:
                LostE2 += 0 
                LostE1 += 0
                LostE3 += 0
            else:
                if np.around(np.linalg.norm(Balls[b][k].velocity), decimals=0) != 0:
                    LostE1 += ((2*np.linalg.norm(Balls[b][k-1].velocity)*2*9.81*0.01 + (2*9.81)*(2*9.81)*0.01*0.01)*Balls[b][k].mass*0.5)
                LostE2 += ((np.linalg.norm(Balls[b][k-1].velocity)*np.linalg.norm(Balls[b][k-1].velocity)-np.linalg.norm(Balls[b][k].velocity)*np.linalg.norm(Balls[b][k].velocity))*Balls[b][k].mass*0.5)
                LostE3 += (Balls[b][k].noofcollisions - Balls[b][k-1].noofcollisions) *(0.5 *(1-0.7*0.7)*Balls[b][k].mass * np.linalg.norm(Balls[b][k-1].velocity)*np.linalg.norm(Balls[b][k-1].velocity))
        Kineticenergy.append(KE)
        TheoreticalLostEnergy.append(LostE2)
        SimulatedLostEnergy.append(LostE1+LostE3)
    plt.plot(Time, Kineticenergy,'g-',Time, TheoreticalLostEnergy, 'r-', Time, SimulatedLostEnergy, 'b-')
    plt.title('Energy')
    plt.show()
    
def MomentumConservation():
    LostM2 = 0
    LostM3 = 0
    for k in range(len(Time)):
        LostM1 = 0
        M  = 0
        for b in range(len(Balls)):
            M += abs(np.linalg.norm(Balls[b][k].velocity)*Balls[b][k].mass)
            if k == 0:
                LostM2 += 0
                LostM1 += 0
                LostM3 += 0
            else:
                if np.around(np.linalg.norm(Balls[b][k].velocity), decimals=0) != 0:
                    LostM1 += (2*9.81*Time[k]*Balls[b][k].mass)
                LostM2 += ((np.linalg.norm(Balls[b][k-1].velocity)-np.linalg.norm(Balls[b][k].velocity))*Balls[b][k].mass)
                LostM3 += (Balls[b][k].noofcollisions - Balls[b][k-1].noofcollisions)*(0.3*Balls[b][k].mass * np.linalg.norm(Balls[b][k-1].velocity))
        Momentum.append(M)
        TheoreticalLostMomentum.append(LostM2)
        SimulatedLostMomentum.append(LostM1+LostM3)
    plt.plot(Time, Momentum,'g-',Time, TheoreticalLostMomentum, 'r-', Time, SimulatedLostMomentum, 'b-')
    plt.title('Momentum')
    plt.show()

MomentumConservation()
EnergyConservation()