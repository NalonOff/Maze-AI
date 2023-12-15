import pygame as pg
import sys

from maze import Maze
from ai import AI
from Game import Game


screen = pg.display.set_mode((416, 416))
pg.display.set_caption("Modele d'IA par renforcement")


if __name__ == '__main__':
    clock = pg.time.Clock()
    maze = Maze(13, 13)
    game = Game(maze)
    ai = AI(maze)

    for i in range(0, 10000):
        if i % 10 == 0:
            ai.eps = max(ai.eps*0.996, 0.05)
        game.play(screen, ai)

    