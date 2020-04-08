import numpy as np
import copy
import tkinter as tkr
from tkinter import messagebox
import multiprocessing
import logging
from Classsetup import Particle
from Classsetup import TotalBalls
from Classsetup import Checking
from Classsetup import GUI
import time
import sys

GUI()

cueball = Particle([1175,425],[GUI.userx,GUI.usery],[0,0],'Cueball',2, 15)
billiardball1 = Particle([425,457],[0,0],[0,0],'BilliardBall1',2, 16)
billiardball2 = Particle([425,393],[0,0],[0,0],'BilliardBall2',2, 16)
billiardball3 = Particle([457,409],[0,0],[0,0],'BilliardBall3',2, 16)
billiardball4 = Particle([457,441],[0,0],[0,0],'BilliardBall4',2, 16)
billiardball5 = Particle([489,425],[0,0],[0,0],'BilliardBall5',2, 16)
billiardball6 = Particle([393,473],[0,0],[0,0],'BilliardBall6',2, 16)
billiardball7 = Particle([393,441],[0,0],[0,0],'BilliardBall7',2, 16)
billiardball8 = Particle([393,409],[0,0],[0,0],'BilliardBall8',2, 16)
billiardball9 = Particle([393,377],[0,0],[0,0],'BilliardBall9',2, 16)
blackball= Particle([425,425],[0,0],[0,0],'Blackball',2, 16)

Listofballs = [cueball, billiardball1, billiardball2, billiardball3, billiardball4, billiardball5, billiardball6, billiardball7, billiardball8, billiardball9, blackball]

tk = tkr.Tk()
canvas = tkr.Canvas(tk,width=1600,height = 850)
canvas.create_rectangle(0,0,1600,850, fill = 'dark green')
canvas.create_rectangle(50,50,1550,800, fill = 'green')
canvas.create_oval(10,10,90,90,fill = 'blue')
canvas.create_oval(1510,10,1590,90,fill = 'blue')
canvas.create_oval(10,760,90,840,fill = 'blue')
canvas.create_oval(1510,760,1590,840,fill = 'blue')
canvas.create_oval(760,10,840,90,fill = 'blue')
canvas.create_oval(760,760,840,840,fill = 'blue')
canvas.grid()
Canvasballs = []

for n in range(len(Listofballs)):
    if n == 0:
        x0 = Listofballs[0].position[0] - Listofballs[0].radius
        x1 = Listofballs[0].position[0] + Listofballs[0].radius
        y0 = Listofballs[0].position[1] - Listofballs[0].radius
        y1 = Listofballs[0].position[1] + Listofballs[0].radius
        Ball = canvas.create_oval(x0,y0,x1,y1,fill = 'white')
        Canvasballs.append(Ball)
    if n == 10:
        x0 = Listofballs[n].position[0] - Listofballs[n].radius
        x1 = Listofballs[n].position[0] + Listofballs[n].radius
        y0 = Listofballs[n].position[1] - Listofballs[n].radius
        y1 = Listofballs[n].position[1] + Listofballs[n].radius
        Ball = canvas.create_oval(x0,y0,x1,y1,fill = 'gray1')
        Canvasballs.append(Ball)
    if n%2 == 0 and n!=0 and n!= 10:
        x0 = Listofballs[n].position[0] - Listofballs[n].radius
        x1 = Listofballs[n].position[0] + Listofballs[n].radius
        y0 = Listofballs[n].position[1] - Listofballs[n].radius
        y1 = Listofballs[n].position[1] + Listofballs[n].radius
        Ball = canvas.create_oval(x0,y0,x1,y1,fill = 'yellow')
        Canvasballs.append(Ball)
    if n%2 == 1 and n!=0 and n!= 10:
        x0 = Listofballs[n].position[0] - Listofballs[n].radius
        x1 = Listofballs[n].position[0] + Listofballs[n].radius
        y0 = Listofballs[n].position[1] - Listofballs[n].radius
        y1 = Listofballs[n].position[1] + Listofballs[n].radius
        Ball = canvas.create_oval(x0,y0,x1,y1,fill = 'red')
        Canvasballs.append(Ball)

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

simulation = TotalBalls(Listofballs)
VelocityCheck = Checking(Listofballs)
Data = []
Closedvar = False

def canvas_update():
    global Closedvar
    time_step = 0.0001
    e = 0
    Initialstate = [[0] for i in range(len(Listofballs))]
    for x in range(len(Listofballs)):
                Initialstate[x].append(copy.deepcopy(Listofballs[x]))
    Data.append(Initialstate)
    xpos = [[Listofballs[i].position[0]] for i in range(len(Listofballs))]
    ypos = [[Listofballs[i].position[1]] for i in range(len(Listofballs))]
    Run = True
    while Run == True:
            simulation.collisions()
            e +=1
            for v in range(len(Listofballs)):
                Listofballs[v].update(time_step)
            if e%100 == 0:
                item = [[e*time_step] for i in range(len(Listofballs))]
                for t in range(len(Listofballs)):
                    item[t].append(copy.deepcopy(Listofballs[t]))
                    xpos[t].append(Listofballs[t].position[0])
                    ypos[t].append(Listofballs[t].position[1])
                    x_dis = xpos[t][-1] - xpos[t][-2]
                    y_dis = ypos[t][-1] - ypos[t][-2]                    
                    if Closedvar == True:
                        Run = False
                        break
                    else: 
                        canvas.move(Canvasballs[t],x_dis,y_dis)
                        tk.update()
                        if VelocityCheck.velocitydetect() == False:
                            Data.append(item)
                            Run = False
                            tk.destroy()
                            np.save("Data1", Data)
                            break
                        else:
                            Data.append(item)
                            Run = True
    else:
        print('Finished')
        sys.exit()
        
        
def closing():
     global Closedvar
     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
         np.save("Data1", Data)
         messagebox.showinfo('','Data Saved')
         Closedvar = True
         time.sleep(1)
         tk.destroy()
         
    
tk.protocol("WM_DELETE_WINDOW", closing)
    
canvas_thread = multiprocessing.Process(target=canvas_update())
canvas_thread.start()