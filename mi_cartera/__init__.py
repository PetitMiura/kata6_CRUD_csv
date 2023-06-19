from flask import Flask, render_template
import csv


app = Flask(__name__) #Creamos la aplicacion

@app.route("/") # Primera ruta o punto de entrada
def index():
    f = open("movements.dat", "r")
    reader = csv.reader(f, delimiter=",", quotechar='"')
    movements = list(reader)
    return render_template("index.html", the_movements=movements)
