from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world!"

@app.route("/admin/")
def admin():
	return "sorry admin page not yet createds"

@app.route("/about/")
def admin():
	return "sorry about page not yet createds"


if __name__ == "__main__":
	app.run(debug=True,port=80)
