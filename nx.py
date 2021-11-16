#!/bin/python
'''
A simplistic model of a socio-economic network in a group of individuals
TODO: 
Class Agent:
    attributes: age, gender, social credit: public, private, 
    agent behavior models: by gender and age, 
    N_individuals = 50-150
    Mechanisms: agent lifecycle: creation, 4 stages (CGJung), ; agent interaction: social credit transfering\creation, social connections creation, strength

'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

nx.draw(G)
plt.show()
