from flask import Flask, jsonify, request, send_from_directory
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Simulated data 
data = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com", "country": "USA"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com", "country": "Canada"},
    {"id": 3, "name": "Charlie", "age": 22, "email": "charlie@example.com", "country": "UK"},
    {"id": 4, "name": "Diana", "age": 28, "email": "diana@example.com", "country": "Germany"},
    {"id": 5, "name": "Eve", "age": 35, "email": "eve@example.com", "country": "France"}
]

# Route for the home page
@app.route('/', methods=['GET'])
def home():
    """
    Home route
    ---
    responses:
      200:
        description: Welcome message
    """
    return jsonify({"message": "Welcome to the REST API! Use /apidocs for Swagger documentation."})

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              age:
                type: integer
              email:
                type: string
              country:
                type: string
    """
    return jsonify(data)

# Route to get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    responses:
      200:
        description: User found
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
            email:
              type: string
            country:
              type: string
      404:
        description: User not found
    """
    user = next((u for u in data if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    """
    Add a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: integer
            email:
              type: string
            country:
              type: string
    responses:
      201:
        description: User added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            age:
              type: integer
            email:
              type: string
            country:
              type: string
    """
    new_user = request.json
    new_user['id'] = len(data) + 1
    data.append(new_user)
    return jsonify(new_user), 201

# Route to handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
