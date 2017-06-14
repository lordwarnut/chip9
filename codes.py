import numpy as np
class CodeGen:
    class MEM:
        @staticmethod
        def mem_to_reg(NNNN, vX):
            return [0x2000 + vX % 16, NNNN % 65536]

        @staticmethod
        def reg_to_mem(vX, NNNN):
            return [0x2100 + vX % 16, NNNN % 65536]

        @staticmethod
        def memx_to_reg(vX, vY):
            return [0x2200 + ((vX % 16) << 4) + vY]

        @staticmethod
        def reg_to_memx(vX, vY):
            return [0x2300 + ((vX % 16) << 4) + vY]

        @staticmethod
        def data(NNNN):
            return [NNNN % 65536]
    class IO:
        @staticmethod
        def int_print():
            pass