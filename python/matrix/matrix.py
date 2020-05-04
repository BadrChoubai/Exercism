class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self.generate_matrix(matrix_string) 

    def row(self, index: int) -> [int]:
        return self.matrix[index-1]

    def column(self, index: int) -> [int]:
        return [row[index-1] for row in self.matrix]

    @staticmethod
    def generate_matrix(matrix_string) -> list:
        return [[int(x) for x in line.split(' ')] for line in matrix_string.splitlines()] 

