# Sean Towne
# 07/22/2021
 

# I know there has to be a more elequent way of doing this,
# but this works and its not too inefficient
def solution(data, n):
	# Count the frequencty of each value like a histogram
	seen = {}
	for d in data:
		if d in seen.keys():
			seen[d] += 1
		else:
			seen[d] = 1

	# for every value in the dictionary greater
	# than n, filter the offending element out 
	# of the the list
	for key in seen.keys():
		if seen[key] <= n: continue
		data = list(filter(lambda x: x != key, data))

	return data


# Testcase 1
# should return []
print(
	solution(
		[1, 2, 3], # data
		0          # n
	)
)

# Testcase 2
# should return [1, 4]
print(
	solution(
		[1, 2, 2, 3, 3, 3, 4, 5, 5], 
		1
	)
)

# Testcase 3
# should return [1, 2, 3]
print(
	solution(
		[1, 2, 3], 
		6
	)
)





