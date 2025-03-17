from flask import Flask
import subprocess
import os
import datetime

app = Flask(__name__)

# Default homepage
@app.route('/')
def home():
    return "Go to <a href='/htop'>/htop</a> to see system stats."

# /htop endpoint to show system stats
@app.route('/htop')
def htop():
    name = "Bhanu Prakash"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get system's 'top' command output
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <html>
    <body>
        <pre>
Name: {name}
User: {username}
Server Time (IST): {server_time}

TOP output:

{top_output}
        </pre>
    </body>
    </html>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
