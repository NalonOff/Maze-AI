import pygame as pg
import sys

from maze import Maze
from ai import AI

clock = pg.time.Clock()
maze = Maze()
ai = AI()

screen = pg.display.set_mode((672, 750))
pg.display.set_caption("Modele d'IA par renforcement")

created = maze.create(21, 21)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                if maze.testCollision(ai.pos, 'right'):
                    ai.pos[0] += maze.tileSize
            if event.key == pg.K_a:
                if maze.testCollision(ai.pos, 'left'):
                    ai.pos[0] -= maze.tileSize
            if event.key == pg.K_w:
                if maze.testCollision(ai.pos, 'up'):
                    ai.pos[1] -= maze.tileSize
            if event.key == pg.K_s:
                if maze.testCollision(ai.pos, 'down'):
                    ai.pos[1] += maze.tileSize

    if ai.pos == [608, 640]:
        pg.quit()
        sys.exit()
    
    maze.draw(screen, created)
    screen.blit(ai.image, ai.pos)

    pg.display.flip()
    screen.fill((0,0,0))

    clock.tick(60)
