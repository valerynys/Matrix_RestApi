from fastapi import FastAPI
from handler import multiply_matrices

app = FastAPI()

@app.post("/multiply")
async def multiply_matrices_handler(matrix1: list[list[float]], matrix2: list[list[float]]):
    return await multiply_matrices(matrix1, matrix2)


'''
{
    "matrix1": [[1.0, 2.0], [3.0, 4.0]],
    "matrix2": [[5.0, 6.0], [7.0, 8.0]]
}
{
    "matrix1": [[1.0, 2.0], [3.0, 4.0]],
    "matrix2": [[5.0, 6.0], [7.0, 8.0]]
}

curl --header "Content-Type: application/json" --request POST --data '{"matrix1": [[1.0, 2.0], [3.0, 4.0]], "matrix2": [[5.0, 6.0], [7.0, 8.0]]}' http://localhost:8000/multiply
'''