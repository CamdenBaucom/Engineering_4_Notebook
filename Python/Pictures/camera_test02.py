import time
import picamera
effects = ['watercolor','cartoon','blur','washedout','oilpaint']

for i in range(5):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.image_effect = str(effects[i])
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
        camera.capture('filterpic'+str(i)+'.jpg')
        print("Done")
