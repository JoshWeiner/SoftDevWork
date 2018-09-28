from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("base.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
