from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Подключение к базе данных SQL Server
def get_db_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=db;DATABASE=mydb;UID=user;PWD=password')
    return conn

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
