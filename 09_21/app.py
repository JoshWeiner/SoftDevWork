from flask import Flask, render_template
app = Flask(__name__)

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template")
def home():
    return render_template("template.html",
                        coll=coll)

if __name__ == "__main__":
    app.debug=True
    app.run()
