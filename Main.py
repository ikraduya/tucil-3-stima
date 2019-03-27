class Koor:
  # Attributes: int x, int y

  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y

class Node:
  # Attributes: Koor currKoor, Koor prevKoor

  def __init__(self, _currKoor, _prevKoor):
    self.curr = _currKoor
    self.prev = _prevKoor


def readFileEksternal(s):
  fin = open(s, "r")
  fr = fin.read()
  fin.close()
  fr_list = fr.split('\n')
  return fr

maze = []
def main():
  inpF = "maze_small.txt"
  maze = readFileEksternal(inpF)

  print("Pilih metode penelusuran:")
  print("1. BFS")
  print("2. A*")
  cmd = int(input("Pilihan: "))
  if (cmd == 1):
    pass
  elif (cmd == 2):
    pass
  else:
    print("Pilihan yang anda masukkan salah")

if __name__ == "__main__":
  main()

