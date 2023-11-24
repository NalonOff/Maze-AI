import pygame as pg

class AI:
    def __init__(self, environment) -> None:
        self.image = pg.transform.scale2x(pg.image.load('assets\\textures\\player.png'))
        self.pos = [32, 0]
        self.trail = []

        self.learningRate = 0.001
        self.trainable = False
        self.eps = 0.99
        self.history = []
        self.valueFunction = {}

        s = 1
        for i in environment:
            for _ in range(1, len(i) + 1):
                self.valueFunction[s] = 0.
                s += 1

    def greedy_step(self, state):
        actions = ['up', 'left', 'down', 'right']
        vmin = None
        vi = None
        for i in range(0, 4):
            a = actions[i]





    def play(self, state):
        # Play given the @state (int)
        if self.is_human is False:
            # Take random action
            if random.uniform(0, 1) < self.eps:
                action = randint(1, 3)
            else: # Or greedy action
                action = self.greedy_step(state)
        else:
            action = int(input("$>"))
        return action

    def add_transition(self, n_tuple):
        # Add one transition to the history: tuple (s, a , r, s')
        self.history.append(n_tuple)
        s, a, r, sp = n_tuple
        self.rewards.append(r)

    def train(self):
        if not self.trainable or self.is_human is True:
            return

        # Update the value function
        for transition in reversed(self.history):
            s, a, r, sp = transition
            if r == 0:
                self.V[s] = self.V[s] + 0.001*(self.V[sp] - self.V[s])
            else:
                self.V[s] = self.V[s] + 0.001*(r - self.V[s])

        self.history = []