import numpy as np

class Memory():
    def __init__(self):
        self.mem = np.zeros(2**16, dtype=np.uint16)
        self.reg = np.zeros(16   , dtype=np.uint16)

    def place(self, m):
        for i in range(len(m) % 65536):
            self.mem[i] = m[i]



