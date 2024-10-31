from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Hello everyone, this is Ishwarya here ! Go to /bio to access my bio page!"

@app.route('/bio')
def bio():
    return render_template('/bio.html', name="Ishwarya Devanathan", age=21, hobbies=["Cook and try new recipes", "Read sci-fi books", "Listen to good music","Watch movies and series"])


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404

if __name__ == '__main__':
    app.run(debug=True)
