<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story')
def story():
    return render_template('base.html')

if __name__ == '__main__':
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story')
def story():
    return render_template('base.html')

if __name__ == '__main__':
>>>>>>> 23b7505c4038c2702db7b8ec8a7c28469790f6b9
    app.run(debug=True)