from flask import Flask, render_template
import requests

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(blog_url).json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = response)


@app.route('/post/<id>')
def post(id):
	id = int(id) - 1
	return render_template('post.html', post=response[id])

if __name__ == "__main__":
    app.run(debug=True)

