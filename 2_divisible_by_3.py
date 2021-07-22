# Sean Towne
# 07/22/2021

# I hope this is not cheating.
# I don't want to write the combination
# algorithm by hand.
import itertools

# https://www.math-only-math.com/divisible-by-3.html
# using the trick where if the sum of the digits is
# divisible by 3, any number composed of those digits
# is divisible by 3.
def divisibleByThree(l):
	return sum(l)%3 == 0

# takes a list of digits and returns the
# largest integer that can be made from combining them.
def composeLargestIntFromListOfDigits(l):
	num = 0
	l = sorted(list(l))
	
	while True:
		digit = l.pop()
		nextValue = digit * 10**len(l)
		num = num + nextValue
		if len(l) == 0: return num


def solution(L):
	# how many digits in the original L are we going to use?
	combinationLength = len(L)

	# Looping through different lengths of combinations.
	while combinationLength > 0:

		# all sub combinations of L with "combinationLength" number of digits.
		combinations = itertools.combinations(L, combinationLength)

		# we only want those combinations that are divisible by three.
		combinationsDivisibleByThree = list(filter(lambda x:divisibleByThree(x), combinations))
		
		# if none are divisible by three, we need to remove a digit and start over.
		if len(combinationsDivisibleByThree) == 0: 
			combinationLength -= 1
			continue

		# Because the algorithm starts with combinations with more digits
		# whatever is in the "solutions" list are the largest value candidates.
		solutions = map(lambda x:composeLargestIntFromListOfDigits(x), combinationsDivisibleByThree)
		largestSolution = max(solutions)
		return largestSolution

	# return 0 on failure to find a number divisible by three.
	return 0
		

# Test Case 1
print(solution([3, 1, 4, 1]))

# Test Case 2
print(solution([3, 1, 4, 1, 5, 9]))










