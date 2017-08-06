from flask import Flask, render_template, url_for

app = Flask(__name__)

# Here we are mapping the URL "/" to the python function index
@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = "true")

