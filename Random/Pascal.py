class pascal:
    def getRow(self, rowIndex: int):
        l = []
        for i in range(rowIndex + 1):
            l.append(self.binomcoeff(rowIndex, i))

    def binomcoeff(self, n, k):
        res = 1
        if (k > n - k):
            k = n - k
        for i in range(k):
            res = res * (n - i)
            res = res // (i + 1)
        return res
