import numpy as np
from matplotlib import pyplot as plt
import random

directions = np.array(
    [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
)


class Polymer:
    def __init__(self, N):
        self.N = N
        self.config = np.zeros((N, 3),dtype=np.int32)
        self.E = 0.0
        self._initialize_saw()

    def set_point(self, index, point, delta_E:None):
        if delta_E is None:
            if point[2] == 0:
                if self.config[index,2]>0:
                    delta_E=-1
                else:
                    delta_E=0
            else:
                if self.config[index,2]>0:
                    delta_E=0
                else:
                    delta_E=1
        self.E += delta_E
        self.config[index] = point
    
    def _initialize_saw(self):
        success = False
        while not success:
            success = True
            self.config[0] = np.array([0, 0, 0])
            self.E = -1

            for i in range(1, self.N):
                valid_moves = []
                for move in directions:
                    new_position = self.config[i - 1] + move
                    if new_position[2] >= 0 and not np.any(
                        np.all(new_position == self.config[:i], axis=1)
                    ):
                        valid_moves.append(new_position)

                if not valid_moves:
                    success = False
                    break

                self.config[i] = random.choice(valid_moves)
                if self.config[i][2] == 0:
                    self.E -= 1

    def occupied(self, position):
        left = self.config[self.config[:, 0] == position[0]]
        left = left[left[:, 1] == position[1]]
        left = left[left[:, 2] == position[2]]
        return left.size>0

    def visualize(self):
        x, y, z = self.config[:, 0], self.config[:, 1], self.config[:, 2]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(x, y, z, marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()

    def r2Gyration(self):
        cop = np.mean(self.config, axis=0)
        return ((self.config-cop)**2).sum()/self.N

