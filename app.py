from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["username"]
    return f"<h1>Hello, {name}! 👋 Welcome to my website.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
