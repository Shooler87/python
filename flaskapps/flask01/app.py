import math

from flask import Flask, request, render_template, session
# todo marshmallow pydantic apiflask smorest
app = Flask(__name__)
app.secret_key = "^DES &ja8s72"

@app.route("/")
def home():
    return "HOME"


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/calc", methods=["POST"])
def calc():
    return request.form


def make_calcs(items):
    session["calcs"] = math.prod(items)
    return session["calcs"]


@app.route("/showcalc", methods=["POST"])
def showcalc():
    # if "secret" not in request.form:
    #     return {"missing": "secret"}
    filtered = [(field, value) for field, value in request.form.items() if field != "hidden_factor"]
    if "calcs" not in session:
        final_value = make_calcs([float(v) for v in request.form.values()])
    else:
        final_value = session["calcs"]
    return render_template("showcalc.html", post=filtered, final_value=final_value)


@app.route("/checksession/<sessionkey>")
def checksession(sessionkey):
    if sessionkey in session:
        return f"session[{sessionkey}] = {str(session[sessionkey])}"
    else:
        return f"{sessionkey} not in session"


@app.route("/destroysession")
def destroysession():
    session.clear()
    return "SESSION DESTROYED"


@app.route("/params/<float:num>/<name>/<surname>")
@app.route("/params/<int:num>/<name>/<surname>")
def params(num: int | float, name: str, surname: str):
    return f"{num} {name} {surname}"


@app.errorhandler(404)
def handle500(e):
    return "ERROR 404", 404


@app.errorhandler(500)
def handle500(e):
    return "ERROR 500", 500

# run app in debug with autoreloading on file save
app.run(debug=True)