# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    cur=problem.getStartState()
    closed=set()
    frontier=util.Stack() #栈结构存放待扩展节点
    frontier.push((cur,[])) #第一位存储节点状态，第二位存储路径
    while not frontier.isEmpty():
        cur,path=frontier.pop()
        if problem.isGoalState(cur): #命中，返回路径
            return path
        if cur not in closed: #避免重复扩展结点
            closed.add(cur)
            for child in problem.getSuccessors(cur):
                if child[0] not in closed: #将所有未扩展子节点放入栈
                    frontier.push((child[0],path+[child[1]]))


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    cur=problem.getStartState()
    closed=set()
    frontier=util.Queue() #用队列存储待扩展节点
    frontier.push((cur,[])) #第一位存储节点状态，第二位存储路径
    while not frontier.isEmpty():
        cur,path=frontier.pop()
        if problem.isGoalState(cur): #命中，返回路径
            return path
        if cur not in closed: #避免重复扩展节点
            closed.add(cur)
            for child in problem.getSuccessors(cur):
                if child[0] not in closed: #将所有未扩展子节点放入队列
                    frontier.push((child[0],path+[child[1]]))


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    cur={"state":problem.getStartState(),"path":[],"cost":0} #第一位存储节点状态，第二位存储路径，第三位存储代价
    closed=set()
    frontier=util.PriorityQueue() #使用优先队列存储待扩展节点，优先取出代价小的节点
    frontier.update(cur,cur["cost"]+heuristic(cur["state"],problem))
    while not frontier.isEmpty():
        cur=frontier.pop()
        if problem.isGoalState(cur["state"]):
            return cur["path"]
        if cur["state"] not in closed: #避免重复扩展节点
            closed.add(cur["state"])
            for child in problem.getSuccessors(cur["state"]):
                if child[0] not in closed:
                    frontier.update({"state":child[0],"path":cur["path"]+[child[1]],"cost":cur["cost"]+child[2]},
                                    cur["cost"]+child[2]+heuristic(child[0],problem)) #子节点的代价为父节点的代价、动作代价、启发函数值之和




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
