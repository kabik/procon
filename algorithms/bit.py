# BIT: https://algo-logic.info/binary-indexed-tree/#toc_id_1_1

class BIT:
    def __init__(self, size):
        self.val = [0]*(size+1)
        self.size = size+1

    def add(self, i, x):
        while i < self.size:
            self.val[i] += x
            i += i & -i

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.val[i]
            i -= i & -i
        return ret

    def debug(self):
        print(self.val)
