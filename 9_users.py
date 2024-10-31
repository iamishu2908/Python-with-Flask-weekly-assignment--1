from flask import Flask, render_template

app = Flask(__name__)
users = [
    {"name": "Arjun", "age": 24, "city": "Mumbai"},
    {"name": "Priya", "age": 28, "city": "Bangalore"},
    {"name": "Rajesh", "age": 32, "city": "Chennai"}
]


@app.route('/')
def index():
    return render_template('users.html', users=users)


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404


if __name__ == '__main__':
    app.run(debug=True)
