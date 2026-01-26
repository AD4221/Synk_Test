import os
import sqlite3
from flask import Flask, request
import requests

app = Flask(__name__)

# Misconfiguration 1: Hardcoded credentials
API_KEY = os.getenv('API_KEY')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Misconfiguration 2: Insecure database connection
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row

# Misconfiguration 3: SQL Injection vulnerability
@app.route('/user/<user_id>')
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = conn.execute(query)
    return cursor.fetchall()

# Misconfiguration 4: Insecure deserialization
@app.route('/data', methods=['POST'])
def process_data():
    import pickle
    data = pickle.loads(request.data)
    return data

# Misconfiguration 5: Missing authentication
@app.route('/admin')
def admin_panel():
    return "Admin Panel"

# Misconfiguration 6: Insecure external request
@app.route('/fetch')
def fetch_external():
    url = request.args.get('url')
    response = requests.get(url, verify=False)  # No SSL verification
    return response.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Debug mode enabled