import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random

WIDTH = 1020  
HEIGHT = 640
TITLE = "Conway's Game of Life"
TILESIZE = 10
FPS = 2
BACKGROUND = [20, 20, 20]
GRID = [0, 0, 0]
r = 100
g = 100
b = 100
ORGANISM = [r, g, b]
populated = []
unpopulated = []
location = []

i = 1

pygame.init()

RESOLUTION = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(TITLE)

icon = pygame.image.load('../../icon.png')
pygame.display.set_icon(icon)

global start
global running
global iteration
global simulation
global remember
global setup
global remove
global dupl
global screenshot

start = False
running = True
iteration = 0
simulation = True
remember = 2
setup = False
remove = False
dupl = False
screenshot = False

font = pygame.font.Font('../../ProximaNovaThin.otf', 56)
font2 = pygame.font.Font('../../ProximaNovaThin.otf', 28)
font3 = pygame.font.Font('../../ProximaNovaThin.otf', 22)
font4 = pygame.font.Font('../../ProximaNovaThin.otf', 22)
font4.set_bold(True)
text = font.render('Game of Life', True, [255, 255, 255])
text1 = font2.render('[Press Enter to Continue]', True, [180, 180, 180])
text2 = font2.render('Life: ', True, [180, 180, 180])
text3 = font2.render(str(len(populated)), True, [255, 255, 255])
text4 = font2.render('Iteration: ', True, [180, 180, 180])
text5 = font2.render(str(iteration), True, [255, 255, 255])
text6 = font4.render('   Controls:', True, [50, 130, 50])
text7 = font3.render('Enter   -   Pause/Start', True, [80, 160, 80])
text8 = font3.render('R   -   Reset', True, [80, 160, 80])
text9 = font3.render('Esc   -   Quit', True, [80, 160, 80])
text10 = font3.render('Left Click   -   Generate', True, [80, 160, 80])
text11 = font3.render('Up/Down   -   Change FPS', True, [80, 160, 80])
text12 = font2.render('FPS: ', True, [180, 180, 180])
text13 = font2.render(str(FPS), True, [255, 255, 255])
text14 = font2.render(str(remember), True, [255, 255, 255])
text15 = font3.render('Right Click   -   Remove', True, [80, 160, 80])
text16 = font3.render('S   -   Screenshot Mode', True, [80, 160, 80])

textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 2 - 40)

