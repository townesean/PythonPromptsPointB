"""
KnightTests.py
Sean Towne
07/24/2021
"""

import time

def legalKnightMovesFromSquare(squareNumber):
	if squareNumber not in range(0, 64):
		raise ValueError("Square Number must be in [0, 63]")

	# coordinants of square on chess board
	x = squareNumber % 8
	y = squareNumber // 8

	# generate all knight moves from coordinant
	# moves are listed in clockwise circle around knight (easier to debug)
	moves = [
		[x - 2, y - 1],
		[x - 1, y - 2],
		[x + 1, y - 2],
		[x + 2, y - 1],
		[x + 2, y + 1],
		[x + 1, y + 2],
		[x - 1, y + 2],
		[x - 2, y + 1],
	]

	# filter out moves that do not land on the chess board
	moves = list(filter(lambda x:x[0] >= 0 and x[0] <= 7, moves))
	moves = list(filter(lambda x:x[1] >= 0 and x[1] <= 7, moves))

	# translate moves back to numbered square [0,63]
	for i in range(0, len(moves)):
		moves[i] = moves[i][1]*8 + moves[i][0]

	# legal knight moves reachable from squareNumber
	return moves

	

def printPath(src):
	print('-------------------------')
	for i in range(0, 8):
		for j in range(0, 8):
			char = "  "
			squareNumber = 8*i + j
			if squareNumber in src:
				char = str(src.index(squareNumber))
				if len(char) == 1: char = " "+char
			print("|"+char, end = '')
		print("|")
		#print('-------------------------')
	print('-------------------------')


"""
does a breadth first search in the graph of knight
moves on a chess board. Returns the path of the
knight as a list of integers.

I borrowed heavily from the code I found here:
https://favtutor.com/blogs/breadth-first-search-python
"""
def bestKnightPathFromSourceToDestination(src, dest):
	# solved, return path containing only the starting square.
	if src == dest: return [src]

	# keeping track of all nodes visited
	# every node is a key, and every value
	# is the parent node of that key. The parent of 
	# the root node is considered to be itself in 
	# this case (makes checking later easier)
	visited = {src:src}

	# keeps track of every node whose children have
	# not been explored. 
	queue = [src]

	# while there are nodes whose children have not
	# been visited, we loop.
	while queue:

		# dequeue next parent to seach under
		nextParent = queue.pop(0)

		# get all the children of nextParent
		moves = legalKnightMovesFromSquare(nextParent)

		for move in moves:
			if move not in visited.keys():
				# Keeping track of every visited node and its parent
				visited[move] = nextParent
				# if unvisited, make sure we check its children
				queue.append(move)

			# Done! everything we need is in "visited"
			if move == dest:
				break

	# Builds the path taken by the knight by back tracking
	# through the "visited" dictionary.
	path = []
	move = dest
	while move != visited[move]:
		path.append(move)
		move = visited[move]
	path.append(move)
	return path[::-1]



# little interactive loop to test the function
if __name__ == "__main__":
	while True:
		print()
		s = int(input("Enter start square: "))
		d = int(input("Enter destn square: "))
		t0 = time.time()
		path = bestKnightPathFromSourceToDestination(s, d)
		t1 = time.time()
		dt = t1-t0
		print("Path: ", path)
		printPath(path)
		print("Completed in " + str(dt*1000) + " ms\n")



