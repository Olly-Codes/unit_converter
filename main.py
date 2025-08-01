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

@app.route("/length/<float:length>/<from_unit>/<to_unit>")
def length(length: float, from_unit: str, to_unit: str):
    print(f"You made it! {length}{from_unit}{to_unit}")
    return render_template("length.html")


@app.route("/weight/<float:weight>/<from_unit>/<to_unit>")
def weight(weight: float, from_unit: str, to_unit: str):
    print(f"You made it! {weight}{from_unit}{to_unit}")
    return render_template("weight.html")

@app.route("/temperature/<float:temp>/<from_unit>/<to_unit>")
def temperature(temp: float, from_unit: str, to_unit: str):
    print(f"You made it! {temp}{from_unit}{to_unit}")
    return render_template("temperature.html")

if __name__ == "__main__":
    app.run(debug=True)