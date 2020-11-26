import pygame
import Solución as sol
pygame.font.init()
screen = pygame.display.set_mode((502, 502))
dif = 500 / 9
sudoku=[[0, 0, 4, 0, 0, 3, 0, 0, 0],
        [8, 0, 0, 0, 9, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 1],
        [0, 1, 3, 5, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 6, 0, 1, 0],
        [0, 6, 0, 7, 2, 0, 0, 5, 9],
        [0, 0, 0, 3, 0, 0, 1, 0, 0],
        [0, 7, 0, 0, 0, 9, 2, 0, 0]]
font = pygame.font.SysFont("comicsans", 50, italic=True)
def dibu():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                text1 = font.render(str(sudoku[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))

    for i in range(10):
        if i % 3 == 0:
            gr = 5
        else:
            gr = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), gr)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), gr)

run = True
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                sudoku=sol.solu(sudoku)
    dibu()
    pygame.display.update()
pygame.quit()	 

