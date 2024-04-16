# Reinforcement Learning


## Overview

### Problem 1
A maze runner agent is trapped in a rectangular maze built up of walls. It needs to navigate the maze in
order to reach goal state(s). The agent can take any one of the four actions among lef t, right ,up, down
at every time step. Depending on the action taken, agent will move to the corresponding cell or will stay
in the same cell if it collides with the walls. There are several doors in the maze that can open only with
a lockpick. The agent also has a lockpick of infinite uses but is not an expert in lock-picking. If it tries to
lockpick a door, there is only a certain probability that it will succeed and will move to the other side of
the door, otherwise, it will stay in the same cell. The doors are 2-way. i.e., they can open from both sides.
The agent incurs a penalty of 1 unit for each time step that it spends in the maze except when in a terminal
state(s) where it gets a finite positive reward. Once the agent reaches the goal state, it stays in the same
state and keeps on getting the positive reward. The agent has only a fixed amount of time horizonLength
units to traverse the maze

- Goal: calculate the optimal reward that the agent can get in N steps from given initial cell of the maze.
| ![](https://github.com/RahulBoipai/Reinforcement_Learning/blob/main/pics/maze.png) |

#### Implementation detail
Implement the function `optimalReward()` that takes current state s and time-step
k and returns maximum reward that the agent can receive in horizonLength time-steps starting from kth
time-step in state s using `dynamic-programming`. 0 ≤k < horizonLength.
An agent can take one of the actions from actionSpace = [left, right, up, down].
takeAction() function from Maze class takes as input current state : tuple (i, j) and action a; i,j being the
current cell indices and a ∈actionSpace and returns list of lists of the form [next state, probability,reward].
For example, in the given maze, takeAction((1, 5), lef t) will return [[(1, 4), p, −1], [(1, 5), 1 −p, −1]].


### Problem 2
A Treasure Hunter agent is trapped in an m×n island from which it cannot escape. Its task is to dig for
buried treasures that are spread across different locations on the island. The island also contains several
traps which always incur damage to the agent whenever visited. At any location on the island (indicated by
a cell), the agent can take possible actions among left, right, up, and down, but not all actions are valid in
every cell, i.e., if the agent tries to go outside the island, it is considered as an invalid action. On visiting a
cell, the agent tries to dig for a possible treasure which causes a small digging cost. If the agent finds the
buried treasure, it earns a positive reward, whereas if the cell turns out to be a trap, it receives a negative
reward. The cells containing treasure are assumed to have an infinite amount of buried treasure.


- Goal: Implement the Q-Learning algorithm for the above problem

| ![](https://github.com/RahulBoipai/Reinforcement_Learning/blob/main/pics/goal_grid.png) |

### Implementation detail
Your task is to implement the function `q learning()` that returns a numpy array Q Table in which
Q Table[ rowIndex, colIndex, actionIndex ] is Q-value of state ( rowIndex, colIndex ) and the action corre-
sponding to the state’s valid action actionIndex.
The function reset() of Environment Class initializes the start state of the agent in the given Environment.
The function step() of Environment Class takes as an input an action index ( up : 0,down : 1,right :
2,left : 3) that can be taken in the current state and returns the next state and its corresponding reward.
Invalid Actions that will take the agent out of the Environment has to be taken care of while implementing
Q Learning.
Implement step size α as follows: At the nth iteration, V isit n(s,a) is the number
of times the state action pair (s,a) is seen. So the step size α = 1/V isit n(s,a).


## Results
Output
- Maze Runner Agent: 
```
================================================
 Horizon Length:  1
 Optimal Reward:  -1.0
================================================
 Horizon Length:  2
 Optimal Reward:  -2.0
================================================
 Horizon Length:  3
 Optimal Reward:  8.0
================================================
 Horizon Length:  4
 Optimal Reward:  18.0
================================================
 Horizon Length:  5
 Optimal Reward:  28.0
================================================
```

- Tresure Hunter Agent
```
Grid World:
[['X' '.' 'O']
 ['.' 'X' 'O']
 ['O' '.' 'X']]
Q-table:
[[[  0.    75.5   89.     0.  ]
  [  0.    85.   100.    75.1 ]
  [  0.   100.     0.    89.  ]]

 [[ 75.1   77.95  85.     0.  ]
  [ 89.    75.5  100.    75.5 ]
  [100.    85.     0.    85.  ]]

 [[ 75.5    0.    75.5    0.  ]
  [ 85.     0.    85.    77.95]
  [100.     0.     0.    75.5 ]]]
```




