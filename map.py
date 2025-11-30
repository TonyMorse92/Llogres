import pygame
import sys
import time


black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
rows = 400
columns = 400
cell_size = 40
state = [0,0,0,0,0,1,0,0,0,0] # 1 black
gen_num = 0


def get_input():
	screen_width = int(input("Input the size of your screen(multiple of 10): "))
	screen_height = screen_width
	cell_size = screen_width/10
	return screen_width,screen_height,cell_size

def main():
	global screen, clock, gen_num, state
	pygame.init()
	screen = pygame.display.set_mode((rows,columns))
	clock = pygame.time.Clock()
	screen.fill(white)

	_ = 0
	#gen_num = 0
	draw_grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		pygame.display.update()

		time.sleep(1)
		_ += 1

def draw_grid():
	for col in range(columns):
		for row in range(rows):
			grid = pygame.Rect(row*cell_size, col*cell_size,cell_size,cell_size)


pygame.draw.rect(screen, grey, grid, 1)


main()
