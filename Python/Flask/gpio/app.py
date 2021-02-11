from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
global msg1
global msg2
msg1 = "You have not Turned on the Green Light Yet."
msg2 = "You have not Turned on the Red Light Yet."

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
     if request.method == "POST":
          if request.form.get("submitBtn1") == "You Turned on the Green Light!":
               if GPIO.input(17) == 1:
	            GPIO.output(17,GPIO.LOW)
                    global msg2
                    global msg1
		    msg2 = msg2
                    msg1 = "You Turned off the Green Light!"
	       else:
                    GPIO.output(17,GPIO.HIGH)
	            msg2 = msg2
                    msg1 = request.form.get("submitBtn1")
	  else:
               if GPIO.input(27) == 1:
                    GPIO.output(27,GPIO.LOW)
                    msg1 = msg1
                    msg2 = "You Turned off the Red Light!"
               else:
                    GPIO.output(27,GPIO.HIGH)
                    msg1 = msg1
                    msg2 = request.form.get("submitBtn2")
     return render_template("index.html", msg1=msg1, msg2=msg2)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
