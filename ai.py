import pygame as pg

class AI:
    def __init__(self, environment) -> None:
        self.image = pg.transform.scale2x(pg.image.load('assets\\textures\\player.png'))
        self.pos = [32, 0]
        self.trail = []

        self.learningRate = 0.001
        self.trainable = False
        self.eps = 0.99
        self.history = []
        self.valueFunction = {}

        s = 1
        for i in environment:
            for _ in range(1, len(i) + 1):
                self.valueFunction[s] = 0.
                s += 1

    def greedy_step(self, state):
        actions = ['up', 'left', 'down', 'right']
        vmin = None
        vi = None
        for i in range(0, 4):
            a = actions[i]
            
        