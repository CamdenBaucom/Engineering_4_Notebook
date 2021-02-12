import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    print("Get ready")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    camera.start_preview()
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Taking picture")
    camera.capture('pic1.jpg')
    print("Done")
