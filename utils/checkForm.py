#Angela Yu SoftDev pd 6
#py file for checking login info, functions for writing/storing user&pass

import hashlib
import csv

def checkLog(user, password):
    data=csv.reader(open("data/userInfo.csv"))
    for entry in data:
        if user == entry[0]:
            if hashlib.sha1(password).hexdigest()==entry[1]:
                return "success! You have logged in."
            return "failure. Incorrect password"
    return "failure. This username does not exist."


def checkReg(user, password):
    data=csv.reader(open("data/userInfo.csv"))
    for entry in data:
        if user == entry[0]:
            return "Failure. This username is taken!"
    with open('data/userInfo.csv', 'a') as csvfile:
        w=csv.writer(csvfile)
        w.writerow ([user, hashlib.sha1(password).hexdigest()])
    return "Success! You have registered."
