import pygame as pg
import sys
from maze import Maze

class Game:
    def __init__(self) -> None:
        self.maze = Maze()
        self.initialPos = [16, 0]
        self.mazeCreated = self.maze.create(13, 13)

    def play(self, screen, ai):
        while not self.is_finished(ai.pos):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                # Movement
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_d:
                        if self.maze.testCollision(ai.pos, 'right'):
                            ai.pos[0] += self.maze.tileSize
                    if event.key == pg.K_a:
                        if self.maze.testCollision(ai.pos, 'left'):
                            ai.pos[0] -= self.maze.tileSize
                    if event.key == pg.K_w:
                        if self.maze.testCollision(ai.pos, 'up'):
                            ai.pos[1] -= self.maze.tileSize
                    if event.key == pg.K_s:
                        if self.maze.testCollision(ai.pos, 'down'):
                            ai.pos[1] += self.maze.tileSize
                    ai.trail.append(pg.rect.Rect(ai.pos, (self.maze.tileSize, self.maze.tileSize)))

            self.display(screen, ai)

            pg.display.flip()
            screen.fill((0,0,0))

            #clock.tick(60)

    def is_finished(self, pos):
        if pos == [608, 640]:
            return True
        return False
    
    def reset(self):
        pass

    def display(self, screen, ai):
        for i in range(len(ai.trail)):
            pg.draw.rect(screen, (96,96,96), ai.trail[i])

        self.maze.draw(screen, self.mazeCreated)
        screen.blit(ai.image, ai.pos)
        