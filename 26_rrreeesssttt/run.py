# Joshua Weiner
# SoftDev1 pd06
#K #25: Getting More REST
# 2018-11-14
import json
import urllib.request as urlrequest
from urllib.request import urlopen
from flask import Flask, render_template
import json, urllib

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/airQuality')
def air():
    key = "FYyF4tsBRbmAdvHaR"
    response = urlopen('https://api.airvisual.com/v2/nearest_city?key=' + key)
    r = response.read()
    d = json.loads(r.decode('utf-8'))
    return render_template("airquality.html", d=d)

@app.route('/news')
def news():
    key = "36c5fe39553a4bd98d59ce42e54a299c"
    response = urlopen('https://newsapi.org/v2/top-headlines?country=us&apiKey=' + key)
    r = response.read()
    d = json.loads(r.decode('utf-8'))
    return render_template("news.html", articles=d['articles'])

@app.route('/tasteDive')
def taste():
    key = '323811-nnnnn-GLM7IWOL'
    req = urlrequest.Request('https://tastedive.com/api/similar?q=tom+petty&info=1&k=' + key, headers={'User-Agent': 'Mozilla/5.0'})
    r = urlopen(req).read()
    d = json.loads(r.decode('utf-8'))
    return render_template("tasty.html", d=d)

if __name__=="__main__":
    app.debug=True
    app.run()
