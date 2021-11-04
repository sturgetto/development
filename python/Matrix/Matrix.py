'''

This is a class to handle Matrix manipulation. Addition, subtraction, dot
product, and division.

'''

class Matrix:
    def __init__(self, matrix):
        if type(matrix) != list or type(matrix[0]) != list:
            raise Exception("A matrix is a list of lists.")
        length = len(matrix[0])
        for array in matrix:
            if length != len(array):
                raise Exception("Each array in a matrix must be equal.")
        self.matrix = matrix

    def __add__(self, rhs):
        if len(self.matrix) != len(rhs.matrix) or \
           len(self.matrix[0]) != len(rhs.matrix[0]):
            raise Exception("Matricies must be equal.")
        nrows = len(self.matrix)
        ncols = len(rhs.matrix[0])
        retval = [[0 for x in range(ncols)] for y in range(nrows)]
        for x in range(nrows):
            for y in range(ncols):
                retval[x][y] = self.matrix[x][y] + rhs.matrix[x][y]
        return retval

    def __sub__(self, rhs):
        if len(self.matrix) != len(rhs.matrix) or \
           len(self.matrix[0]) != len(rhs.matrix[0]):
            raise Exception("Matricies must be equal.")
        nrows = len(self.matrix)
        ncols = len(rhs.matrix[0])
        retval = [[0 for x in range(ncols)] for y in range(nrows)]
        for x in range(nrows):
            for y in range(ncols):
                retval[x][y] = self.matrix[x][y] - rhs.matrix[x][y]
        return retval
        
    def __matmul__(self, rhs):
        if (len(self.matrix[0]) != len(rhs.matrix)):
            raise Exception("LHS columns (" + str(len(self.matrix[0])) + \
                  ") must equal RHS rows (" + str(len(rhs.matrix)) + ")")
        nrows = len(self.matrix)
        ncols = len(rhs.matrix[0])
        retval = [[0 for x in range(ncols)] for y in range(nrows)]
        nmax = len(rhs.matrix)
        for x in range(nrows):
            for y in range(ncols):
                for n in range(nmax):
                    retval[x][y] += self.matrix[x][n] * rhs.matrix[n][y]
        return retval

    def __truediv__(self, rhs):
        raise Exception("True division not supported.")

if __name__ == "__main__":
    try:
        ob2 = Matrix([ [1, 2, 3] ])
        ob1 = Matrix([ [4], [5], [6] ])
        print(ob1 @ ob2)
        print(ob1 / ob2)
        ob1 = Matrix([ [1, 2, 3] ])
        ob2 = Matrix([ [4, 5, 6] ])
        print(ob1 + ob2)
        print(ob1 - ob2)
    except Exception as inst:
        print(inst)
