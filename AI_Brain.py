#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:35:08 2020

@author: smithbarbose
"""
import numpy as np
import random
import os
import torch.nn as nn
import torch.nn.functional as functional
import torch.optim as optimizer
import torch.autograd as autograd
from torch.autograd import Variable 

class Network(nn.Module):
    def__init__(self,input_size,nb_action):
        super(Network, self).__init__()
        self.input_size=input_size
        self.nn_action=nn_action
        self.fcl = nn.Linear(input_size, 30)
        self.fc2 = nn.Linear(30,nb_action)
    def forward(self,state):
        x=functional.relu(self.fc1(state))
        q_values=self.fc2(x)
        return q_values
    
    
