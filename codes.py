class CodeGen:
    class Data:
        @staticmethod
        def MEMTOACC(vX):
            return 0x2000 + vX

        @staticmethod
        def ACCTOMEM(vX):
            return 0x2100 + vX


        @staticmethod
        def MEMTOREG(add, vY):
            return 0x2300 + add << 4 + vY

        @staticmethod
        def REGTOMEM(vX, add):
            return 0x2400 + vX << 4 + add


        @staticmethod
        def ACCTOREG(vX):
            return 0x2500 + vX

        @staticmethod
        def REGTOACC(vX):
            return 0x2600 + vX


        @staticmethod
        def REGTOREG(vX, vY):
            0x2700 + + vX << 4 + vY

        @staticmethod
        def MEMTOMEM(add1, vY):
            0x2800 + + vX << 4 + vY

    class IO:
        @staticmethod
        def INTPRINT():