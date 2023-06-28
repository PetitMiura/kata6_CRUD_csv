from mi_cartera import app
from mi_cartera.models import Movement, MovementDAO
from flask import render_template, request, redirect, flash
import csv

dao = MovementDAO("movements.dat")

@app.route("/")
def index():
    try:
        movements = dao.all()
        return render_template("index.html", the_movements=movements, title="Todos")
    except ValueError as e:
        flash("Su fichero de datos está corrupto")
        flash(str(e))
        return render_template("index.html", the_movements=[], title="Todos")


@app.route("/new_movement", methods=["GET", "POST"])
def new_mov():
    if request.method == "GET":
        return render_template("new.html", the_form = {}, title="Alta de movimiento")
    else:
        data = request.form
        try:
            dao.insert(Movement(data["date"], data["abstract"],
                                data["amount"], data["currency"]))
            return redirect("/")
        except ValueError as e:
            flash(str(e))
            return render_template("new.html", the_form=data, title="Alta de movimiento")

      

@app.route("/update_movement/<int:pos>", methods=["GET", "POST"])
def upd_mov(pos):
    if request.method == "GET":
        mov = dao.get(pos)
        return render_template("update.html", title="Modificación de movimiento",
                               the_form=mov)
    else:
        data = request.form
        try:
            mv = Movement(data["date"], data["abstract"],
                                data["amount"], data["currency"])
            dao.update(pos, mv)
        except ValueError as e:
            flash(str(e))
            return render_template("update.html", the_form=data, title="Modificación de movimiento")

      