import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
from matplotlib import animation


class Particle:
    def __init__(self, Position=np.array([0,0], dtype=float), Velocity=np.array([0,0], dtype=float), Acceleration=np.array([0,0], dtype=float), Name='Ball', Mass=1.0, Radius = 0.5):
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass
        self.radius = Radius
        self.Name = Name

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Radius: {5}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration, self.radius)

    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
    def momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self, deltaT):
        self.position +=  self.velocity*deltaT
        self.velocity +=  self.acceleration*deltaT

        for i in range(0,2):
            if self.position[i] - self.radius < 0:
                self.position[i] = self.radius
                self.velocity[i] = -self.velocity[i]
            if self.position[i] + self.radius > 10:
                self.position[i] = 10 - self.radius
                self.velocity[i] = -self.velocity[i]

    def overlap(self,other):
        return np.hypot(self.position, other.position) < self.radius + other.radius


billiardball = Particle([5,5],[2,-1],[0,0],'BilliardBall1',2, 0.3)

xpos =[]
ypos = []
t =0

while t in range(100): 
    billiardball.update(0.1)
    xpos.append(billiardball.position[0])
    ypos.append(billiardball.position[1])
    t += 1
else:
    pass


fig = plt.figure()
ax = plt.axes(xlim=(0,10),ylim=(0,10))
line, = ax.plot([],[],lw = 2)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = xpos[i]
    y = ypos[i]
    line.set_data(x,y)
    print(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 100, interval = 10, blit=True)




#plt.plot(xpos, ypos) 
#plt.xlabel('x - position') 
#plt.ylabel('y - position') 

plt.show() 