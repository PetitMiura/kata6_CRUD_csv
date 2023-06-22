from mi_cartera import app
from mi_cartera.models import Movement, MovementDAO
from flask import render_template, request, redirect
import csv

dao = MovementDAO("movements.dat")

@app.route("/")
def index():
    f = open("movements.dat", "r")
    reader = csv.DictReader(f, delimiter=",", quotechar='"')
    movements = list(reader)

    return render_template("index.html", the_movements=movements)


@app.route("/new_movement", methods=["GET", "POST"])
def new_mov():
    if request.method == "GET":
        return render_template("new.html")
    else:
        data = request.form
        dao.insert(Movement(data["date"], data["abstract"],
                                  data["amount"], data["currency"]))

        return redirect("/")

