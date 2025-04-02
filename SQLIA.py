from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.executemany("INSERT INTO users (username, password) VALUES (?, ?)",
                  [("admin", "password123"), ("user1", "letmein"), ("user2", "123456")])
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        c.execute(query)
        user = c.fetchone()
        conn.close()
        
        if user:
            message = f"Welcome, {user[1]}!"
        else:
            message = "Invalid credentials!"
    
    return render_template_string('''
        <html>
        <body>
            <h2>Login</h2>
            <form method="post">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
            <p>{{ message }}</p>
        </body>
        </html>
    ''', message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
