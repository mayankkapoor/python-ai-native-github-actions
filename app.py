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

@app.route("/factors/<int:number>")
def factors(number):
    """Find all factors of a given number."""
    if number <= 0:
        return jsonify({"error": "Please provide a positive number"}), 400
        
    factors_list = [i for i in range(1, number + 1) if number % i == 0]
    return jsonify({
        "number": number,
        "factors": factors_list,
        "count": len(factors_list)
    })

if __name__ == "__main__":
    app.run(debug=True)