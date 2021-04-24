class Matrix:
    def __init__(self, mx1):
        self.mx1 = mx1

    def __str__(self):
        res_list = [' '.join([f'{j:02}' for j in i]) for i in self.mx1]
        res_str = '\n'.join(res_list)
        return f'{res_str}'

    def __add__(self, other):
        res = []
        for i in range(len(self.mx1)):
            res.append([x + y for x, y in zip(self.mx1[i], other.mx1[i])])
        return Matrix(res)


matrix_1 = Matrix([[5, 1, 2], [10, 2, 6], [9, 12, 1]])
matrix_2 = Matrix([[2, 5, 11], [10, 1, 4], [1, 1, 21]])
print(matrix_1 + matrix_2)
