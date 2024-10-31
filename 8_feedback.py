from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

feedback_list = []

@app.route('/')
def home():
    return "Go to /feedback to access the feedback app!"

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        feedback_list.append({'name': name, 'feedback': feedback})
    return render_template('feedback.html', feedback_list=feedback_list)

@app.errorhandler(404)
def page_not_found(e):
    return "This route is not available at the moment. Please check the URL! Thank you ! :)", 404

if __name__ == '__main__':
    app.run(debug=True)
