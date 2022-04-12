class FSM:
    def __init__(self,actual):
        self.game = actual.game
        self.stateStack = []

    def pop(self):
        return self.Stack.pop()

    def push(self, state):
        self.Stack.append(state)

    def update(self):
        actual = self.Stack[len(self.Stack) - 1]





