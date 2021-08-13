import pygame
from decimal import *
from stuff import Grid, Box, load_image, Button, write, scale
from minmax import availableSpaces, selectSpace, minimax, gameIsOver, hasWon, clearBoard
pygame.init()
w = 500
h = 500
win = pygame.display.set_mode((w, h))
board = [['', '', ''],
		 ['', '', ''],
		 ['', '', '']]

def clear():
	pygame.display.update()
	win.fill((225, 225, 225))



def menu():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	pygame.quit()


def main():
	running = True
	r = 3
	c = 3
	lw = 500
	lh = 300
	highlight = Box(0, 0, lw//c, lh//r, fill=False)
	objects = []
	notAvailable = []
	turn = False
	mode = "multiplayer"
	sense = "MUMU"
	playing = False
	lastwin = None
	singlePlayer = Button(lw//2, lh//2, 100, 30, string="SINGLE PLAYER")
	multiplayer = Button(lw//2, singlePlayer.rect.centery+50, 100, 30, string="MULTIPLAYER")
	brainLevelDown = Button(0, multiplayer.rect.centery+50, 20, 30, string="<")
	brainLevelDown.rect.left = multiplayer.rect.left - 3
	brainLevelUp = Button(0, multiplayer.rect.centery+50, 20, 30, string=">")
	brainLevelUp.rect.right = multiplayer.rect.right + 3
	brainLevel = Button(lw//2, brainLevelUp.rect.centery, 60, 30, string=sense)
	quit = Button(lw//2, brainLevel.rect.centery+50, 100, 30, string="QUIT")
	menu = [singlePlayer, multiplayer, brainLevelUp, brainLevelDown, brainLevel, quit]
	if turn:
		letter = 'x'
	else:
		letter = 'o'
	while running:
		mouse = pygame.mouse.get_pos()
		mx = int(Decimal(scale(mouse[0], lw, c)).quantize(Decimal('1.'), rounding=ROUND_DOWN))
		my = int(Decimal(scale(mouse[1], lh, r)).quantize(Decimal('1.'), rounding=ROUND_DOWN))
		if playing:
			if my * lh//r >= (lh - 100):
				highlight.rect.y = scale(lh-100, lh-100, r-1) *lh//r
			else:
				highlight.rect.y = my * lh//r
			highlight.rect.x = mx * lw//c
			
			if turn:
				letter = 'x'
			else:
				letter = 'o'
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.MOUSEBUTTONUP and playing:
				if ((mode == "multiplayer" and not turn) or (mode == "multiplayer" and turn) or (mode == "single" and turn)) and not gameIsOver(board) and playing:
					selectSpace(board, [mx, my], letter)
	
			elif event.type == pygame.MOUSEBUTTONUP and not playing:
				for but in menu:
					if but == singlePlayer and singlePlayer.is_over(mouse[0], mouse[1]):
						mode = "single"
						playing = True
					elif but == multiplayer and multiplayer.is_over(mouse[0], mouse[1]):
						mode = "multiplayer"
						playing = True
					if brainLevelUp.is_over(mouse[0], mouse[1]):
						sense = "GOD LEVEL"
					elif brainLevelDown.is_over(mouse[0], mouse[1]):
						sense = "MUMU"
					if quit.is_over(mouse[0], mouse[1]):
						running = False

		#print(playing)
		brainLevel.string = sense
		if mode == "single" and not turn and not gameIsOver(board) and playing:
			if sense == "GOD LEVEL":
				selectSpace(board, minimax(board, depth=6)[1], 'o')
			elif sense == "MUMU":
				selectSpace(board, minimax(board, depth=4)[1], 'o')
			
			
		if playing:
			for i in range(len(board)):
				for j in range(len(board[i])):
					if notAvailable.count([j, i]) == 0:
						if board[i][j] == 'x':
							x, x_rect= load_image("xo/ex.png")
							x = pygame.transform.scale(x, (lw//c, lh//r))
							x_rect.x = j * (lw//c)
							x_rect.y = i * (lh//r)
							objects.append([x, x_rect])
							notAvailable.append([j, i])
							turn = not turn
								
						elif board[i][j] == 'o':
							o, o_rect = load_image("xo/oh.png")
							o = pygame.transform.scale(o, (lw//c, lh//r))
							o_rect.x = j * (lw//c)
							o_rect.y = i * (lh//r)
							objects.append([o, o_rect])
							notAvailable.append([j, i])
							turn = not turn

		if playing:
			if hasWon(board) is not False or gameIsOver(board):
				if hasWon(board) is not False:
					lastwin = hasWon(board)
				else:
					lastwin = "tie"
				clearBoard(board)
				objects.clear()
				notAvailable.clear()
				playing = False
			Grid(win, r, c, lw, lh)
			for o in objects:
				win.blit(o[0], o[1])
			highlight.draw(win)
		if not playing:
			for but in menu:
				but.is_over(mouse[0], mouse[1])
				but.draw(win)
			if lastwin != "tie" and lastwin != None:
				write(win, "PLAYER " + lastwin.upper() + " WON THE LAST GAME!!!", lw//2, quit.rect.centery+100, 30)
			elif lastwin == "tie":
				write(win, "THE LAST GAME WAS A TIE", lw//2, quit.rect.centery+100, 30)
		clear()
	pygame.quit()

if __name__ == "__main__":
	main()