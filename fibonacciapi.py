from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/fibonacci/<int:x>')
def fibonacci(x):
    n1, n2 = 0, 1
    count = 0
    while count < x:
            print(n1)
            n = n1 + n2
            n1 = n2
            n2 = n
            count += 1
    if x <= 0:
        print("Please enter a positive number.")
        result = {
            "Fibonacci": False,
            "Number": x,
            "Server IP": "123.234.253.23",
        }
    elif x == 1:
        print("Fibonacci sequence is:")
        print(n1)
        result = {
            "Fibonacci": False,
            "Number": x,
            "Server IP": "123.234.253.23",
        }
    else:
        print("Fibonacci sequence:")
        
        result = {
                "Fibonacci": True,
                "Number": x,
                "Server IP": "122.223.256.24",
            }

    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)