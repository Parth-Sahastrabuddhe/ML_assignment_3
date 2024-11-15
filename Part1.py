import numpy as np
import matplotlib.pyplot as plt
import random

class GridMDP:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.state = [(i,j) for i in range(grid_size) for j in range(grid_size)]
        self.action = ['up', 'down', 'right', 'left']
        self.num_actions = len(self.action)

        self.reward = np.zeros((grid_size, grid_size))
        self.reward[4, 4] = +10
        self.reward[1, 1] = -5
        self.reward[1, 3] = -5
        self.reward[3, 1] = -5
        self.reward[2, 3] = +5

        self.reset()

    def reset(self):
        self.agent = [0, 0]
        return tuple(self.agent)
    
    def step(self, action):
        if action == 'up':
            self.agent[0] = max(0, self.agent[0] - 1)
        elif action == 'down':
            self.agent[0] = min(self.grid_size - 1, self.agent[0] + 1)
        elif action == 'left':
            self.agent[1] = max(0, self.agent[1] - 1)
        elif action == 'right':
            self.agent[1] = min(self.grid_size - 1, self.agent[1] + 1)
        else:
            raise ValueError('Invalid action')

        reward = self.reward[self.agent[0], self.agent[1]]
        end = (self.agent == [4, 4])

        return tuple(self.agent), reward, end
    
    def visual(self):
        grid = np.full((self.grid_size, self.grid_size), ' ')
        grid[4, 4] = 'G'
        grid[1, 1] = 'P'
        grid[1, 3] = 'P'
        grid[3, 1] = 'P'
        grid[2, 3] = 'IR'
        grid[self.agent[0], self.agent[1]] = 'A'

        plt.figure(figsize=(5,5))
        plt.imshow(grid == 'A', cmap='Blues', interpolation='nearest')
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                text = 'A' if grid[i, j] == 'A' else grid[i, j]
                plt.text(j, i, text, ha="center", va="center")

        plt.grid(visible=True, color='black', linewidth=0.5)
        plt.xticks(np.arange(-0.5, self.grid_size, 1), [])
        plt.yticks(np.arange(-0.5, self.grid_size, 1), [])
        plt.gca().set_xticks(np.arange(-0.5, self.grid_size, 1), minor=True)
        plt.gca().set_yticks(np.arange(-0.5, self.grid_size, 1), minor=True)
        plt.gca().grid(which='minor', color='black', linewidth=0.5)
        plt.xticks([])
        plt.yticks([])
        plt.title("Grid world MDP")
        plt.show()

if __name__ == "__main__":
    env = GridMDP()
    state = env.reset()
    print('Initial state:', state)
    env.visual()
    for step in range(15):
        while True:
            action = input("Enter an action (up, down, left, right): ")
            if action in ['up', 'down', 'left', 'right']:
                break

        next_state, reward, end = env.step(action)
        print(f"step {step+1}: Action = {action}, state = {next_state}, reward = {reward}, end = {end}")
        env.visual()
        if end:
            print("Goal reached!")
            break