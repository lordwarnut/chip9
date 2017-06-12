import memory
import numpy as np

class Core:
    def __init__(self):
        self.mem = memory.Memory()
        self.pc = np.uint16(0)

    def step(self):
        currCell = self.mem.mem[self.pc]
        ins = [(0xf000 & currCell) >> 12,
               (0x0f00 & currCell) >> 8,
               (0x00f0 & currCell) >> 4,
               (0x000f & currCell) >> 0,]

        if ins[0] == 0x1:
            if ins[1] == 0x0:
                self._print_int(ins[3])
            if ins[1] == 0x1:
                self._print_char(chr(ins[2] << 4 + ins[3]))

        #print(hex(currCell), list(hex(i) for i in ins))


    def _add(self, vX):
        self.mem.acc += self.mem.reg[vX]

    def _sub(self, vX):
        self.mem.acc -= self.mem.reg[vX]

    def _print_int(self, vX):
        print(self.mem.reg[vX])

    def _print_char(self, vX):
        print(chr(self.mem.reg[vX]))