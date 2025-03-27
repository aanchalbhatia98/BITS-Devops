from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Define a route to return a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello, Flask!", "status": "success"}
    return jsonify(data)

# Define a route to handle POST requests
@app.route('/api/data', methods=['POST'])
def post_data():
    input_data = request.json
    response = {"received": input_data, "status": "success"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)