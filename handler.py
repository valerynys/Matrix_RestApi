import numpy as np

async def multiply_matrices(matrix1: list[list[float]], matrix2: list[list[float]]):
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    result = matrix1.dot(matrix2)
    return {"result": result.tolist()}
