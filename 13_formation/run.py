from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("form.html")

@app.route("/auth")
def authenticate():
    name = app
    req = request
    username = request.args['username']
    return render_template("base.html", a_name = name, req=req, username=username)

if __name__ == "__main__":
    app.debug = True
    app.run()
