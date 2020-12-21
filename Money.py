from Pair.Pair import Pair


class Money(Pair):

    def __init__(self, a, b, max):
        super().__init__(a, b)
        self._max = max

    def get_max(self):
        return self._max

    def add(self, a = 0, b = 0):
        self._b += b
        self._a += a + self._b // self._max
        self._b %= self._max

    def subtract(self, a = 0, b = 0):
        self._b -= b
        self._a -= a - abs(self._b // self._max)
        self._b %= self._max
