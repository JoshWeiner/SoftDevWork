# Joshua Weiner
# SoftDev1 pd06
# K #24: A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import json, urllib

app=Flask(__name__)
#My API key: LpXOMgLF9wRXaF259fjRP6gWZvj4nb2jB6h1jX7L

@app.route("/")
def home():
    #url to be requested. Passed date parameter, my api key, and parameter for hd quality image
    #chose my birthday, because why not?
    url = 'https://api.nasa.gov/planetary/apod?api_key=LpXOMgLF9wRXaF259fjRP6gWZvj4nb2jB6h1jX7L&date=2018-7-22&hd=True'
    #loads http response
    response = urllib.request.urlopen(url)
    #reads sent information packet
    r = response.read()
    #jsonify the packet, turning it into a dictionary
    stuff = json.loads(r)
    #test print for debugging
    print(stuff)

    #return html template with json dictionary
    return render_template("index.html", stuff=stuff)

if __name__=="__main__":
    app.debug=True
    app.run()
