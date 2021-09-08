import copy
import numpy as np
import datetime


def hasWon(p_board):
	for i in range(len(p_board)):
		if p_board[i][0] == p_board[i][1] == p_board[i][2] == 'x':
			return 'x'
			break
		elif p_board[i][0] == p_board[i][1] == p_board[i][2] == 'o':
			return 'o' 
			break
		for j in range(len(p_board[i])):
			if i == 0:
				if p_board[i][j] == p_board[i+1][j] == p_board[i+2][j] == 'x':
					return 'x'
					break
				elif p_board[i][j] == p_board[i+1][j] == p_board[i+2][j] == 'o':
					return 'o'
					break
			if j == 0:
				if i == 0 and p_board[i][j] == p_board[1][1] == p_board[2][2] == 'x':
					return 'x'
					break
				elif i == 2 and p_board[i][j] == p_board[1][1] == p_board[0][2] == 'x':
					return 'x'
					break
				if i == 0 and p_board[i][j] == p_board[1][1] == p_board[2][2] == 'o':
					return 'o'
					break
				elif i == 2 and p_board[i][j] == p_board[1][1] == p_board[0][2] == 'o':
					return 'o'
					break
	return False

def availableSpaces(p_board):
	validMoves = []
	for i in range(len(p_board)):
		for j in range(len(p_board[i])):
			if p_board[i][j] == '':
				validMoves.append([j, i])
	return validMoves

def gameIsOver(p_board):
	if len(availableSpaces(p_board)) == 0 or hasWon(p_board) is not False:
		return True
	return False

def selectSpace(p_board, spot, l):
	p_board[spot[1]][spot[0]] = l

def clearBoard(p_board):
	for i in range(len(p_board)):
		for j in range(len(p_board[i])):
			selectSpace(p_board, [j, i], '')

def evaluateBoard(p_board):
	if hasWon(p_board) is False:
		return 0
	if hasWon(p_board) == 'o':
		return 1
	elif hasWon(p_board) == 'x':
		return -1





def minimax(p_board, start, depth, isMaximising=True, alpha=float('-inf'), beta=float('inf')):
	if (datetime.datetime.now()-start).total_seconds()*1000>100:
		return [None]

	if depth<=0:
		return [evaluateBoard(p_board)] 

	if gameIsOver(p_board):
		return [evaluateBoard(p_board)]


	else:

		bestMove=None
		if isMaximising:
			letter = 'o'
			bestScore = -1000
		else:
			letter = 'x'
			bestScore = 1000
		for i in range(len(availableSpaces(p_board))):
			f_board = copy.deepcopy(p_board)
			selectSpace(f_board, availableSpaces(f_board)[i], letter)
			#print(f_board, "\n")
			
			if isMaximising:
				h_bestScore = minimax(f_board, start, depth-1, not isMaximising, alpha, beta)[0]
				if h_bestScore==None:
					return [None]
				if h_bestScore > bestScore:
					bestScore = h_bestScore
					bestMove = availableSpaces(p_board)[i]
					alpha = max(alpha, bestScore)
					if alpha>=beta:
						break

			elif not isMaximising:
				h_bestScore = minimax(f_board, start, depth-1, not isMaximising, alpha, beta)[0]
				if h_bestScore==None:
					return [None]
				if h_bestScore < bestScore:
					bestScore = h_bestScore
					bestMove = availableSpaces(p_board)[i]
					beta=min(beta, bestScore)
					if beta<=alpha:
						break

		
		return [bestScore, bestMove]

def ids(state):
	start_time=datetime.datetime.now()
	best_move=[-1, -1]
	d=1
	move=minimax(state, start_time, d)
	while move[0]!=None:
		d+=1
		move=minimax(state, start_time, d)
		if move[0]!=None:
			bestMove=move[1]
	print(d)
	return bestMove



