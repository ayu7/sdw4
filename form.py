#angela
#forms
#9/28

from flask import Flask, render_template, request
from utils import checkForm

app=Flask(__name__)

@app.route("/")
@app.route("/login/")
def form():
    print request.headers
    return render_template('form.html', title="test form")

@app.route("/authen/", methods=['POST'])
def auth():
    if request.form["action"]=="login"
        return render_template('authenticate.html', message= checkForm.checkLog(request.form["user"], request.form["password"]))
    else:
        return render_template('form.html', message= checkForm.checkReg(request.form["user"], request.form["password"]))


if __name__=="__main__":
    app.debug=True
    app.run()
