from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/calculate/<int:number>")
def calculate(number):
    """Calculate the square and cube of a number."""
    return jsonify({
        "number": number,
        "square": number ** 2,
        "cube": number ** 3
    })

if __name__ == "__main__":
    app.run(debug=True)