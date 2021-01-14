import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((0, 0),    'Accel Data:',  font=font, fill=500)
# draw.text((0, 50),    'Accel Data:',  font=font, fill=100)

while True:
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	accel_x_str = str(accel_x)
	accel_y_str = str(accel_y)
	accel_z_str = str(accel_z)
	draw.text((0, 20),    'X:{0:.3f}'.format(accel_x) + accel_x_str,  font=font, fill=500)
	# draw.text((0, 35),    'Y:' + accel_y_str,  font=font, fill=500)
	# draw.text((0, 50),    'Z:' + accel_z_str,  font=font, fill=500)
	disp.image(image)
	disp.display()
	time.sleep(0.5)
	disp.clear()
