class Matrix:
    def __init__(self, m):
        if type(m) != list or type(m[0]) != list:
            raise Exception("A matrix is a list of lists.")
        length = len(m[0])
        for array in m:
            if length != len(array):
                raise Exception("Each array in a matrix must be equal.")
        self.m = m

    def __add__(self, lhs):
        if len(self.m) != len(lhs.m) or len(self.m[0]) != len(lhs.m[0]):
            raise Exception("Matricies must be equal.")
        nrows = len(self.m)
        ncols = len(lhs.m[0])
        retval = [[0 for x in range(ncols)] for y in range(nrows)]
        for x in range(nrows):
            for y in range(ncols):
                retval[x][y] = self.m[x][y] + lhs.m[x][y]
        return retval

    def __sub__(self, lhs):
        if len(self.m) != len(lhs.m) or len(self.m[0]) != len(lhs.m[0]):
            raise Exception("Matricies must be equal.")
        nrows = len(self.m)
        ncols = len(lhs.m[0])
        retval = [[0 for x in range(ncols)] for y in range(nrows)]
        for x in range(nrows):
            for y in range(ncols):
                retval[x][y] = self.m[x][y] - lhs.m[x][y]
        return retval
        
    def __matmul__(self, o):
        if (len(self.m[0]) != len(o.m)):
            raise Exception("LHS columns (" + str(len(self.m[0])) + ") must equal RHS rows (" + str(len(o.m)) + ")")
        nrows = len(self.m)
        ncols = len(o.m[0])
        retval = [[0 for x in range(ncols)] for y in range(nrows)]
        nmax = len(o.m)
        print("nrows: " +str(nrows) + " ncols: " +str(ncols) + " nmax: " +str(nmax))
        for x in range(nrows):
            for y in range(ncols):
                for n in range(nmax):
                    retval[x][y] += self.m[x][n] * o.m[n][y]
        return retval

if __name__ == "__main__":
    try:
        ob2 = Matrix([ [1, 2, 3] ])
        ob1 = Matrix([ [4], [5], [6] ])
        print(ob1 @ ob2)
        print(ob1 + ob2)
        print(ob1 - ob2)
    except Exception as inst:
        print(inst)
