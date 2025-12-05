from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import string
import random
import os

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, short TEXT, long TEXT)")
        conn.commit()
        conn.close()

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# --- Home Page ---
@app.route("/")
def home():
    return render_template("index.html", short_url=None)

# --- Create Short URL ---
@app.route("/shorten", methods=["POST"])
def shorten_url():
    long_url = request.form.get("long_url")

    if not long_url:
        return render_template("index.html", short_url="Invalid URL")

    # Generate unique code
    short_code = generate_short_code()

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO urls (short, long) VALUES (?, ?)", (short_code, long_url))
    conn.commit()
    conn.close()

    short_url = request.host_url + short_code
    return render_template("index.html", short_url=short_url)

# --- Redirect Short URL ---
@app.route("/<short_code>")
def redirect_url(short_code):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT long FROM urls WHERE short = ?", (short_code,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "Invalid URL", 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)