import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt 

class Particle:
    """
    Class to model a massive particle in a gravitational field. 
    It will make use of numpy arrays to store the position velocity etc. 
    Working directly from past exercises... 

    mass in kg 
    position and velocity in m 
    """
    def __init__(self, Position=np.array([0,0], dtype=float), Velocity=np.array([0,0], dtype=float), Acceleration=np.array([0,0], dtype=float), Name='Ball', Mass=1.0):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
    def momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self, deltaT):
        self.position +=  self.velocity*deltaT
        self.velocity +=  self.acceleration*deltaT

billiardball = Particle([0,0],[2,43],[2,1],'BilliardBall1',2)

xpos =[]
ypos = []


while np.linalg.norm(billiardball.velocity) < 1000: 
    billiardball.update(0.1)
    xpos.append(billiardball.position[0])
    ypos.append(billiardball.position[1])
else:
    pass


plt.plot(xpos, ypos) 
plt.xlabel('x - position') 
plt.ylabel('y - position') 

plt.show() 
