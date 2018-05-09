from search import Problem


def is_valid(state):
    missionaryLeft, cannibalLeft, boat, missionaryRight, cannibalRight = state

    if (missionaryLeft >=0 and missionaryRight >=0):
        return True
    elif (cannibalLeft >= 0 and cannibalRight >= 0):
        return True
    elif (missionaryLeft >= 0 or missionaryLeft >= cannibalLeft):
        return True
    elif (missionaryRight >= 0 or missionaryRight >= cannibalRight):
        return True
    else:
        return False


class VCL(Problem):
    def result(self,state,action):
        return action
    def value(self,state):
        pass

    def __init__(self, initial, goal):
        self.goal = goal
        self.initial = initial
        Problem.__init__(self, self.initial, self.goal)

    def __repr__(self):
        return "< State (%s, %s) >" % (self.initial, self.goal)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        actions = []
        if state[2] == 'S':
            new_state = (state[0],state[1]-2 , 'D',state[3],state[4]+2)
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (state[0]-2, state[1], 'D', state[3]+2, state[4])
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (state[0]-1, state[1]-1, 'D', state[3]+1,  state[4]+1)
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (state[0], state[1]-1, 'D',state[3], state[4]+1)
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (state[0]-1, state[1], 'D', state[3]+1, state[4])
            if is_valid(new_state):
                actions.append(new_state)

        else:

            new_state = (state[0],state[1]+2, 'S',state[3], state[4]-2)
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (state[0]+2, state[1], 'S', state[3]-2, state[4])
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (state[0]+1, state[1]+1, 'S', state[3]-1, state[4]-1)
            if is_valid(new_state):
                actions.append(new_state)

            new_state =(state[0], state[1]+1, 'S',state[3], state[4]-1)
            if is_valid(new_state):
                actions.append(new_state)

            new_state =(state[0]+1, state[1], 'S', state[3]-1,state[4])
            if is_valid(new_state):
                actions.append(new_state)



        return actions