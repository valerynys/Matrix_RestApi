import requests

url = "http://localhost:8000/multiply"
data = {
    "matrix1": [[1, 2], [3, 4]],
    "matrix2": [[5, 6], [7, 8]]
}
response = requests.post(url, json=data)
print(response.json())
