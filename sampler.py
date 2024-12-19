import numpy as np
import random
from polymer import Polymer
from tqdm import tqdm

directions = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])

class Sampler:
    def __init__(self, plm: Polymer,T):
        self.plm = plm
        self.T=T
        self.factor=np.exp(-1/self.T)
    
    def step(self):
        i = random.randint(0, self.plm.N - 1)
        new_pos = self.plm.config[i] + directions[random.randint(0, 5)]
        if new_pos[2] < 0:
            return

        bonds = self.plm.config[i-1:i+2]-new_pos
        lengths_sqared=(bonds**2).sum(axis=1).astype(int)
        if not np.all(np.logical_or(lengths_sqared==1,lengths_sqared==2,lengths_sqared==3)):
            return

        if self.plm.occupied(new_pos):
            return
        
        if new_pos[2] == 0:
            if self.plm.config[i,2]>0:
                delta_E=-1
            else:
                delta_E=0
        else:
            if self.plm.config[i,2]>0:
                delta_E=0
            else:
                delta_E=1

        if delta_E>0 and random.random()>self.factor:
            return

        self.plm.set_point(i, new_pos, delta_E)
        return

    
    def MC_step(self):
        for i in tqdm(range(self.plm.N),desc=f"MC_step",leave=False,position=1):
            self.step()