# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import copy

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
		
expand = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
search = [[,,,,,],
        [,,,,,],
        [,,,,,],
        [,,,,,],
        [,,,,,]]
		 

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1


def search(grid,init,goal,cost):
	search_array = [[0, init[0], init[1]]]
	grid[init[0]][init[1]] = -1

	expand_count = 0

	row =  len(grid)
	column = len(grid[0])
	
	not_found = True
	
	while(not_found):
	
		try:
			current_node = search_array.pop(0)
			expand[current_node[1]][current_node[2]] = expand_count
			expand_count += 1
			
			if current_node[1] == goal[0] and current_node[2] == goal[1]:
				return expand
		except:
			return "fail"
			
		#	Below is useful for seeing the progression
		#print "current node = " + str(current_node)			
			
		#Check all directions and append appropriate ones to the list, will not add
		#anywhere that is marked as blocked (1) or already checked (-1)
		
		#Check Left
		if (current_node[1] - 1 >= 0):
			if (grid[current_node[1]-1][current_node[2]] == 0):
				search_array.append([current_node[0] + 1, current_node[1] - 1, current_node[2]])
				grid[current_node[1] - 1][current_node[2]] = -1
			
		#Check Right
		if (current_node[1] + 1 < row):
			if (grid[current_node[1] + 1][current_node[2]] == 0):
				search_array.append([current_node[0] + 1, current_node[1] + 1, current_node[2]])
				grid[current_node[1] + 1][current_node[2]] = -1
		
		#Check Up
		if (current_node[2] - 1 >= 0):
			if (grid[current_node[1]][current_node[2] - 1] == 0):
				search_array.append([current_node[0] + 1, current_node[1], current_node[2]])
				grid[current_node[1]][current_node[2] - 1] = -1
		
		#Check Down
		if (current_node[2] + 1 < column):
			if (grid[current_node[1]][current_node[2] + 1] == 0):
				search_array.append([current_node[0] + 1, current_node[1], current_node[2] + 1])
				grid[current_node[1]][current_node[2] + 1] = -1
		
		
if __name__ == "__main__":
	print search(grid, [0,0], goal, cost)
	
	