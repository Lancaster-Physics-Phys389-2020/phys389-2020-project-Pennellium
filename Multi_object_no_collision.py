import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt 
import tkinter as tkr
import time
import threading
import logging



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
        
        for i in range(len(TotalBalls)):
            for j in range(len(TotalBalls)):
                if i!=j:
                    x = abs(TotalBalls[i].position[0] - TotalBalls[j].position[0])
                    y = abs(TotalBalls[i].position[1] - TotalBalls[j].position[1])
                    length = np.hypot(x,y)
                    if length < 2*self.radius:
                        print(TotalBalls[0].velocity)
                        TotalBalls[i].velocity = -TotalBalls[i].velocity
                        TotalBalls[j].velocity = -TotalBalls[j].velocity
                        
        if self.position[0] - self.radius < 0:
            self.position[0] = self.radius
            self.velocity[0] = -self.velocity[0]
        if self.position[0] + self.radius > 1000:
            self.position[0] = 1000 - self.radius
            self.velocity[0] = -self.velocity[0]
        if self.position[1] - self.radius < 0:
            self.position[1] = self.radius
            self.velocity[1] = -self.velocity[1]
        if self.position[1] + self.radius > 1000:
            self.position[1] = 1000 - self.radius
            self.velocity[1] = -self.velocity[1]
            
        self.position +=  self.velocity*deltaT
        self.velocity +=  self.acceleration*deltaT
        

billiardball1 = Particle([20,20],[10,0],[0,0],'BilliardBall1',2, 20)
billiardball2 = Particle([80,20],[-20,0],[0,0],'BilliardBall2',2, 20)
billiardball3 = Particle([550,600],[-150,140],[0,0],'BilliardBall3',2, 20)

TotalBalls = [billiardball1, billiardball2, billiardball3]

tk = tkr.Tk()
canvas = tkr.Canvas(tk,width=1000,height = 1000)
canvas.grid()

Ball1 = canvas.create_oval(0,0,40,40,fill = "light blue")
Ball2 = canvas.create_oval(60,0,100,40,fill = "red")
Ball3 = canvas.create_oval(530,580,570,620,fill = "green")

Canvasballs = [Ball1, Ball2, Ball3]

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def canvas_update():
    t =0
    xpos = [[billiardball1.position[0],],[billiardball2.position[0],],[billiardball3.position[0],]]
    ypos = [[billiardball1.position[1],],[billiardball2.position[1],],[billiardball3.position[1],]]
    while t in range(10000):
        t += 1
        for v in range(len(TotalBalls)):
            TotalBalls[v].update(0.01)
            xpos[v].append(TotalBalls[v].position[0])
            ypos[v].append(TotalBalls[v].position[1])
            x_dis = xpos[v][t] - xpos[v][t-1]
            y_dis = ypos[v][t] - ypos[v][t-1]
            canvas.move(Canvasballs[v],x_dis,y_dis)
            tk.update()
            time.sleep(0.01)
            pass
    

canvas_thread = threading.Thread(target=canvas_update, name='CanvasThread')
canvas_thread.setDaemon(True)
stop_threads = True
canvas_thread.start()

tk.mainloop()



#plt.plot(xpos, ypos) 
#plt.xlabel('x - position') 
#plt.ylabel('y - position') 

plt.show() 