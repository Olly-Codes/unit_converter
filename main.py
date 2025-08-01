from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        try:
            category = request.form["category"]
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]

            print(category, value, from_unit, to_unit)
        except Exception as e:
            print(e)
        return f"It works"
    return render_template("index.html")

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

if __name__ == "__main__":
    app.run(debug=True)