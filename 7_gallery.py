from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return " Go to /gallery to access the gallery page!"

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404


if __name__ == '__main__':
    app.run(debug=True)
