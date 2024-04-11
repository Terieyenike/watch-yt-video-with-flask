from flask import Flask, render_template, request, jsonify
import pywhatkit

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/watch", methods=["POST"])
def watch():
   try:
    video = request.form['video']
    pywhatkit.playonyt(video)
    return render_template('watch.html', video=video)
   except Exception as e:
     return render_template('error.html', error=str(e))
