import memory
import numpy as np

class Core:
    def __init__(self):
        self.mem = memory.Memory()
        self.pc = np.uint16(0)
        self.running = True

    def incer_getter(self):
        NNNN = self.mem.mem[self.pc]
        self.pc += 1
        return NNNN

    def step(self):
        currCell = self.incer_getter()
        ins = [(0xf000 & currCell) >> 12,
               (0x0f00 & currCell) >> 8,
               (0x00f0 & currCell) >> 4,
               (0x000f & currCell) >> 0,]

        if ins[0] == 0x1:
            if ins[1] == 0x0:
                self._print_int(ins[3])
            if ins[1] == 0x1:
                self._print_char(chr(ins[2] << 4 + ins[3]))

        if ins[0] == 0x2:
            if ins[1] == 0x0:
                self._mem_to_reg(self.incer_getter(), ins[3] )
            if ins[1] == 0x1:
                self._reg_to_mem(ins[3], self.incer_getter())
            if ins[1] == 0x2:
                self._memx_to_reg(ins[2], ins[3])
            if ins[1] == 0x3:
                self._reg_to_memx(ins[2], ins[3])

    def _add(self, vX):
        self.mem.acc += self.mem.reg[vX]

    def _sub(self, vX):
        self.mem.acc -= self.mem.reg[vX]


    def _print_int(self, vX):
        print(self.mem.reg[vX])

    def _print_char(self, vX):
        print(chr(self.mem.reg[vX]))


    def _mem_to_reg(self, NNNN, vX):
        self.mem.reg[vX] = self.mem.mem[NNNN]

    def _reg_to_mem(self, vX, NNNN):
        self.mem.mem[NNNN] = self.mem.reg[vX]

    def _memx_to_reg(self, vX, vY):
        self.mem.reg[vX] = self.mem.mem[self.mem.reg[vY]]

    def _reg_to_memx(self, vX, vY):
        self.mem.mem[self.mem.reg[vX]] = self.mem.reg[vY]