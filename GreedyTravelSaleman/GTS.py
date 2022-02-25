
INT_MAX = 2000000000

def findShortestEdge(travelPaths, startVertex, visited):
  cost = INT_MAX
  l = len(travelPaths)
  for i in range(0, l):
    if i not in visited:
      if travelPaths[startVertex][i] < cost and travelPaths[startVertex][i] > 0:
        cost = travelPaths[startVertex][i]
        nextVertex = i
  return nextVertex

def GreedyTravelSaleman(travelPaths, startPoint):
  cost = 0
  tour = [startPoint]
  standingPoint = startPoint
  length = len(travelPaths)

  # edge = vertex  - 1
  for i in range(0, length - 1):
    nextPoint = findShortestEdge(travelPaths, standingPoint, tour)
    tour.append(nextPoint)
    cost = cost + travelPaths[standingPoint][nextPoint]
    standingPoint = nextPoint

  tour.append(startPoint)
  cost = cost + travelPaths[standingPoint][startPoint]
  return [tour, cost]

testPath=[
  [-1, 20, 42, 31, 6, 24],
  [10, -1, 17, 6, 35, 18],
  [25, 5, -1, 27, 14, 9],
  [12, 9, 24, -1, 30, 12],
  [14, 7, 21, 15, -1, 38],
  [40, 15, 16, 5, 20, -1]
]

result = GreedyTravelSaleman(testPath, 0)
for i in result[0]:
  print(i, "-> ", end='')
print('Cost:', result[1])