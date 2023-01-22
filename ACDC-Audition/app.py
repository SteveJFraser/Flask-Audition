from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/loggedin')
def loggedin():
    first_name = request.args.get('fname-data')
    last_name = request.args.get('lname-data')
    return render_template('loggedin.html', first_name=first_name, last_name=last_name)


if __name__ == "__main__":
    app.run(debug=True)
