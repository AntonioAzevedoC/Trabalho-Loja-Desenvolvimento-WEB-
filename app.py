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

# Rota página de produtos
@app.route('/produtos')
def renderProdutos():
    return render_template("produtos.html")

