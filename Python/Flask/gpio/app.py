from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST1","POST2"])
def index():
     if request.method == "POST1":
          GPIO.output(17,GPIO.HIGH)
          msg = request.form.get("submitBtn1")
     else:
          GPIO.output(17,GPIO.LOW)
          msg = "You have not Turned on the Green Light Yet."
     if request.method == "POST2":
          GPIO.output(27,GPIO.HIGH)
          msg = request.form.get("submitBtn2")
     else:
          GPIO.output(27,GPIO.LOW)
          msg = "You have not Turned on the Red Light Yet."
     return render_template("index.html", msg=msg)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
