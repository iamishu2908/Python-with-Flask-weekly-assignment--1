from flask import Flask, render_template
import random
app = Flask(__name__)
quotes = [
"Be the change that you wish to see in the world.",
"The best way to find yourself is to lose yourself in the service of others.",
"Live as if you were to die tomorrow. Learn as if you were to live forever.",
"In a gentle way, you can shake the world.",
"The weak can never forgive. Forgiveness is the attribute of the strong."
]


@app.route('/')
def home():
    return "Go to /quote to get an insighting quote from Gandhi Ji!"

@app.route('/quote')
def quote():
    chosen_quote = random.choice(quotes)
    return render_template('quote.html', quote=chosen_quote)

@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404

if __name__ == '__main__':
    app.run(debug=True)
