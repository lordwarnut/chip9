import core
import random
from codes import CodeGen as C
import numpy as np

c = core.Core()

ins = []
ins += C.MEM.memx_to_reg(0x0, 0x1)
ins += C.MEM.reg_to_memx(0x2, 0x3)
c.mem.place(ins)
c.mem.reg[0] = 0x0001
c.mem.reg[2] = 0xf0e1
c.mem.reg[3] = 0x0002

print('mem', ("{:04x} " * 8).format(*c.mem.mem[:8]))
print('reg', ("{:04x} " * 8).format(*c.mem.reg[:8]))
print()

c.step()
print('mem', ("{:04x} " * 8).format(*c.mem.mem[:8]))
print('reg', ("{:04x} " * 8).format(*c.mem.reg[:8]))
print()

c.step()
print('mem', ("{:04x} " * 8).format(*c.mem.mem[:8]))
print('reg', ("{:04x} " * 8).format(*c.mem.reg[:8]))