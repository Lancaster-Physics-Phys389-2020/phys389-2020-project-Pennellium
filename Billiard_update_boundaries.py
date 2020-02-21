import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt 

class Particle:
    def __init__(self, Position=np.array([0,0], dtype=float), Velocity=np.array([0,0], dtype=float), Acceleration=np.array([0,0], dtype=float), Name='Ball', Mass=1.0, Radius = 0.5, Boundaries= np.array([0,10,0,10], dtype=float)):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass
        self.radius = Radius
        self.boundaries = Boundaries

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Radius: {5}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration, self.radius)

    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
    def momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self, deltaT):
        self.position +=  self.velocity*deltaT
        self.velocity +=  self.acceleration*deltaT

        

    def overlap(self,other):
        return np.hypot(self.position, other.position) < self.radius + other.radius

class 


billiardball = Particle([0,0],[2,43],[2,1],'BilliardBall1',2, 0.1)

xpos =[]
ypos = []


while np.linalg.norm(billiardball.velocity) < 1000: 
    billiardball.update(0.1)
    xpos.append(billiardball.position[0])
    ypos.append(billiardball.position[1])
else:
    pass