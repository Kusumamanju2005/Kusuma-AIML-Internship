import requests

url = "http://127.0.0.1:5001/invocations"

payload = {
    "dataframe_records": [
        {
            "sepal length (cm)": 5.1,
            "sepal width (cm)": 3.5,
            "petal length (cm)": 1.4,
            "petal width (cm)": 0.2
        }
    ]
}

response = requests.post(
    url,
    json=payload,
    timeout=30
)

print("========== REST API TEST ==========")
print("Status Code:", response.status_code)
print("Response:", response.text)

if response.status_code == 200:
    print("REST API prediction successful!")
else:
    print("REST API request failed.")