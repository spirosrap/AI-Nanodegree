# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  start_state = problem.getStartState()
  if(problem.isGoalState(start_state)):
    return [start_state]

  frontier = util.Stack()
  # frontier.push((start_state,"South",1))
  frontier.push((start_state,"South",1))
  explored = []
  solution = []
  previous = {}
  while True:
    if frontier.isEmpty():
      return []
    node = frontier.pop()

    # solution.append(node[1])
    explored.append(node)
    successors = problem.getSuccessors(node[0])

    for state in successors:
      if not((state in explored) or (state in frontier.list)):
        previous[state] = node
        if(problem.isGoalState(state[0])):
          node = state
          node1 = node
          while node1[0] != start_state:
            solution.append(node1[1])
            node1 = previous[node1]
            print node1
          print("Solution",solution[::-1])
          return solution[::-1]
        frontier.push(state) 

  # util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"

  def heapToList(heap):
    l =[]
    for i in heap:
      l.append(i[1])
    return l
      
  start_state = problem.getStartState()
  if(problem.isGoalState(start_state)):
    return [start_state]

  frontier = util.PriorityQueue()
  # frontier.push((start_state,"South",1))
  cost = 0
  print("start state",start_state)
  frontier.push((start_state,"",1),cost)
  explored = []
  solution = []
  previous = {}
  while True:
    if frontier.isEmpty():
      return []

    node = frontier.pop()

    # solution.append(node[1])
    explored.append(node)
    successors = problem.getSuccessors(node[0])
    cost += 1
    for state in successors:
      if not((state in explored) or (state in heapToList(frontier.heap))):
        previous[state] = node
        if(problem.isGoalState(state[0])):
          node = state
          node1 = node
          while node1[0] != start_state:
            solution.append(node1[1])
            node1 = previous[node1]
            print node1
          print("Solution",solution[::-1])
          return solution[::-1]
        frontier.push(state,cost) 
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  def heapToList(heap):
    l =[]
    for i in heap:
      l.append(i[1])
    return l
  def f(a):
    return a[2]  

  start_state = problem.getStartState()
  if(problem.isGoalState(start_state)):
    return [start_state]

  frontier = util.PriorityQueueWithFunction(f)
  # frontier.push((start_state,"South",1))
  cost = 0
  frontier.push((start_state,"",0))
  explored = []
  solution = []
  previous = {}
  while True:
    if frontier.isEmpty():
      return []

    node = frontier.pop()

    # solution.append(node[1])
    explored.append(node)
    successors = problem.getSuccessors(node[0])
    cost += 1
    for state in successors:
      if not((state in explored) or (state in heapToList(frontier.heap))):
        previous[state] = node
        if(problem.isGoalState(state[0])):
          node = state
          node1 = node
          while node1[0] != start_state:
            solution.append(node1[1])
            node1 = previous[node1]
          print("Solution",solution[::-1])
          return solution[::-1]
        frontier.push(state)
      elif (state in heapToList(frontier.heap)):
        st1 = frontier.findInHeap(state)
        if st1 != None:
          print("Difference",st1,state)                      
          if st1[1][2] < state[2]:
            frontier.delFromHeap(state)
            frontier.push(st1[1])



def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  cost = 0

  def heapToList(heap):
    l =[]
    for i in heap:
      l.append(i[1])
    return l

  def f(a):
    return cost + heuristic(a[0],problem)
       
  start_state = problem.getStartState()
  if(problem.isGoalState(start_state)):
    return [start_state]

  frontier = util.PriorityQueueWithFunction(f)
  # frontier.push((start_state,"South",1))
  frontier.push((start_state,"",cost))
  explored = []
  solution = []
  previous = {}
  while True:
    if frontier.isEmpty():
      return []
    node = frontier.pop()
    cost += 1
    if(problem.isGoalState(node[0])):      
      node1 = node
      while node1[0] != start_state:
        solution.append(node1[1])
        node1 = previous[node1]
      print("Solution",solution[::-1])
      return solution[::-1]

    explored.append(node)
    successors = problem.getSuccessors(node[0])
    

    for state in successors:
      if not((state in explored) or (state in heapToList(frontier.heap))):
        previous[state] = node
        frontier.push(state)
      elif (state in heapToList(frontier.heap)):
        st1 = frontier.findInHeap(state)
        if st1 != None:
          print("Difference",st1[0],f(state))                      
          print("cost",cost)
          if st1[0] < cost:
            frontier.delFromHeap(state)
            frontier.push(st1[1])
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
