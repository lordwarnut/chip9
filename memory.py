import numpy as np

class Memory():
    def __init__(self):
        self.mem = np.zeros(2**16, dtype=np.uint16)
        self.reg = np.zeros(16   , dtype=np.uint16)
        self.acc = np.uint(0)



