from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    camera.start_preview()
    pir.wait_for_no_motion()
    camera.stop_preview()
