import pygame as pg
import random

class Maze:
    def __init__(self, width, height) -> None:
        self.textures = {
            'wall': pg.transform.scale2x(pg.image.load('assets\\textures\\wall.png')),
            'floor': pg.transform.scale2x(pg.image.load('assets\\textures\\floor.png'))
        }

        self.tileSize = 32
        self.collisions = []
        self.created = self.create(width, height)

    def create(self, width, height):
        maze = [['#' for _ in range(width)] for _ in range(height)]
        stack = [(1, 1)]  # Start the stack with the initial cell

        while stack:
            x, y = stack[-1]

            # Get unvisited neighbors
            neighbors = [(x + dx, y + dy) for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == '#']

            if neighbors:
                nx, ny = random.choice(neighbors)
                maze[(y + ny) // 2][(x + nx) // 2] = ' '  # Carve out the wall between the current cell and the chosen neighbor
                maze[ny][nx] = ' '  # Mark the neighbor cell as visited
                stack.append((nx, ny))  # Move to the neighbor cell
            else:
                stack.pop()  # Backtrack if no unvisited neighbors are found

        # Set entrance and exit
        maze[0][1] = ' '
        maze[height - 1][width - 2] = ' '

        return maze

    def draw(self, screen, maze):
        y = 0
        for layer in maze:
            x = 0
            for tile in layer:
                if tile == '#':
                    screen.blit(self.textures.get('wall'), (x * self.tileSize, y * self.tileSize))
                    self.collisions.append((x * self.tileSize, y * self.tileSize))

                x += 1
            y += 1

    def testCollision(self, pos, direction):
        # 0: haut, 1: bas, 2: gauche, 3: droite
        if direction == 0:
            if (pos[0], pos[1] - self.tileSize) in self.collisions:
                return False   
            else:
                return True
        if direction == 1:
            if (pos[0], pos[1] + self.tileSize) in self.collisions:
                return False   
            else:
                return True
        if direction == 2:
            if (pos[0] - self.tileSize, pos[1]) in self.collisions:
                return False   
            else:
                return True
        if direction == 3:
            if (pos[0] + self.tileSize, pos[1]) in self.collisions:
                return False   
            else:
                return True
