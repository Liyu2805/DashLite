from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", fullname="", email="", bio="", skill="")

@app.route("/dashboard", methods=["POST"])
def dashlite():
    fullname = request.form.get("name")
    email = request.form.get("email")
    bio = request.form.get("message")
    skill = request.form.get("skill")
    hours = 0.1
    streak = 1
    return render_template("dashboard.html", fullname=fullname, email=email, bio=bio, skill=skill, hours=hours, streak=streak)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)