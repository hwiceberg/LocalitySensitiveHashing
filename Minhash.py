# minhash
import random
import sys

BIG_PRIME = 2147483647
class Minhash:
    def __init__(self, k):
        self.k = k
        # generate k hash functions (pair-wise independant)
        self.hash_funcs = [self.gen_hash_function() for i in range(k)]

    def random_parameter(self):
        return random.randrange(0, BIG_PRIME - 1)

    def gen_hash_function(self):
        a, b = self.random_parameter(), self.random_parameter()
        return lambda x: (a * x + b) % BIG_PRIME

    def cal(self, words):
        mh = [sys.maxint for i in range(self.k)]
        for i in range(self.k):
            for word in words:
                mh[i] = min(mh[i], self.hash_funcs[i](word))
        return mh