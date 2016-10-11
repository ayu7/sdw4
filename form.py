#angela
#forms
#9/28

from flask import Flask, render_template, request, session, url_for, redirect
import os, hashlib, csv

app=Flask(__name__)
app.secret_key=os.urandom(32)


@app.route("/login/")
@app.route("/")
def form():
    if len(session.keys())==0:
        return render_template('form.html', title="test form")
    else:
        return redirect(url_for('home'))

@app.route("/home/")
def home():
    return render_template('home.html', username=session['userkey'])

@app.route("/logout/")
def logout():
    session.pop('userkey')
    return render_template('authenticate.html', message="sucess! You have logged out.")

@app.route("/authen/", methods=['POST'])
def auth():
    if request.form["action"]=="login":
        return render_template('authenticate.html', message= checkLog(request.form["user"], request.form["password"]))
    else:
        return render_template('form.html', message= checkReg(request.form["user"], request.form["password"]))

def checkLog(user, password):
    data=csv.reader(open("data/userInfo.csv"))
    for entry in data:
        if user == entry[0]:
            if hashlib.sha1(password).hexdigest()==entry[1]:
                session['userkey']=user
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


if __name__=="__main__":
    app.debug=True
    app.run()
