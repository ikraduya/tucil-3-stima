def readFileEksternal(s):
  fin = open(s, "r")
  fr = fin.read()
  fin.close()
  fr_list = fr.split('\n')
  return fr

def main():
  inpF = "maze_small.txt"
  mz_list = readFileEksternal(inpF)

  

if __name__ == "__main__":
  main()

