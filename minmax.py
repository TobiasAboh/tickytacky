import copy

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
	if len(availableSpaces(p_board)) == 0 and hasWon(p_board) is False:
		return 0
	if hasWon(p_board) == 'o':
		return 1
	elif hasWon(p_board) == 'x':
		return -1

def minimax(p_board, isMaximising=True, depth=0, maxdepth=10):
	depth += 1
	#print(depth)
	if len(availableSpaces(p_board)) == 9:
		return [0, [0, 0]]
	if gameIsOver(p_board):
		return [evaluateBoard(p_board)]
	else:
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
			h_bestScore = minimax(f_board, not isMaximising, depth, maxdepth)[0]
			if isMaximising:
				if h_bestScore > bestScore:
					bestScore = h_bestScore
					bestMove = availableSpaces(p_board)[i]
			elif not isMaximising:
				if h_bestScore < bestScore:
					bestScore = h_bestScore
					bestMove = availableSpaces(p_board)[i]
			if depth >= maxdepth:
				break
		
		return [bestScore, bestMove]




