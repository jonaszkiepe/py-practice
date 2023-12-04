from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
response = requests.get('https://api.npoint.io/f4e424f597d8a068c460').json()


@app.route('/')
def home():
    return render_template('index.html', posts=response)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<id>')
def post(id):
    id = int(id) - 1
    return render_template('post.html', post=response[id])


@app.route('/form-entry', methods=["POST"])
def receive_data():
    print(request.form["name"])
    print(request.form["email"])
    print(request.form["phone"])
    print(request.form["message"])
    return "<h1>Message has been sent</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)
