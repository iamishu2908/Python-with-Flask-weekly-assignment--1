from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "user" and password == "password":
        return "Welcome! You have landed on the home page. :)", 200
    else:
        return "Invalid credentials. Please try again!", 401


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404


if __name__ == '__main__':
    app.run(debug=True)
