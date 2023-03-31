import unittest
from my_module import multiply_matrices

class TestMultiplyMatrices(unittest.TestCase):
    def test_multiply_matrices(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = {"result": [[19, 22], [43, 50]]}
        result = await multiply_matrices(matrix1, matrix2)
        self.assertEqual(result, expected_result)
