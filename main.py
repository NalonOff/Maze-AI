import pygame as pg
import sys

from maze import Maze
from ai import AI

clock = pg.time.Clock()
maze = Maze()


screen = pg.display.set_mode((672, 750))
pg.display.set_caption("Modele d'IA par renforcement")

created = maze.create(13, 13)
ai = AI(created)
print(ai.valueFunction)
while maze.is_finished(ai.pos) is False:
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
            ai.trail.append(pg.rect.Rect(ai.pos, (maze.tileSize, maze.tileSize)))

    for i in range(len(ai.trail)):
        pg.draw.rect(screen, (96,96,96), ai.trail[i])

    maze.draw(screen, created)
    screen.blit(ai.image, ai.pos)

    pg.display.flip()
    screen.fill((0,0,0))

    clock.tick(60)
