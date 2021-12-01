class FenwickTree:

    def __init__(self, arr):
        self.tree = [0 for _ in range(len(arr) + 1)]

        for i in range(len(arr)):
            self.add(i, arr[i])

    def sum(self, k):
        psum = 0
        k += 1

        while k >= 1:
            psum += self.tree[k]
            k -= (k & -k)

        return psum

    def add(self, k, delta):
        k += 1

        while k < len(self.tree):
            self.tree[k] += delta
            k += (k & -k)


ft = FenwickTree([1, 3, 4, 8, 6, 1, 4, 2])
print(ft.tree)
print(ft.sum(7))
