import core
import random
import numpy as np

c = core.Core()
c.mem.mem[0] = np.uint16(0x1100)
c.mem.reg[0] = np.uint16(0x0042)
c.step()