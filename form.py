#angela
#forms
#9/28

from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
@app.route("/login/")
def form():
    print request.headers
    return render_template('form.html', title="test form")

@app.route("/authen/", methods=['POST'])
def auth():
    response=""
    if request.form["user"]=="hello" and request.form["password"]=="cool":
        response="success"
    else:
        response="failure"
    return render_template('formMessage.html', message=reponse)
                               

if __name__=="__main__":
    app.debug=True
    app.run()
