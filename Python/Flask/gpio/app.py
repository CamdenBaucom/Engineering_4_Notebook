from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
     if request.method == "POST":
          if request.form.get("submitBtn1") == "You Turned on the Green Light!" and request.form.get("submitBtn1") == "You Turned on the Red Light!":
               GPIO.output(17,GPIO.HIGH)
               GPIO.output(27,GPIO.HIGH)
               msg1 = request.form.get("submitBtn1")
               msg2 = request.form.get("submitBtn2")
          elif request.form.get("submitBtn1") == "You Turned on the Green Light!":
               GPIO.output(17,GPIO.HIGH)
               GPIO.output(27,GPIO.LOW)
               msg1 = "You have not Turned on the Green Light Yet."
               msg2 = request.form.get("submitBtn2")
	  else:
               GPIO.output(17,GPIO.LOW)
               GPIO.output(27,GPIO.HIGH)
               msg1 = request.form.get("submitBtn1")
               msg2 = "You have not Turned on the Red Light Yet."
     else:
          GPIO.output(17,GPIO.LOW)
	  GPIO.output(27,GPIO.LOW)
          msg1 = "You have not Turned on the Green Light Yet."
	  msg2 = "You have not Turned on the Red Light Yet."
     # if request.method == "POST2":
          # GPIO.output(27,GPIO.HIGH)
          # msg2 = request.form.get("submitBtn2")
     # else:
          # GPIO.output(27,GPIO.LOW)
          # msg2 = "You have not Turned on the Red Light Yet."
     return render_template("index.html", msg1=msg1, msg2=msg2)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
