from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return("<h1>This is an app to learn about Josh Weiner!</h1><br><table><tr><td><a href='/josh'>About Josh</a></td></tr><tr><td><a href='/schedule'>Josh's Schedule</a></td></tr></table>")

@app.route("/josh")
def josh():
    return('''
    <h1>About Josh</h1>
    <br>
    <p>Josh (also known as Kim Josh Un) is a current senior at Stuyvesant High School. He loves to play the guitar, participate in Model UN, and CS!! He has a duck, of course, who goes by Kim Ig Neous by day and Ba-rock Obama at night. His duck is a painted rock. Josh has few friends.</p>
    <br>
    <table><tr><td><a href='/'>Home</a></td></tr><tr><td><a href='/schedule'>Josh's Schedule</a></td></tr></table>
    ''')

@app.route("/schedule")
def schedule():
    return('''
    <h1>Josh's Schedule</h1>
    <br>
    <h4>Daily Schedule:</h4>
    <ol>
        <li>BC Calculus</li>
        <li>TA for Intro CS</li>
        <li>Western Political Thought</li>
        <li>Systems Level Communication and Nerd Culture</li>
        <li>Great Books</li>
        <li>Software Development</li>
        <li>US Government and Politics</li>
        <li>Macroeconomics</li>
        <li>Gym/Physics C</li>
        <li>Physics C</li>
    </ol>
    <br><br>
    <h4>Upcoming Events:</h4>
    <table>
        <tr><td>9/28</td><td>TeenHacks LI</tr>
        <tr><td>10/13</td><td>MiniMUNC 2018</td></tr>
        <tr><td>10/27</td><td>HoMMUNC</td></tr>
    </table>
    <br><br>
    <table><tr><td><a href='/'>Home</a></td></tr><tr><td><a href='/josh'>About Josh</a></td></tr></table>
    ''')

if __name__ == "__main__":
    app.debug = True
    app.run()
