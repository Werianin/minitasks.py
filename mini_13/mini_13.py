import matrix_power

matrix = [[1.0, 2.0], [3.0, 4.0]]


assert matrix_power.foreign_matrix_power(matrix, 3) == [[37.0, 54.0],
                                                        [81.0, 118.0]]
# [[37.0, 54.0],
#  [81.0, 118.0]]

assert matrix_power.foreign_matrix_power(matrix, 10) == [[4783807.0, 6972050.0],
                                                         [10458075.0, 15241882.0]]
# [[4783807.0, 6972050.0],
#  [10458075.0, 15241882.0]]
