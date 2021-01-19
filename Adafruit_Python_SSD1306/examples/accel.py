import time #import time library
import Adafruit_SSD1306 #import the display library
import Adafruit_LSM303 #import the accelerometer library

from PIL import Image #import Python Imaging Library elements
from PIL import ImageDraw #import Python Imaging Library elements
from PIL import ImageFont #import Python Imaging Library elements

lsm303 = Adafruit_LSM303.LSM303() #set up accelerometer called lsm303
RST = 24 #ssd pin configuration

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D) #sets up ssd disp

disp.begin() #begin running display
disp.clear() #clear display
disp.display() #establish display

width = disp.width  #establish width as total width of display
height = disp.height #establish height as total height of display
image = Image.new('1', (width, height)) #creating black and white image

draw = ImageDraw.Draw(image) #draw means run image
font = ImageFont.load_default() #establish font as default

while True: #run forever
	draw.rectangle((0,0,width,height), outline=0, fill=0) #create a black rectangle the total size of the screen
	draw.text((0, 0),    'Accel Data:',  font=font, fill=500) #Write Accel Data at the top
	accel, mag = lsm303.read() #accel reads from the lsm
	accel_x, accel_y, accel_z = accel #take the three varibles and asign them to x,y,z
	real_accel_x = accel_x / 100 #turn it into m/s^2
	real_accel_y = accel_y / 100 #turn it into m/s^2
	real_accel_z = accel_z / 100 #turn it into m/s^2
	draw.text((0, 20),    'X:{0:.3f}'.format(real_accel_x),  font=font, fill=500) #print X: and then its info with 3 decimal places
	draw.text((0, 35),    'Y:{0:.3f}'.format(real_accel_y),  font=font, fill=500) #print X: and then its info with 3 decimal places
	draw.text((0, 50),    'Z:{0:.3f}'.format(real_accel_z),  font=font, fill=500) #print X: and then its info with 3 decimal places
	disp.image(image) #print all the previous data
	disp.display() #display the image
	time.sleep(0.1) #wait 0.1 seconds (before a new rectangle is made and the info gets updated
