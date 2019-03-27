import queue 

class Koor:
  # Attributes: int x, int y
  def __init__(self, _x=0, _y=0):
    self.x = _x
    self.y = _y

  def __hash__(self):
    return hash((self.x, self.y))
  
  def __eq__(self, other):
    return (self.x == other.x) and (self.y == other.y)

  def __ne__(self, other):
    return not self.__eq__(other)
 
  def __str__(self):
    return ("(" + str(self.x) + "," + str(self.y) + ")")

  def __repr__(self):
    return self.__str__()

  def set(self, _x, _y):
    self.x = _x
    self.y = _y


  def getLeft(self):
    return Koor(self.x - 1, self.y)
  def getRight(self):
    return Koor(self.x + 1, self.y)
  def getUp(self):
    return Koor(self.x, self.y - 1)
  def getDown(self):
    return Koor(self.x, self.y + 1)

class Tree:
  # Attributes: dict of key(child_node) value(parent_node)
  def __init__(self):
    self.data = dict()
  
  def add(self, child_node, parent_node):
    self.data[child_node] = parent_node
  
  def getNodeParent(self, child_node):
    return self.data[child_node]

  def printTree(self):
    print("isi tree =")
    for c, p in self.data.items():
      print(c, ":", p)


def readFileEksternal(s):
  fin = open(s, "r")
  fr = fin.read()
  fin.close()
  fr_list = fr.split('\n')
  return fr_list

def getMazeSize(maze):
  x_size = len(maze[0])
  y_size = len(maze)
  return (x_size, y_size)

def getGatesPos(maze):
# Asumsi: start berada di tembok kiri, finish di tembok kanan
  startPos = Koor()
  finishPos = Koor()

  for i in range(y_size):
    # Periksa start
    if (maze[i][0] == '0'):
      startPos.set(0, 1)
    
    # Periksa finish
    if (maze[i][x_size-1] == '0'):
      finishPos.set(x_size-1, i)

  return startPos, finishPos


def leftPossible(maze, curr):
  if (curr.getLeft() in visited):
    return False
  return (curr.x-1 >= 0 and maze[curr.y][curr.x-1] == '0')

def rightPossible(maze, curr):
  if (curr.getRight() in visited):
    return False
  return (curr.x+1 < x_size and maze[curr.y][curr.x+1] == '0')

def upPossible(maze, curr):
  if (curr.getUp() in visited):
    return False
  return (curr.y-1 >= 0 and maze[curr.y-1][curr.x] == '0')

def downPossible(maze, curr):
  if (curr.getDown() in visited):
    return False
  return (curr.y+1 < y_size and maze[curr.y+1][curr.x] == '0')

visited = set() # set of Koor
q = queue.Queue() # queue of Koor
tree = Tree()  # dict of key(Koor) value(Koor)
x_size = 0; y_size = 0

def BFS(maze):
  global x_size, y_size

  x_size, y_size = getMazeSize(maze)
  startPos, finishPos = getGatesPos(maze)

  # Mulai penelusuran
  q.put(startPos)
  while(not q.empty()):
    currKoor = q.get()

    if currKoor == finishPos: # Jika mencapai finish
      break
    visited.add(currKoor)

    if leftPossible(maze, currKoor):
      left = currKoor.getLeft()
      tree.add(left, currKoor)
      q.put(left)
    if rightPossible(maze, currKoor):
      right = currKoor.getRight()
      tree.add(right, currKoor)
      q.put(right)
    if upPossible(maze, currKoor):
      up = currKoor.getUp()
      tree.add(up, currKoor)
      q.put(up)
    if downPossible(maze, currKoor):
      down = currKoor.getDown()
      tree.add(down, currKoor)
      q.put(down)

    # c = input()

  if currKoor != finishPos:
    return []

  pathLog = []    
  ptKoor = currKoor
  pathLog.append(ptKoor)
  # tree.printTree()
  while (ptKoor != startPos):
    ptKoor = tree.getNodeParent(ptKoor)
    pathLog.append(ptKoor)

  pathLog.reverse()
  return pathLog


def main():
  inpF = "maze_small.txt"
  maze = readFileEksternal(inpF)

  print("Pilih metode penelusuran:")
  print("1. BFS")
  print("2. A*")
  cmd = int(input("Pilihan: "))
  if (cmd == 1):
    pathSolusi = BFS(maze)
    print(pathSolusi)

  elif (cmd == 2):
    pass
  else:
    print("Pilihan yang anda masukkan salah")

if __name__ == "__main__":
  main()

