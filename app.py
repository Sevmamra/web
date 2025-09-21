from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["username"]
    email = request.form["email"]
    role = request.form["role"]
    
    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #333;
            }}
            .box {{
                background: white;
                padding: 40px;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }}
            h1 {{ color: #0077cc; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Hello, {name}! 👋</h1>
            <p>We’ve registered your email as <b>{email}</b>.</p>
            <p>You are a proud <b>{role}</b> 🚀</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
