
COLOR = ['red', 'blue', 'green', 'yellow', 'violet', 'orange']

TestGraph = [
  [0, 1, 1, 0, 1, 0, 0],
  [1, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 1, 1, 1, 0],
  [0, 0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 1, 1],
  [0, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 1, 0]
]
LENG = 7

vertexes = []

class Vertex:
  def __init__(self, name, degree):
    self.name = name
    self.degree = degree
    self.color = ''

def getVertexDegree(graph, vertexNo):
  degree = 0
  for d in graph[vertexNo]:
    degree = d + degree
  return degree

def isConnected(graph, v1, v2):
  return graph[v1][v2]

def sortDegree(vertexArray):
  leng = len(vertexArray)
  for i in range(0, leng - 1):
    for j in range(i + 1, leng):
      if vertexArray[i].degree <= vertexArray[j].degree:
        temp = vertexArray[i]
        vertexArray[i] = vertexArray[j]
        vertexArray[j] = temp

  return vertexArray 

def printVertexArray(vArray):
  for v in vArray:
    print(v.name, v.degree, v.color)


def greedyColoring(graph, sortedArray):
  index = 1
  color = 1
  # color the biggest
  sortedArray[0].color = COLOR[0]

  # set current = second
  current = sortedArray[index]

  # color vertes not connect with biggest
  while index < LENG - 1:
    # color the next biggest if not colored
    if current.color == '':
      current.color = COLOR[color]
    for i in range(LENG):
      # skip itself or previous biggest
      if sortedArray[i].name == current.name or i < index:
        continue
      
      # if smaller not colered and not connected to biggest => color it
      if sortedArray[i].color == '' and isConnected(graph, sortedArray[i].name, current.name) == 0:
        sortedArray[i].color = COLOR[color]

    # change next biggest and color
    index += 1
    color += 1
    current = sortedArray[index]

  return sortedArray
  


if __name__ == "__main__":
  for i in range(len(TestGraph)):
    deg = getVertexDegree(TestGraph, i)
    vertexes.append(Vertex(i, deg))

  # printVertexArray(vertexes)

  
  colored = greedyColoring(TestGraph, sortDegree(vertexes))
  printVertexArray(colored)