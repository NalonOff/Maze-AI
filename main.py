import pygame as pg
import sys

from maze import Maze
from ai import AI
from Game import Game


screen = pg.display.set_mode((416, 416))
pg.display.set_caption("Modele d'IA par renforcement")


if __name__ == '__main__':
    clock = pg.time.Clock()
    game = Game()
    ai = AI(game.mazeCreated)
    
    game.play(screen, ai)
