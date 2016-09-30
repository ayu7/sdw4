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
    if request.form["user"]=="hello" and request.form["password"]=="cool":
        return render_template('authenticate.html', message="success")
    else:
        return render_template('authenticate.html', message="failure")
                               

if __name__=="__main__":
    app.debug=True
    app.run()
