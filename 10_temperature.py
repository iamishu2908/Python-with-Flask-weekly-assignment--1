from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fahrenheit = None
    if request.method == 'POST':
        celsius = float(request.form['celsius'])
        fahrenheit = (celsius * 9/5) + 32
    return render_template('temperature.html', fahrenheit=fahrenheit)


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404


if __name__ == '__main__':
    app.run(debug=True)
