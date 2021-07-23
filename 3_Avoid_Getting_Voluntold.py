# Sean Towne
# 07/22/2021

"""
For reference:
-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
"""


"""
Given the number of a square on the chess
board x, this function returns the numbers of
the squares where a knight could move from
x.
"""
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


# returns a tuple where the first element is the
# number of hops associated with an optimal path,
# and the second element is an array representing
# the corresponding path. The purpose of the tuple
# is for printing out the path.
def solution(src, dest):
	# going to use src as a path history, 
	# need to change it to an iterable object.
	if not hasattr(src, '__iter__'): src = [src]

	# create a well named reference to the top of src history
	# and to the number of moves so far
	current = src[len(src)-1]
	numberOfMoves = len(src)-1

	# https://chess.stackexchange.com/questions/4465/longest-path-for-knight
	# it is possible to get to any square on a 
	# chessboard with a knight in 6 or less hops
	if numberOfMoves > 6: return float('inf'), []

	# base case.
	# Recursion should stop when our starting
	# square is the same as where we want to go.
	if current == dest: return numberOfMoves, src

	# Get the list of squares we can move to and
	# filter out squares we have already visited.
	# If dead end, return large number.
	nextPossibleMoves = legalKnightMovesFromSquare(current)
	nextPossibleMoves = list(filter(lambda x:x not in src, nextPossibleMoves))
	if len(nextPossibleMoves) == 0: return float('inf'), []

	# Recurse into all possible paths that do not
	# loop in on themselves and that do not exceed
	# a length of 6.
	pathLengths = []
	for move in nextPossibleMoves:
		nextSrc = src + [move]
		pathLengths.append(solution(nextSrc, dest))

	# return the length of fastest path
	# along with the path itself.
	lengths = [p[0] for p in pathLengths]
	bestLength = min(lengths)
	bestIndex = lengths.index(bestLength)
	return pathLengths[bestIndex]


# Test Case 1
answer = solution(19, 36)
printPath(answer[1])
print("Number of Hops: " + str(answer[0]) + "\n")

# Test Case 2
answer = solution(0, 1)
printPath(answer[1])
print("Number of Hops: " + str(answer[0]) + "\n")

# My test Cases
answer = solution(0, 63)
printPath(answer[1])
print("Number of Hops: " + str(answer[0]) + "\n")

answer = solution(20, 38)
printPath(answer[1])
print("Number of Hops: " + str(answer[0]) + "\n")





