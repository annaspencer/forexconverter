from flask import Flask, request, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal
import math



app = Flask(__name__)
app.config['SECRET_KEY'] = "327-446-427"
debug = DebugToolbarExtension(app)
c = CurrencyRates(force_decimal=True)
cc = CurrencyCodes()


@app.route("/")
def home_page():
    """home page"""
    return render_template("index.html")
        
    

@app.route("/convert")
def convert():
    """convert """
    try:
        con_from = request.args["convert_from"]
        con_to = request.args["convert_to"]
        amount = Decimal(request.args["amount"])
        symbol = cc.get_symbol(con_to)
        converted_amt = c.convert(con_from, con_to, amount)
        display_amt = round(converted_amt, 2)
        
        return render_template("converted-rate.html", con_from = con_from, con_to = con_to, display_amt = display_amt, symbol = symbol)
    except:
            return render_template("/error.html")
        
@app.route("/error")
def error():
    """display error message"""

    amount = request.args["amount"]

    return render_template("error.html", amount = amount )
