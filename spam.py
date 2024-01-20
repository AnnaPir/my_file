from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/spam/<string:text>/<int:count>")
def spam(text="spam", count=10):
    text = " " + text
    return text * count


@app.route("/")
@app.route("/main")
def index():
    return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("from.html")

@app.route("/scam")
def scam():
    return render_template("scam.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        value = int(request.form.get("age"))
        print(value)
        if value < 18:
            return f"Ваш вік менше 18, ми не зможемо <strike>обдурити вас</strike> вам допомогти"
        else:
            return render_template("scam.html")


@app.route("/submit_form2", methods=["GET"])
def submit_form2():
    if request.method == "GET":
        value = request.args.get("name")
        print(value)
    return f"З Вашої картки зняли гроши."


if __name__ == "__main__":
    app.run(debug=True)