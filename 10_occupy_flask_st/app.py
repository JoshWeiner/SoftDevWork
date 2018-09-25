#Team Jinja Bread Men - Joshua Weiner and Bo Hui Lu
#SoftDev pd6
#K #10: Jinja Tuning ...
#2018-09-23

from flask import Flask, render_template
from csv import reader
import random
from data import occupations.csv
app = Flask(__name__)

occDict = {}
occList = []

@app.route("/")
@app.route("/home")
def home():
    return('''
<h3>Find your job below</h3>
<a href="/occupations">Click Me!</a>
''')

@app.route("/occupations")
def occupado():
    #opens csv file, reads it as dictionary
    #separates by commas not contained in double quotes
    with open('occupations.csv') as infile:
        reader = csv.DictReader(infile)
        #for each row in the csv file
        for row in reader:
            #add occupation and percentage to dictionary
             occDict[ row['Job Class'] ] = row['Percentage']
        #remove the dictionary key/value pair of 'Total'
        occDict.pop('Total')

    #Turns percentage string into a floating point
    #Loop through each key/value pair in dictionary
    for i in occDict.keys():
        occDict[i] = eval(occDict[i])

    #Adds jobs to array where it can be selected randomly based on its percentage
    for job in occDict.keys():
        for numTimes in range(int(occDict[job] * 10)):
            #Need to convert percentages to integers accurately to use the range() function,
            occList.append(job)
            #populate an array of ~1000 values, because of the use of range
            #array populated by percentages
    #return dictionary, random occupation, html template
    return render_template("template.html", occ=occDict, randocc=random.choice(occList))

if __name__ == "__main__":
    app.debug=True
    app.run()
