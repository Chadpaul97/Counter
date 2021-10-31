from flask import Flask,render_template,session,redirect
from werkzeug.utils import redirect
app = Flask(__name__)
app.secret_key = 'topSecret'

@app.route('/')
def index():
    if 'visit' in session:
        session['visit']+=1
    else:
        session['visit'] = 1
    if 'count' in session:
        session['count']+=1
    else:
        session['count'] = 0
    return render_template("index.html")


@app.route("/destroy_sess")
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)