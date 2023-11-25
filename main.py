import pygame
from collections import deque   
from typing import List, Tuple
import maps


class MazeSolver:
    def __init__(self, maze_map):
        self.WIDTH = 500
        self.HEIGHT = 500
        self.maze_map = maze_map
        self.CELL_SIZE = self.WIDTH / len(self.maze_map)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.LIGHT_BLUE = (173, 216, 230)
        self.is_running = True

    def draw_shortest_path(self, shortest_path, screen):
        for i in range(len(shortest_path)):
            if i == 0:
                continue
            row = shortest_path[-i][0]
            col = shortest_path[-i][1]
            pygame.draw.rect(screen, self.YELLOW, (row * self.CELL_SIZE, col * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
            pygame.time.wait(10)
            pygame.display.update()

    def draw_bfs(self, cell, screen):
        pygame.draw.rect(screen, self.LIGHT_BLUE, (cell[0] * self.CELL_SIZE, cell[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        pygame.time.wait(5)
        pygame.display.update()

    def breadth_first_search(self, screen) -> List:
        start_cell = (len(self.maze_map) - 1, len(self.maze_map[0]) - 1)
        visited = [start_cell]
        queue = deque([start_cell])
        paths = {}
        shortest_path = []
        goal_cell = (0, 0)

        while len(queue) > 0:
            curr_cell = queue.popleft()
            neighbours = [
            (curr_cell[0] - 1, curr_cell[1]), (curr_cell[0], curr_cell[1] - 1),
            (curr_cell[0] + 1, curr_cell[1]), (curr_cell[0], curr_cell[1] + 1),
            ]
            for cell in neighbours:
                if(
                    0 <= cell[0] < len(self.maze_map) and
                    0 <= cell[1] < len(self.maze_map[0]) and
                    (self.maze_map[cell[1]][cell[0]] == 0 or self.maze_map[cell[1]][cell[0]] == 3) and
                    cell not in visited
                ):
                    queue.append(cell)
                    visited.append(cell)
                    paths[cell] = curr_cell
                    if cell == goal_cell:
                        continue
                    self.draw_bfs(cell, screen)
            if curr_cell == goal_cell:
                break

        while goal_cell != start_cell:
            shortest_path.append(goal_cell)
            goal_cell = paths[goal_cell]
        
        shortest_path.append(start_cell)
        
        return shortest_path

    def draw_maze(self, screen) -> Tuple:
        for row in range(len(self.maze_map)):
                for col in range(len(self.maze_map[row])):
                    if self.maze_map[col][row] == 2:
                        color = self.GREEN
                        pygame.draw.rect(screen, color, (row * self.CELL_SIZE, col * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                    elif self.maze_map[row][col] == 3:
                        color = self.RED
                        pygame.draw.rect(screen, color, (row * self.CELL_SIZE, col * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                    else:
                        color = self.WHITE if self.maze_map[col][row] == 0 else self.BLACK
                        pygame.draw.rect(screen, color, (row * self.CELL_SIZE, col * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                        
                        color = self.YELLOW
                        pygame.draw.line(screen, color, (row * self.CELL_SIZE, col * self.CELL_SIZE), ((row + 1) * self.CELL_SIZE, col * self.CELL_SIZE))
                        pygame.draw.line(screen, color, (row * self.CELL_SIZE, (col + 1) * self.CELL_SIZE), ((row + 1) * self.CELL_SIZE, (col + 1) * self.CELL_SIZE))

                        pygame.draw.line(screen, color, (row * self.CELL_SIZE, col * self.CELL_SIZE), (row * self.CELL_SIZE, (col + 1) * self.CELL_SIZE))
                        pygame.draw.line(screen, color, ((row + 1) * self.CELL_SIZE, col * self.CELL_SIZE), ((row + 1) * self.CELL_SIZE, (col + 1) * self.CELL_SIZE))

    def main(self):
        clock = pygame.time.Clock()
        pygame.init() 
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Maze")

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE):
                    self.is_running = False
            
            self.draw_maze(screen)
            path = self.breadth_first_search(screen)
            self.draw_shortest_path(path, screen)
            pygame.display.flip()

            if path[0] == (0,0):
                pygame.time.wait(4000)
                self.is_running = False

            clock.tick(30)


if __name__ == "__main__":
    solver = MazeSolver(maps.maze_map2)
    solver.main()
