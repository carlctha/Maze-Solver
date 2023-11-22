import pygame


def create_maze(maze_map, screen):
    CELL_SIZE = 100
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    for row in range(len(maze_map)):
            for col in range(len(maze_map[row])):
                color = WHITE if maze_map[row][col] == 0 else BLACK
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                pygame.draw.line(screen, YELLOW, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, row * CELL_SIZE))
                pygame.draw.line(screen, YELLOW, (col * CELL_SIZE, (row + 1) * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE))

                pygame.draw.line(screen, YELLOW, (col * CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE, (row + 1) * CELL_SIZE))
                pygame.draw.line(screen, YELLOW, ((col + 1) * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE))


def main(maze_map):
    WIDTH, HEIGHT = 700, 700

    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze")
    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE):
                is_running = False
        
        create_maze(maze_map, screen)

        pygame.display.flip()


maze_map = [
        [0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0]
]


if __name__ == "__main__":
    main(maze_map)
