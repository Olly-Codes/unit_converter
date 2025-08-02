import conversion as c
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        try:
            category: str = request.form["category"]
            value: float = float(request.form["value"])
            from_unit: str = request.form["from_unit"]
            to_unit: str = request.form["to_unit"]

            print(category, value, from_unit, to_unit)

            match category:
                case "length":
                    return redirect(url_for("length", length=value,
                                             from_unit=from_unit,
                                             to_unit=to_unit))
                case "weight":
                    return redirect(url_for("weight", weight=value,
                                             from_unit=from_unit,
                                             to_unit=to_unit))
                case "temperature":
                    return redirect(url_for("temperature", temp=value,
                                             from_unit=from_unit,
                                             to_unit=to_unit))
        except Exception as e:
            print(e)
    return render_template("index.html")

@app.route("/length/<float:length>/<from_unit>/<to_unit>", methods=["GET", "POST"])
def length(length: float, from_unit: str, to_unit: str):

    if request.method == "POST":
        return redirect(url_for("index"))

    orig_val = length
    results = c.convert_length(length, from_unit, to_unit)
    converted_val = results

    return render_template("length.html", orig_length=orig_val, 
                           value=converted_val, from_unit=from_unit,
                           to_unit=to_unit)


@app.route("/weight/<float:weight>/<from_unit>/<to_unit>", methods=["GET", "POST"])
def weight(weight: float, from_unit: str, to_unit: str):

    if request.method == "POST":
        return redirect(url_for("index"))

    orig_val = weight
    results = c.convert_weight(weight, from_unit, to_unit)
    converted_val = results

    return render_template("weight.html", orig_weight=orig_val, 
                           value=converted_val, from_unit=from_unit,
                           to_unit=to_unit)

@app.route("/temperature/<float:temp>/<from_unit>/<to_unit>", methods=["GET", "POST"])
def temperature(temp: float, from_unit: str, to_unit: str):

    if request.method == "POST":
        return redirect(url_for("index"))

    orig_val = temp
    results = c.convert_temp(temp, from_unit, to_unit)
    converted_val = results

    return render_template("temperature.html", orig_temp=orig_val, 
                           value=converted_val, from_unit=from_unit,
                           to_unit=to_unit)

if __name__ == "__main__":
    app.run(debug=True)