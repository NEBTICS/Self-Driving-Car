#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:22:47 2020

@author: smithbarbose
"""
'libraries'
import numpy as np
import random
from random import Random,randint
import matplotlib.pyplot as plt
import time 
import cv2
'importing kivy pakages'
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color,Ellipse,Line
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector 
from kivy.clock import Clock
'start of code'
'importing the brain'
from AI_Brain import Dqn
#mouse click
Config.set('input','mouse','mouse,multitouch_on_demand')
#recap 
last_x=0
last_y=0
n_points=0
lengts=0
#DQN
brain=Dqn(3,3,0.9)
action2rotation=[0,20,-20]
last_reward=0
score=[]
'initialing map'
first_update=True
def init():
    global sand()
    global goal_x
    global goal_y
    global first_update(snad=np.zeros((longueur,largeur)))
    goal_x=20
    goal_y=largeur-10
    first_update=False
#initalizing the distance
last_distance=0
'building the car'
class Car(Widget):
    angle=NumericProperty(0)
    rotaion = NumericProperty(0)
    velocity_x=NumericProperty(0)
    velocity_y=NumericProperty(0)
    velocity=ReferenceListProperty(velocity_x, velocity_y)
    'sensors1'
    sensor1_x=NumericProperty(0)
    sensor1_y=NumericProperty(0)
    sensor1=ReferenceListProperty(sensor1_x, sensor1_y)
    'sensors2'
    sensor2_x=NumericProperty(0)
    sensor2_y=NumericProperty(0)
    sensor2=ReferenceListProperty(sensor2_x, sensor2_y)    
    'sensors3'
    sensor3_x=NumericProperty(0)
    sensor3_y=NumericProperty(0)
    sensor3=ReferenceListProperty(sensor3_x, sensor3_y)
    signal1=NumericProperty(0)
    signal2=NumericProperty(0)
    signal3=NumericProperty(0)
    def move(self,rotation):
        self.pos=Vector(*self.velocity)+self.pos
        self.rotation=rotation
        self.angle=self.angle+self.rotation
        self.sensor1=Vector(30,0).rotation(self.angle)+self.pos
        self.sensor2=Vector(30,0).rotation((self.angle+30)%360) + self.pos
        self.sensor3=Vector(30,0).rotation((self.angle-30)%360) + self.pos
        self.signal1=init(np.sum(sand[init(self.sensor1_x)-10:int(self.sensor1_x)+10,init(sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2=init(np.sum(sand[init(self.sensor2_x)-10:int(self.sensor2_x)+10,init(sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3=init(np.sum(sand[init(self.sensor3_x)-10:int(self.sensor3_x)+10,init(sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            self.signal1=1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2=1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3=1.
class Ball1(Widget):
    pass
class Ball2(Widget):
    pass
class Ball3(Widget):
    pass
'creating the class game'
class Game(Widget):
    car=ObjectProperty(None)
    Ball1=ObjectProperty(None)
    Ball2=ObjectProperty(None)
    Ball3=ObjectProperty(None)
    def serve_car(self):
        self.car.center=self.center
        self.car.velocity = Vector(6,0)
    def update(self,dt):
        global brain
        global last_reward
        global score
        global last_distance
        global goal_x
        global goal_y
        global longueur
        global largeur
        
         
            
                
        
        
        
        
        
        
        
        



    