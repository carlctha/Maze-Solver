import pygame
from collections import deque   
from typing import List, Tuple


def draw_shortest_path(shortest_path, screen, cell_size):
    YELLOW = (255, 255, 0)
    print(shortest_path)
    for i in range(len(shortest_path)):
        if i == 0:
            continue
        row = shortest_path[-i][0]
        col = shortest_path[-i][1]
        pygame.draw.rect(screen, YELLOW, (row * cell_size, col * cell_size, cell_size, cell_size))
        pygame.time.wait(100)
        pygame.display.update()


def draw_bfs(cell, cell_size, screen, color):
    pygame.draw.rect(screen, color, (cell[0] * cell_size, cell[1] * cell_size, cell_size, cell_size))
    pygame.time.wait(50)
    pygame.display.update()

def breadth_first_search(maze_map, starting_node, cell_size, screen, color) -> List:
    start_cell = starting_node
    visited = [start_cell]
    queue = deque([start_cell])
    paths = {}
    shortest_path = []
    goal_cell = (0, 0)

    while len(queue) > 0:
        curr_cell = queue.popleft()
        directions = [
        (curr_cell[0] - 1, curr_cell[1]), (curr_cell[0], curr_cell[1] - 1),
        (curr_cell[0] + 1, curr_cell[1]), (curr_cell[0], curr_cell[1] + 1),
        ]
        for cell in directions:
            if(
                0 <= cell[0] < len(maze_map) and
                0 <= cell[1] < len(maze_map[0]) and
                (maze_map[cell[0]][cell[1]] == 0 or maze_map[cell[0]][cell[1]] == 3) and
                cell not in visited
            ):
                queue.append(cell)
                visited.append(cell)
                paths[cell] = curr_cell
                if cell == goal_cell:
                    continue
                draw_bfs(cell, cell_size, screen, color)
        if curr_cell == goal_cell:
            break

    while goal_cell != start_cell:
        shortest_path.append(goal_cell)
        goal_cell = paths[goal_cell]
    
    shortest_path.append(starting_node)
    
    return shortest_path



def draw_maze(maze_map, screen, cell_size) -> Tuple:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    for row in range(len(maze_map)):
            for col in range(len(maze_map[row])):
                if maze_map[row][col] == 2:
                    color = GREEN
                    pygame.draw.rect(screen, color, (row * cell_size, col * cell_size, cell_size, cell_size))
                    starting_node = (row, col)
                elif maze_map[row][col] == 3:
                    color = RED
                    pygame.draw.rect(screen, color, (row * cell_size, col * cell_size, cell_size, cell_size))
                else:
                    color = WHITE if maze_map[row][col] == 0 else BLACK
                    pygame.draw.rect(screen, color, (row * cell_size, col * cell_size, cell_size, cell_size))

                    pygame.draw.line(screen, YELLOW, (row * cell_size, col * cell_size), ((row + 1) * cell_size, col * cell_size))
                    pygame.draw.line(screen, YELLOW, (row * cell_size, (col + 1) * cell_size), ((row + 1) * cell_size, (col + 1) * cell_size))

                    pygame.draw.line(screen, YELLOW, (row * cell_size, col * cell_size), (row * cell_size, (col + 1) * cell_size))
                    pygame.draw.line(screen, YELLOW, ((row + 1) * cell_size, col * cell_size), ((row + 1) * cell_size, (col + 1) * cell_size))

    return starting_node


def main(maze_map):
    WIDTH, HEIGHT = 500, 500
    CELL_SIZE = WIDTH / len(maze_map)
    LIGHT_BLUE = (173, 216, 230)
    clock = pygame.time.Clock()
    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze")
    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE):
                is_running = False
        
        starting_node = draw_maze(maze_map, screen, CELL_SIZE)
        path = breadth_first_search(maze_map, starting_node, CELL_SIZE, screen, LIGHT_BLUE)
        draw_shortest_path(path, screen, CELL_SIZE)
        pygame.display.flip()

        if path[0] == (0,0):
            pygame.time.wait(10000)
            is_running = False

        clock.tick(30)


maze_map0 = [
        [3, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 2]
]


maze_map1 = [
    [3, 0, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 2]
]


maze_map2 = [
    [3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2],
]


if __name__ == "__main__":
    main(maze_map2)