text1Rect = text1.get_rect()
text1Rect.center = (WIDTH // 2, HEIGHT // 2 + 5)

text2Rect = text3.get_rect()
text2Rect.center = (40, 40)

text3Rect = text3.get_rect()
text3Rect.center = (96, 40)

text4Rect = text4.get_rect()
text4Rect.center = (87, 80)

text5Rect = text5.get_rect()
text5Rect.center = (150, 80)

text6Rect = text6.get_rect()
text6Rect.center = (56, 390)

text7Rect = text7.get_rect()
text7Rect.center = (116, 430)

text8Rect = text8.get_rect()
text8Rect.center = (71, 460)

text9Rect = text9.get_rect()
text9Rect.center = (73, 490)

text10Rect = text10.get_rect()
text10Rect.center = (127, 520)

text15Rect = text15.get_rect()
text15Rect.center = (127, 550)

text16Rect = text16.get_rect()
text16Rect.center = (130, 610)

text11Rect = text11.get_rect()
text11Rect.center = (141, 580)

text12Rect = text12.get_rect()
text12Rect.center = (63, 120)

text13Rect = text13.get_rect()
text13Rect.center = (101, 120)

text14Rect = text14.get_rect()
text14Rect.center = (101, 120)

clock = pygame.time.Clock()


def event():

	global running
	global start
	global setup
	global populated
	global simulation
	global iteration
	global FPS
	global remember
	global remove
	global screenshot

	for event in pygame.event.get():

		if pygame.mouse.get_pressed()[0]:
			try:
				remove = False
				coordinates = pygame.mouse.get_pos()
				life(coordinates[0], coordinates[1])
			except AttributeError:
				pass
		if pygame.mouse.get_pressed()[2]:
			try:
				remove = True
				coordinates = pygame.mouse.get_pos()
				life(coordinates[0], coordinates[1])
			except AttributeError:
				pass
				
		if event.type == pygame.QUIT:
			running = False
			setup = False
			start = False
			screenshot = False
			simulation = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
				setup = False
				start = False
				screenshot = False
				simulation = False

			if setup == True:
				if event.key == pygame.K_DOWN:
					if remember > 1:
						remember = remember - 1

				if event.key == pygame.K_UP:
					if remember < 20:
						remember = remember + 1

			if event.key == pygame.K_RETURN:
				if setup == True:
					setup = False
					start = True
				elif start == True:
					setup = True
					start = False
				elif running == True:
					running = False
					setup = True
			
			if event.key == pygame.K_r:
				if setup == True:
					iteration = 0
					populated.clear()

			if event.key == pygame.K_s:
				if start == True:
					start = False
					screenshot = True
				elif screenshot == True:
					screenshot = False
					start = True


def grid():

	for x in range(0, WIDTH, TILESIZE):
		pygame.draw.line(screen, GRID, (x, 0), (x, HEIGHT), 1)

	for y in range(0, HEIGHT, TILESIZE):
		pygame.draw.line(screen, GRID, (0, y), (WIDTH, y), 1)


def life(x, y):

	global populated
	global dupl
	global TILESIZE

	if running == True:
		TILESIZE = 20
		X_TILESIZE = x * TILESIZE
		Y_TILESIZE = y * TILESIZE
		location = [X_TILESIZE, Y_TILESIZE]
		populated.append(location)
	else:
		TILESIZE = 10
		x = x - x % TILESIZE
		y = y - y % TILESIZE
		X_TILESIZE = x
		Y_TILESIZE = y
		location = [X_TILESIZE, Y_TILESIZE]

	if setup == True and len(populated) >= 1 and remove == True:
		for org in populated:
			if org == location:
				populated.remove(org)
	elif setup == True and remove == False:
		for org in populated:
			if org == location:
				dupl = True
		if dupl == False:
			populated.append(location)
		dupl = False

	del location


def death(location):

	global unpopulated

	unpopulated.append(location)

	del location


def factory():

	life(24, 10)
	life(24, 13)
	life(25, 12)
	life(23, 12)
	life(24, 12)

	life(43, 10)
	life(43, 11)
	life(43, 12)
	life(39, 5)
	life(40, 6)
	life(41, 7)
	life(42, 8)
	life(43, 9)
	life(40, 10)
	life(40, 14)
	life(42, 19)
	life(42, 11)


def render():

	global populated
	global iteration
	global start
	global running
	global setup
	global FPS
	global remember
	global screenshot
	
	screen.fill(BACKGROUND)

	for organism in populated:

		if start == True or screenshot == True:
			r = random.randint(10, 250)
			g = random.randint(10, 250)
			b = random.randint(10, 250)
		elif running == True:
			r = 30
			g = random.randint(60, 160)
			b = 30	
		else:
			r = 100
			g = 100
			b = 100
			
		ORGANISM = [r, g, b]
		pygame.draw.rect(screen, ORGANISM, (organism, [TILESIZE, TILESIZE]))	

	if setup == True:
		grid()
	if setup == True or start == True:
		screen.blit(text2, text2Rect)
		text3 = font2.render(str(len(populated)), True, [255, 255, 255])
		screen.blit(text3, text3Rect)
		screen.blit(text4, text4Rect)
		if start == True and len(populated) != 0:
			iteration += 1
		text5 = font2.render(str(iteration), True, [255, 255, 255])
		screen.blit(text5, text5Rect)

	if start == True:
		screen.blit(text12, text12Rect)
		text13 = font2.render(str(FPS), True, [255, 255, 255])
		screen.blit(text13, text13Rect)

	if setup == True:
		screen.blit(text12, text12Rect)
		text14 = font2.render(str(remember), True, [255, 255, 255])
		screen.blit(text14, text14Rect)

	if running == True:
		screen.blit(text, textRect)
		screen.blit(text1, text1Rect)
		screen.blit(text6, text6Rect)
		screen.blit(text7, text7Rect)
		screen.blit(text8, text8Rect)
		screen.blit(text9, text9Rect)
		screen.blit(text10, text10Rect)
		screen.blit(text11, text11Rect)
		screen.blit(text15, text15Rect)
		screen.blit(text16, text16Rect)

	pygame.display.flip()


def duplication():

	global location
	global i

	duplicate = False

	if i == 1:
		death(location)
	else:
		for empty in unpopulated:
			if empty == location:
				duplicate = True
		if duplicate == False:
			death(location)
		duplicate = False


def rule():

	global unpopulated
	global populated
	global location
	global running
	global i
	
	unpopulated = []

	i = 1

	for organism in populated:
		
		numOfNeighbour = 0

		existR = False
		existL = False
		existU = False
		existD = False
		existCUR = False
		existCDR = False
		existCUL = False
		existCDL = False

		if running == False:
			if organism[0] > 1010 or organism[0] < 0 or organism[1] > 630 or organism[1] < 0: 
				populated.remove(organism)


		for neighbour in populated:

			if neighbour != organism:
				
				if neighbour[0] == organism[0] + TILESIZE and neighbour[1] == organism[1]:
					numOfNeighbour += 1
					existR = True
		
				elif neighbour[0] == organism[0] - TILESIZE and neighbour[1] == organism[1]:
					numOfNeighbour += 1
					existL = True

				elif neighbour[1] == organism[1] + TILESIZE and neighbour[0] == organism[0]:
					numOfNeighbour += 1
					existD = True

				elif neighbour[1] == organism[1] - TILESIZE and neighbour[0] == organism[0]:
					numOfNeighbour += 1
					existU = True
		
				elif neighbour[0] == organism[0] + TILESIZE and neighbour[1] == organism[1] - TILESIZE:
					numOfNeighbour += 1
					existCUR = True

				elif neighbour[0] == organism[0] + TILESIZE and neighbour[1] == organism[1] + TILESIZE:
					numOfNeighbour += 1
					existCDR = True

				elif neighbour[0] == organism[0] - TILESIZE and neighbour[1] == organism[1] - TILESIZE:
					numOfNeighbour += 1
					existCUL = True
		
				elif neighbour[0] == organism[0] - TILESIZE and neighbour[1] == organism[1] + TILESIZE:
					numOfNeighbour += 1
					existCDL = True

		if existR == False:
			location = [organism[0] + TILESIZE, organism[1]]
			duplication()

		if existL == False:
			location = [organism[0] - TILESIZE, organism[1]]
			duplication()

		if existU == False:
			location = [organism[0], organism[1] - TILESIZE]
			duplication()

		if existD == False:
			location = [organism[0], organism[1] + TILESIZE]
			duplication()

		if existCUR == False:
			location = [organism[0] + TILESIZE, organism[1] - TILESIZE]
			duplication()

		if existCDR == False:
			location = [organism[0] + TILESIZE, organism[1] + TILESIZE]
			duplication()

		if existCUL == False:
			location = [organism[0] - TILESIZE, organism[1] - TILESIZE]
			duplication()

		if existCDL == False:
			location = [organism[0] - TILESIZE, organism[1] + TILESIZE]
			duplication()

		i += 1

		if numOfNeighbour < 2 or numOfNeighbour > 3:
			organism.append("die")

	for empty in unpopulated:
		
		numOfNeighbour = 0

		for neighbour in populated:
				
			if neighbour[0] == empty[0] + TILESIZE and neighbour[1] == empty[1]:
				numOfNeighbour += 1
					
			elif neighbour[0] == empty[0] - TILESIZE and neighbour[1] == empty[1]:
				numOfNeighbour += 1
				
			elif neighbour[1] == empty[1] + TILESIZE and neighbour[0] == empty[0]:
				numOfNeighbour += 1
				
			elif neighbour[1] == empty[1] - TILESIZE and neighbour[0] == empty[0]:
				numOfNeighbour += 1
					
			elif neighbour[0] == empty[0] + TILESIZE and neighbour[1] == empty[1] - TILESIZE:
				numOfNeighbour += 1
				
			elif neighbour[0] == empty[0] + TILESIZE and neighbour[1] == empty[1] + TILESIZE:
				numOfNeighbour += 1
				
			elif neighbour[0] == empty[0] - TILESIZE and neighbour[1] == empty[1] - TILESIZE:
				numOfNeighbour += 1
					
			elif neighbour[0] == empty[0] - TILESIZE and neighbour[1] == empty[1] + TILESIZE:
				numOfNeighbour += 1

		if numOfNeighbour != 3:
			empty.append("empty")

	born = []

	for empty in unpopulated:
		if len(empty) == 2:
			born.append(empty)

	survive = []

	for organism in populated:
		if len(organism) == 2:
			survive.append(organism)

	populated = survive + born

	del unpopulated
	del survive
	del born


factory()

running = True

while running:
	render()
	rule()
	clock.tick(FPS)
	event()
	
populated.clear()
TILESIZE = 10

while simulation:

	FPS = 60

	while setup:
		clock.tick(FPS)
		render()
		event()
				
	FPS = remember

	while start:
		clock.tick(FPS)
		remember = FPS
		rule()
		render()
		event()

	while screenshot:
		render()
		clock.tick(FPS)
		event()