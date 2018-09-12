##Joshua Weiner and Thomas Lee - Leiner and Meaner
##SoftDev1 pd06
##K 02: NO-body expects the Spanish Inquisition!
##2018 - 09 - 09

import random
#This allows us to randonly select from a group

KREWES = {

        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']

} #KREWES defined as global variable


def randomizer():
    chosenTeam = raw_input("Choose your team (w, m, or x): ") #User chooses the team from which they want a random member of
    if KREWES.has_key(chosenTeam):
        #make a list of the chosen team
        team = KREWES[chosenTeam]
        #randonly select one student from the team
        #print team #for debugging
        student = random.choice(team) 
        #print the student's name
        print(student) 
    else:
        print ("KREWES doesn't have team " + chosenTeam) #For when the user inputs an invalid team

randomizer() #run the randomizer
