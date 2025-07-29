from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

if __name__ == "__main__":
    app.run(debug=True)