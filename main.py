from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<user>')
def user (user):
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

    