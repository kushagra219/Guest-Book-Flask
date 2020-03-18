from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    pass


if __name__ == '__main__':
    app.run(debug=True)