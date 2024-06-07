def printSolution2(sol):
    for i in range(len(sol)+2):
        print("--", end="")
    print("")
    for i in sol:
        print("|", end="")
        for j in i:
            if j == 0:
                print("  ", end ="")
            if j == 1:
                print("* ", end ="")
        #     print(str(j) + " ", end ="")
        # print(str(j) + " ", end ="")
        print("|")
    for i in range(len(sol)+2):
        print("--", end="")
    print("")

def printSolution(sol):
    for i in sol:
        for j in i:
            if j == 0:
                print("  ", end ="")
            if j == 1:
                print("* ", end ="")
        #     print(str(j) + " ", end ="")
        # print(str(j) + " ", end ="")
        print("")


def isSafe(maze, x, y):
    if x >=0 and x<= len(maze[0])-1 and y>=0 and y <= len(maze)-1 and maze[y][x]==0:
        #print("x: {}, y: {}, maze: {}".format(x,y, maze[y][x]))
        return True
    return False

def solveMazeUtil(maze, x, y, sol):
    # verificam daca x,y este punctul final al labirintului
    if x == len(maze[0])-1 and y == len(maze)-1 and maze[y][x]==0:
        sol[y][x] = 1
        return True

    if isSafe(maze, x, y):
        # verificam daca (x,y) este deja in lista de solutii
        if sol[y][x] == 1:
            return False
        
        #punem pozitia (x,y) in solutie
        sol[y][x] = 1

        if solveMazeUtil(maze, x+1, y, sol):
            return True

        if solveMazeUtil(maze, x, y+1, sol):
            return True
        
        if solveMazeUtil(maze, x-1, y, sol):
            return True

        if solveMazeUtil(maze, x, y-1, sol):
            return True

        sol[y][x] = 0
        return False



def solveMaze(maze):
    sol = [ [0 for i in range(len(maze[0]))] for j in range(len(maze))]
    printSolution(sol)
    
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Nu avem solutie")
        return False
    print("solutia este:")
    printSolution(sol)
    return True



if __name__ == "__main__":
    maze = [
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0]
    ]
    print("The Maze is :\n")
    printSolution2(maze)
    print(" ")
    solveMaze(maze)