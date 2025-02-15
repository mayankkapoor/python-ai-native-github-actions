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

@app.route("/isprime/<int:number>")
def is_prime(number):
    """Check if a given number is prime."""
    if number <= 1:
        return jsonify({"error": "Please provide a number greater than 1"}), 400
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return jsonify({
                "number": number,
                "is_prime": False,
                "first_divisor": i
            })
    
    return jsonify({
        "number": number,
        "is_prime": True
    })

if __name__ == "__main__":
    app.run(debug=True)