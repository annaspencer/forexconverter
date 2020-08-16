from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = "327-446-427"
debug = DebugToolbarExtension(app)
c = CurrencyRates()
cc = CurrencyCodes()


@app.route("/")
def home_page():
    """home page"""
    return render_template("index.html")

@app.route("/convert")
def convert():
    """convert"""
    con_from = request.args["convert_from"]
    con_to = request.args["convert_to"]
    amount = request.args["amount"]
    symbol = cc.get_symbol(con_to)

    if type(amount) != int:
        return render_template("invalid-num.html")
    else: return render_template("converted-rate.html", con_from = con_from, con_to = con_to,  amount = amount, symbol = symbol)
