import numpy as np 
#RL environment
class gridworld:
    def __init__(self, dims, goal_states, error_states):
        # for actions
        self.actions = ["up", "down", "right", "left"]
        self.action_map = {"up": 0, "down":1, "right": 2, "left": 3}
        self.movement = [[-1,0], [1,0], [0,1], [0,-1]]	

        # for states
        self.rows = dims[0]
        self.columns = dims[1]
        self.current_state = None
        self.error_states = error_states 
        self.goal_states = goal_states
        self.empty_states =  [(i, j) for i in range(self.rows) for j in range(self.columns) if (i, j) not in (self.goal_states + self.error_states)]

        # visual representation of gridworld
        self.grid = np.array([["." for i in range(self.columns)] for j in range(self.rows)])
        for g in self.goal_states:
            self.grid[g] = "O"
        for e in self.error_states:
            self.grid[e] = "X"

    #print gridworld
    def print_grid(self):
        print("Grid World:")				
        print(self.grid)

    #set current state to start state
    def reset(self, start_state = None):
        if start_state != None:
             self.current_state = start_state
        else:
            self.current_state =  self.empty_states[np.random.choice(len(self.empty_states))]
        return self.current_state

    def step(self, action): 
        action_index = action
        action_taken = self.actions[action]  
        
        new_state, reward  = (-1, -1), 0 
        
        # out of the board , no movement but -reward for taking action
        if (action_taken == "up" and self.current_state[0] == 0) or (action_taken == "down" and self.current_state[0] == self.rows-1) :
            raise Exception("Invalid action taken")
        elif (action_taken == "left" and self.current_state[1] == 0) or (action_taken == "right" and self.current_state[1] == self.columns-1) :
            raise Exception("Invalid action taken")

        # inside the board
        else:
            new_state = (self.current_state[0] + self.movement[action_index][0] , self.current_state[1] + self.movement[action_index][1])
            if new_state in self.empty_states: # no reward in empty states 
                reward = -1
            elif new_state in self.goal_states: # good state
                reward = 10
            elif new_state in self.error_states: # bad state
                reward = -5 

        # current state changes because of taking action 
        self.current_state = new_state  

        #return current state, reward 
        return self.current_state, reward


class Solution:
    def __init__(self, env, gamma=0.9, epsilon=0.1, maxIter=5000, maxTimesteps = 100):
        self.q_table = {}
        self.env = env
        self.gamma, self.epsilon, self.maxIter, self.maxTimesteps = gamma, epsilon, maxIter, maxTimesteps

        ####### You may add extra functions/ variables in this class
    
    def get_next(self,state,q_table):
        temp_a = []
        temp_v =[]
        for i in  range (4):    
            action_taken = self.env.actions[i]  
            if (action_taken == "up" and state[0] == 0) or (action_taken == "down" and state[0] == self.env.rows-1) :
                continue
            elif (action_taken == "left" and state[1] == 0) or (action_taken == "right" and state[1] == self.env.columns-1) :
                continue
            else:
                temp_v.append(q_table[state[0] ,state[1], i])
                temp_a.append(i)
        return temp_v,temp_a
    
    def get_max(self,p_value,p_action):
        max_value = max(p_value)
        i = p_value.index(max_value) 
        action = p_action[i]
        return action

    def greedy(self,next_state,q_table):
        #list of valid action and Q value
        list_v,list_a = self.get_next(next_state,q_table)

        #greedy action with max Q value
        g_action = self.get_max(list_v,list_a)
        return g_action
        
    def e_greedy(self,state,q_table):
        n_value,n_action = self.get_next(state,q_table)
        p = np.random.uniform(0,1)
        #print("P",p)
        if p < self.epsilon:
            nxt_action = np.random.choice(n_action)
    
        else:
            nxt_action = self.get_max(n_value,n_action)
        #print(nxt_action)
        return nxt_action

    # Define the Q-learning algorithm
    def q_learning(self):
        q_table = np.zeros((self.env.rows, self.env.columns, len(self.env.actions)))
        
        for iter in range(self.maxIter):
            
            state = self.env.reset()
            visit_n = np.zeros((self.env.rows, self.env.columns, len(self.env.actions)))
            ########## Complete this function #######
            for iter in range(self.maxTimesteps):
                
                #choose epsilon greedy action for current state
                Action = self.e_greedy(state,q_table)
                next_state, reward = self.env.step(Action)

                # to calculate alpha for each iteration , alpha = 1 / visit_n(s, a)
                # visit_n = {}
                visit_n[state[0],state[1], Action] = visit_n[state[0],state[1], Action] + 1 
                alpha = 1 / visit_n[state[0],state[1], Action]

                #choose greedy action for next_state
                a = self.greedy(next_state,q_table)

                #calculate and update Q(S,A)
                Q = q_table[state[0] ,state[1], Action]
                Q_next = q_table[next_state[0] ,next_state[1], a]
                TD = reward + self.gamma*Q_next - Q 
                Q = Q + alpha * TD
                q_table[state[0] ,state[1], Action] = Q

                #update current state
                state = next_state
                # print(state,Action)
                
            #############################

        return q_table 


if __name__ == "__main__":
    np.random.seed(100)

    size = 3
    goal_states = [(0, size-1), (1, size-1), (size-1, 0)] 
    error_states = [(o, o) for o in range(size)] 
    grid = gridworld((size, size), goal_states, error_states)

    grid.print_grid()
    solution = Solution(grid)
    q_table = solution.q_learning()

    print("Q-table:")
    print(q_table)

    assert round(q_table[0,0,1], 5)== 75.5 and round(q_table[0,1,2], 5)==100.0, 'wrong answer'