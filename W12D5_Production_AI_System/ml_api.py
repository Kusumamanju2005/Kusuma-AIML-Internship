from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

iris = load_iris()

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(iris.data, iris.target)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]

    prediction = model.predict([features])

    return jsonify({
        "prediction": int(prediction[0])
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
