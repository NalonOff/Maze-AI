import pygame as pg
import random
import numpy as np

class AI:
    def __init__(self, maze) -> None:
        self.maze = maze

        self.image = pg.transform.scale2x(pg.image.load('assets\\textures\\player.png'))
        self.pos = [32, 0]
        self.trail = []

        self.learningRate = 0.05
        self.trainable = False
        self.eps = 0.99
        self.history = []
        self.valueFunction = {}
        
        self.environment = self.maze.created

        s = 1
        for i in self.environment:
            for _ in range(1, len(i) + 1):
                self.valueFunction[s] = 0.
                s += 1

    def greedy_step(self, state):
        # Greedy step
        actions = [0, 1, 2, 3]  # 0: haut, 1: bas, 2: gauche, 3: droite
        vmin = None
        vi = None
        for i in range(4):
            a = actions[i]
            if not self.maze.testCollision(self.pos, a):
                if a == 0:
                    if vmin is None or vmin < self.environment[state[0], state[1] - 1]:
                        
                        vmin = self.valueFunction[self.pos[0], self.pos[1]]
                        vi = i
                if a == 1:
                    if vmin is None or vmin < self.environment[state[0], state[1] + 1]:
                        
                        vmin = self.valueFunction[self.pos[0], self.pos[1]]
                        vi = i
                if a == 2:
                    if vmin is None or vmin < self.environment[state[0] - 1, state[1]]:
                        
                        vmin = self.valueFunction[self.pos[0], self.pos[1]]
                        vi = i
                if a == 3:
                    if vmin is None or vmin < self.environment[state[0] + 1, state[1]]:
                        
                        vmin = self.valueFunction[self.pos[0], self.pos[1]]
                        vi = i

        # Exploration-exploitation trade-off
        if np.random.rand() < self.eps:
            return np.random.choice(actions)
        else:
            return actions[vi if vi is not None else 0]

    def play(self, state):
        # Play given the @state (int)
        if self.is_human is False:
            # Take random action
            if random.uniform(0, 1) < self.eps:
                action = random.randint(1, 3)
            else: # Or greedy action
                action = self.greedy_step(state)
        else:
            action = int(input("$>"))
        return action

    def add_transition(self, n_tuple):
        # Add one transition to the history: tuple (s, a , r, s')
        self.history.append(n_tuple)
        s, a, r, sp = n_tuple
        self.rewards.append(r)

    def train(self):
        if not self.trainable or self.is_human is True:
            return

        # Update the value function
        for transition in reversed(self.history):
            s, a, r, sp = transition
            if r == 0:
                self.V[s] = self.V[s] + 0.001*(self.V[sp] - self.V[s])
            else:
                self.V[s] = self.V[s] + 0.001*(r - self.V[s])

        self.history = []
        