from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json()
    message = data.get("message")

    conn = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success", "message": message})

@app.route("/messages", methods=["GET"])
def get_messages():
    conn = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM messages")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
