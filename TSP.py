from sys import maxsize
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, s):

	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		current_pathweight = 0

		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		min_path = min(min_path, current_pathweight)
		
	return min_path

if __name__ == "__main__":

	
	graph = [[20, 90, 65, 89], [85, 75, 95, 78],
			[25, 75, 0, 370], [720, 45, 60, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))
