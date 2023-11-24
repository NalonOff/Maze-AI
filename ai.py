import pygame as pg

class AI:
    def __init__(self) -> None:
        self.image = pg.transform.scale2x(pg.image.load('assets\\textures\\player.png'))
        self.pos = [32, 0]
        self.trail = []

        self.learningRate = 0.001