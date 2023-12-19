""" sitewordz app! """
import sqlite3
from flask import Flask, jsonify, session, render_template

app = Flask(__name__)
app.secret_key ='2hKgJ4kbZMoWAQ-'

def get_current_user():
    """loads currently logged in user"""
    conn = sqlite3.connect('db/sitewordz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name FROM users WHERE is_logged_in = 1")
    user = cursor.fetchone()
    conn.close()
    print(f"user: {user}, type(user): {type(user)}")
    session['user_id'] = user[0]
    if user:
        return user[1]
    else:
        return jsonify({"error": "No logged-in user found"}), 404

@app.route('/')
def play_game():
    """main gameç logic"""
    user = get_current_user()
    return render_template('web/game_play.html', user_name=user)

if __name__ == '__main__':
    app.run(debug=True)
