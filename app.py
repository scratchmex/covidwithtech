from flask import Flask, request, render_template

app = Flask(__name__)


import news, stats


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/actions", methods=["POST"])
def actions():
    data = request.form
    task = data.get("CurrentTask")

    if not task:
        return {"actions": [{"say": "Some error ocurred, please try again."}]}

    if task == "news":
        return news.action(data)

    if task == "stats":
        return stats.action(data)

    return {"actions": [{"say": f"That task ({task}) wasn't recognized"}]}
