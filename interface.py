from flask import Flask, render_template, request
from imc import Imc

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():

    return render_template("home.html")


@app.route("/calculo", methods=["POST"])
def calculo():
    peso = float(request.form.get("peso"))
    altura = float(request.form.get("altura"))
    print(peso)
    print(altura)
    calc = Imc(peso, altura)
    total = round(calc.calculo(), 2)
    print(total)
    return render_template("calculo.html", total=total)


if __name__ == "__main__":
    app.run(debug=True)
