class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, delta):  # i is 1-based
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix(self, i):  # sum of 1..i
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_sum(self, l, r):
        return self.prefix(r) - self.prefix(l - 1)