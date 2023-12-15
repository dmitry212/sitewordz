""" sitewordz app! """
import sqlite3
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/get_logged_in_user')
def get_logged_in_user():
    conn = sqlite3.connect('sitewordz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE is_logged_in = 1")
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "No logged-in user found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
