from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404


if __name__ == '__main__':
    app.run(debug=True)
