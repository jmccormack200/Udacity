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

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,test,goal,cost):
	current_point = test
	goal_not_found = True
	depth = 1
	while(goal_not_found):
		if (grid[current_point[0]][current_point[1]]) == 0:
			grid[current_point[0]][current_point[1]] = X
			if current_point[0] <= len(current_point):
				current_point[0]+= 1
		goal_not_found = False
	path = "Test"
	return path




if __name__ == '__main__':
	print "scoop whoop"
	print search(grid, init, goal, cost)
	