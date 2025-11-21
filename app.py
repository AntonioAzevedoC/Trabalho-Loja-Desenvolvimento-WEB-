# flask run --debug

from flask import Flask, render_template, request
from markupsafe import escape
import math

# Iniciando Flask
app = Flask(__name__)

# Rota Index
@app.route('/')
def rootRoute():
    return render_template("index.html") # Rendering HTML page

# Rota página de cálculo de equação de 2°
@app.route('/pageCalc2Grau')
def renderCalc2Grau():
    return render_template("produtos.html")

# Rota página de cálculo de conversão de fahrenheit
@app.route('/pageCalcFahr')
def renderCalcFahr():
    return render_template("conta.html")
