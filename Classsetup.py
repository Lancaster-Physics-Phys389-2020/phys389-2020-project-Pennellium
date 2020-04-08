import numpy as np
import itertools
import tkinter as tkr

class Particle: #Sets up the Particle class for formatting of the pool balls compenent variables
    def __init__(self, Position=np.array([0,0], dtype=float), Velocity=np.array([0,0], dtype=float), Acceleration=np.array([0,0], dtype=float), Name='Ball', Mass=1.0, Radius = 0.5, Noofcollisions = 0):
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass
        self.radius = Radius
        self.Name = Name
        self.noofcollisions = Noofcollisions

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Radius: {5}, Collisions: {6}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration, self.radius, self.noofcollisions)
 
    def update(self, deltaT): #Function that is called to update the position and velocity of the balls for each timestep
        if np.any(self.velocity) != 0: #Only runs the update function on that ball if any of the velocity components are not zero 
            if self.position[0] - self.radius < 50: #Checks the minimum x axis to see if the ball is interacting with the table
                self.position[0] = 50 + self.radius
                self.velocity[0] = -0.7*self.velocity[0]
                self.noofcollisions += 1 
            if self.position[0] + self.radius > 1550: #Checks the maximum x axis to see if the ball is interacting with the table
                self.position[0] = 1550 - self.radius
                self.velocity[0] = -0.7*self.velocity[0]
                self.noofcollisions += 1
            if self.position[1] - self.radius < 50: #Checks the minimum y axis to see if the ball is interacting with the table
                self.position[1] = 50 + self.radius
                self.velocity[1] = -0.7*self.velocity[1]
                self.noofcollisions += 1
            if self.position[1] + self.radius > 800: #Checks the maximum y axis to see if the ball is interacting with the table
                self.position[1] = 800 - self.radius
                self.velocity[1] = -0.7*self.velocity[1]
                self.noofcollisions += 1
                
            self.position +=  self.velocity*deltaT #Updates the position of the ball in steps of deltaT
            self.velocity +=  np.sign(self.velocity)*(self.acceleration*deltaT- 2*9.81*deltaT) #Updates the velocity of the ball in steps of deltaT
            #The ball is slowed down by the friction of the table for each time step
        else:
            pass
        
        
class TotalBalls: #Class of the group of all the pool balls used for the game.
    TotalBilliards = []
    
    def __init__(self,ListofBalls):
        self.TotalBilliards = ListofBalls #Sets the list of particles used in the functions as the list of balls set in the SimulationUpdate file
        
    def __repr__(self):
        for i in range(len(self.TotalBilliards)):
            return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Radius: {5}'.format(self.TotalBilliards[i].Name,self.TotalBilliards[i].mass,self.TotalBilliards[i].position, self.TotalBilliards[i].velocity,self.TotalBilliards[i].acceleration, self.TotalBilliards[i].radius)
    
    def collisions(self): #Function that handles the interaction of the balls with each other
        collide = False 
        for ball1, ball2 in itertools.combinations(self.TotalBilliards, 2): #Runs through all the different combinations of the two of the balls
            if np.any(ball1.velocity) != 0 or np.any(ball2.velocity) != 0: #Checks to see if either of the balls are moving to see if they can interact
                x = abs(ball1.position[0] - ball2.position[0])
                y = abs(ball1.position[1] - ball2.position[1])
                length = np.hypot(x,y) #Finds the distance between the interacting balls
                if length < ball1.radius + ball2.radius and collide == False: #Checks to see if the Balls are touching and whether they have already interacted in the previous run through.
                    #Finds the resultant velocity of interacting balls due to the elastic collision in 2D space
                    velocity1 = ball1.velocity
                    velocity2 = ball2.velocity
                    ball1.velocity = velocity1 - (2*ball2.mass)/(ball1.mass+ball2.mass) * (np.dot(velocity1-velocity2, ball1.position-ball2.position)/np.linalg.norm(ball1.position-ball2.position)**2) *(ball1.position-ball2.position)
                    ball2.velocity = velocity2 - (2*ball1.mass)/(ball1.mass+ball2.mass) * (np.dot(velocity2-velocity1, ball2.position-ball1.position)/np.linalg.norm(ball1.position-ball2.position)**2) *(ball2.position-ball1.position)
                    collide = True
            else:
                pass
            
            
class Checking: #Class used to determine whether the simulation should continue to run
    TotalBilliards = []
    
    def __init__(self,ListofBalls):
        self.TotalBilliards = ListofBalls
        
    def __repr__(self):
            for i in range(len(self.TotalBilliards)):
                return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Radius: {5}'.format(self.TotalBilliards[i].Name,self.TotalBilliards[i].mass,self.TotalBilliards[i].position, self.TotalBilliards[i].velocity,self.TotalBilliards[i].acceleration, self.TotalBilliards[i].radius)
    
    def velocitydetect(self): # Changes state depending on the state of all of the balls in the simulation
        for ball in self.TotalBilliards:
            if np.all(np.around(np.hypot(ball.velocity[0],ball.velocity[1]),decimals=2)) < 0.001: #Checks whether all of the balls have stopped moving
                return False
            else:
                return True
            
class GUI:
    GUI = tkr.Tk()
    tkr.Label(GUI, text='x-velocity').grid(row=0) 
    tkr.Label(GUI, text='y-velocity').grid(row=1) 
    v1 = tkr.StringVar()
    v2 = tkr.StringVar()
    e1 = tkr.Entry(GUI,textvariable=v1) 
    e2 = tkr.Entry(GUI,textvariable=v2) 
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1)
    GUI.mainloop()
    userx = v1.get()
    usery = v2.get()