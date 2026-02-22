#!/usr/bin/python3
"""Implements a simple Flask API."""

from flask import Flask, jsonify

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user[username])

@app.route("/add_user")
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User created",
        "user": user
    }), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
