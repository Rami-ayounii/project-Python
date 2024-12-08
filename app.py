from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
from routes import register_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

register_routes(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)