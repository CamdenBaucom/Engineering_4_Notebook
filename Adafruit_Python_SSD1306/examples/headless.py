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
	draw.text((45,50),    'Z:m/s^2',  font=font, fill=500) #Write Z:m/s^2 at the top
	accel, mag = lsm303.read() #accel reads from the lsm
	accel_x, accel_y, accel_z = accel #take the three varibles and asign them to x,y,z
	real_accel_z = accel_z / 100 #turn it into m/s^2
	if real_accel_z > 11: #if accel is greater than 11
		real_accel_z = 11 #make it 11
	if real_accel_z < -11: #if accel is less than -11
		real_accel_z = -11 # make it -11
	math_z = (real_accel_z - 11)*(-1) #subtract 11 and make it positive again
	line_z = (math_z * 40)/(22) #numbers will range from 0-22 and they need to range from 0-40 so convert
	draw.text((0, 0),    '11',  font=font, fill=500) #Accel of 11 will be printed at the top
	draw.text((0, 20),    '0',  font=font, fill=500) #Accel of 0 will be printed in the middle
	draw.text((0, 40),    '-11',  font=font, fill=500) #Accel of -11 will be printed at the bottom
	draw.line((30, line_z, 98, line_z), fill=255) #create a line with y values ranging from 0-40 according to the scale
	disp.image(image) #print all the previous data
	disp.display() #display the image
	time.sleep(0.01) #wait 0.01 seconds (before a new rectangle is made and the info gets updated

