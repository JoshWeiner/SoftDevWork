# Joshua Weiner
# SoftDev1 pd06
#K #25: Getting More REST
# 2018-11-14

from flask import Flask, render_template
import json, urllib

app=Flask(__name__)
key = "AldSY8uCqSuYTIB4i2k9K1vsabwmG6qT"

@app.route("/")
def home():
    #url to be requested. Passed date parameter, my api key, and parameter for hd quality image
    #chose my birthday, because why not?
    url = 'https://app.ticketmaster.com/discovery/v2/events.json?city=New-York&apikey='
    #loads http response
    response = urllib.request.urlopen(url + key)
    #reads sent information packet
    r = response.read()
    #jsonify the packet, turning it into a dictionary
    stuff = json.loads(r)
    #test print for debugging
    listofevents = stuff['_embedded']['events']
    print(listofevents)

    #return html template with json dictionary
    return render_template("index.html", events=listofevents)

if __name__=="__main__":
    app.debug=True
    app.run()
