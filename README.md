# Engineering_4_Notebook
My Engineering 4 Notebook

## Hello Python
A short program to generate a random number from 1-6 based on user input. This assignment helped refresh me on some Python syntax that I had used in the past but had kind of forgotten. It was also the first time I had used the input() function, which takes user input and determines what return type it is( in contrast to raw_input() which always returns a string,) then whatever the user inputed can then be assigned to a variable and used like any other value.

```ruby
# Automatic Dice Roller
# Written by Camden Baucom

from random import randint #imports the random function

print ("Automatic Dice Roller")


activeProgram = True #boolean used to loop or exit the program

while activeProgram == True: #loops the program
	roll = input("Press enter to get a random number from 1 to 6\nPress x and then enter to escape the program:\n") 
         #logs the input of the user, and determines the type of variable, before assigning the value of the input to roll	
	if roll == "": #if the user just presses enter
		rollValue = randint(1,6) #A random number from 1 to 6 is generated
		print(rollValue) #That number is printed
	elif roll == "x": #if the user presses x and then presses enter
		activeProgram = False #kicks the user out of the while loop 
	else: #if something other than enter, or x and then enter, was pressed
		print("Please reenter value") #tell the user to reenter their input
else: #if the activeProgram boolean is False, which can only be done through the elif roll == "x"
	print("leaving program") #tell the user they are leaving the program
	exit() #leave the program"
```

## Python Program 01 – Calculator
A calculator with 5 different operators and two different numbers, all based off user input. The input mechanism was similar to the one on Hello Python above, but since the inputs were two integers and then an operator, I first treated them all like strings. Then with the operators, I matched the string of the operator with the actual operation. Finally with the integers, I just put them into an int() before sticking them into the function.
```ruby
def doMath(numOne,numTwo,operation): #the doMath function, with the input points named numOne,numTwo, and operation respectively
	if operation == "-": #if the string input is "-" then
		return numOne - numTwo #subtract numTwo from numOne and return the answer
	elif operation == "+": #if the string input is "+" then
		return numOne + numTwo #add numTwo to numOne and return the answer
	elif operation == "*": #if the string input is "*" then
		return numOne * numTwo #multiply numOne by numTwo and return the answer
	elif operation == "/": #if the string input is "/" then
		divNum = numOne / numTwo #divide numOne by numTwo and save the answer as divNum
		roundedNum = round(divNum, 2) #round that answer to two decimal places
		return roundedNum #return the rounded answer
	elif operation == "%": #if the string input is "%" then
		return numOne % numTwo #divide numOne by numTwo, determine the remainder, and save the answer 
	else:
		return "invalid operator syntax" #if the input for operation does not match one of these above, then it was imputed incorrectly
numberOne = int(input("First number:\n")) #Print First number:, then skip a line and wait for user input, which is converted into an integer
numberTwo = int(input("Second number:\n")) #Print Second number:, then skip a line and wait for user input, which is converted into an integer
```
With all that, the user is prompted with the input(), where the quotations in the brackets appear as text for the user to see. The function runs and the results are then printed and the program ends.

## Python Program 02 – Quadratic Solver
A basic quadratic solver with three coefficient inputs, which first determines if there are real roots, by taking the discriminant, and if it does exist, puts the roots into an array and returns the roots. The bulk of the code is the quadSolver function, which first determines the discriminant, b^2 -4ac, and since the square root of the discriminant is then determined, the only way to get a real root(i is non-real) is for the discriminant to be greater than or equal to 0. For non real roots, it returns "No real roots," but for real roots it first creates an empty array called roots, and adds the two roots to them, which is then returned and printed. I also had to import math, as Python doesn't have a built in square root function.
```ruby
import math #imports a math module with a square root function, which Python does not have
def quadSolver(co1,co2,co3): #quadSolver function, with 3 inputs
	discrim = (co2 ** 2)-(4 * co1 * co3) #find the discriminant, b^2 - 4ac 
	if discrim < 0: #if the discriminant is less than 0, you are finding the square root of a negative number which is non-real
		return "No real roots" #tell the user that there are no real roots
	else: #if the discriminant is greater than or equal to 0
		roots = [] #create an empty array called roots
		roots.append(((-1 * co2) - (math.sqrt(discrim))) / (co1 * 2)) #plug the coefficients into the quadratic formula, and add the root to the array
		roots.append(((-1 * co2) + (math.sqrt(discrim))) / (co1 * 2)) #plug the coefficients into the quadratic formula, and add the root to the array
		return roots #return the array
```

## Python Program 03 – Strings and Loops
A program to take sentences and print them vertically with minus signs replacing spaces. However, we were also tasked to do this by using arrays and for loops. Initially I had problems when I tried printing the arrays, where only the first word would print and nothing else, before I realized that the .split() built in python function automatically creates an array. I also made use of another built in python function, the .replace() function which replaces all instances of something with something else. In my case, I did it to create the minus sign between the words, because the .split() function gets rid of all spaces, so I had to use the .replace() before the .split(). Then I used the for loop, which takes items inside of an array, to go deeper into the array, eventually to the letters themselves, which were finally prined.
```ruby
def takeapart(sen): #takeapart fucntion, with a variable called sen
	sen = sen.replace(" ", "- ") #replace all instances of spaces with a dash and then the space, so that later at the end of each word will be a minus sign
	words = sen.split() #split the words wherever there is a space, and create an array with the list called word
	for word in words: #for the items, each indidual word, in the array words
		for letter in word: #for the items, each individual letter, in the array word
			print(letter) #print the letters
```

## Python Challenge – MSP
A hangman function! It was really fun to play around and tinker with. Beyond the bare minimum hangman, I allowed the user to choose difficulty, meaning how many guesses they got, told the user all they guesses they made, and if they didn't guess the word, I told them what the word was in the end. The program is based almost completely on functions, of which there are 4 in the program: a hangman shape creating function, a word encoding function, a guess loging function, and a word search function. The hardest of the 4 was the word search function of which the hardest part was when the user guessed correctly. To do this, the function loops through all the letters of the word and stores the letter number at which the guess is. Then the function updates the original blank (full of dashes) word by deleting the dashes at the correct index and inserting the guess in their place.
```ruby
if guess in word: #if the user's guess is in the word
	print("Got one!") #print Got one!
	for i in range(len(word)): #loop through this function the number of times equal to the length of the word
		if word[i] == guess: #as i counts up from 0 to the length of the word, check each letter of the word, by looking at index i, to see if it matches the guess
			guessPos.append(i) #if the guess matches a letter at index i, add the number of i to guessPos
	for i in range(len(guessPos)): #loop through this function how ever many times the guess was inside the wod
		del blankWordList[guessPos[i]] #delete a dash from blankWordList at the index that the correct guess appeared
		blankWordList.insert(guessPos[i],guess) #add the correct guess to blankWordList at the index that the correct guess appeared
	blankWord = ''.join(map(str, blankWordList)) #blankWord is equal to the string of blankWordList
	print(blankWord) #print blankWord, which is the dashes with updated correct guesses
```
Then to keep the program going, and allow the user to keep making guesses the program must pass 2 criteria, first that the number of wrong guesses does not equal the number of guesses to make the hangman, and second that the originally blank word that is updated with correct guesses does not equal the starting word. It also runs through the guessLog function to make sure that all gueses are unique and not repeateed.
```ruby
while numberWrong < endCrit and blankWord != secretWord: #while the number of wrong guess does not equal the end criteria (above) and the blankWord (dashes replaced with guesses) does not equal secretWord
	newGuess = input("Player 2, please guess a letter:\n") #player 2 is prompted to enter a guess
	if guessLog(newGuess) == False: #guessLog is run with the guess and if it returns false, meaning this is a repeat guess
		print("You have already guessed that, please input a new guess") #tell the user it is a repeat guess and ask them to enter another
	else: #if guessLog does not return false, meaning this is a unique guess
		wordSearch(newGuess) #run wordSearch function with the guess
```

## GPIO Pins – Bash
A simple progam, but a very nice introduction to hardware and Bash. The wiring was very simple, with just two leds, and Bash was also very simple with a very basic for loop. Bash itself has slightly different syntax than Python, but all the same logic applies, so all I had to do was become familiar with the exact Bash syntax.
```ruby
for i in {1..10} #loop 10 times
do #do this for the loop
	gpio write 0 0 #Turn pin 0 off
	gpio write 2 0 #Turn pin 2 off
	sleep 1 #Wait 1 second
	gpio write 0 1 #Turn pin 0 on
	gpio write 2 1 #Turn pin 2 on
	sleep 1 #Wait 1 second
done #end the loop
```
[Video of it working](https://drive.google.com/file/d/1PnNx3qf194lGCICYVwvdoQJYG4Jole6H/view)

## GPIO Pins - Python
The exact same program as GPIO Pins - Bash, but this time using Python syntax, which I'm more comfortable with. The wiring was the same, and I also used a for loop, so I just reused the video from GPIO Pins - Bash, as everything physical was exactly the same. This time, however, I had to import two Python libraries to make the GPIO pins work, and reduce excess code. 
```ruby
from gpiozero import LED #from the gpiozero library, import the function LED
from time import sleep #from the time library, import the function sleep
for i in range(10): #loop this 10 times
	led1.on() #turn led1 on
	led2.on() #turn led2 on
	sleep(1) #wait 1 second
	led1.off() #turn led1 off
	led2.off() #turn led2 off
	sleep(1) #wait 1 second
```

[Video of it working (reused from GPIO Pins - Bash)](https://drive.google.com/file/d/1PnNx3qf194lGCICYVwvdoQJYG4Jole6H/view)

## GPIO Pins - SSH
My first time remotely running an application, albeit one that was two lines long! This assignment should have been very straightforward but I initially struggled with connecting to my pi on the Seure Shell App, as I mistakenly though the hostname of the application was "raspberrypi" and not my ip address, eventually though I figured out my issue and the rest of the assignment was a breeze, just initiallizing the pins, and then turning them on / off.

[Video of it working](https://drive.google.com/file/d/1QUJS4yOZbOzWK4icZdXCIiUZ8wNOO8D1/view)

## GPIO Pins - I2C
A very challenging but fun assignment mashing together Adafruits's SSD1306 Display and LSM303 Accelerometer. My biggest problem I had was when I displayed my data it would display on top of itself, meaning you could never read what it said, eventually though I figured out that if I printed a black rectangle at the beginning of the loop and then added a bit of a delay at the end it would work. In addition I learned the very vaulable skill of copy pasting in Beagle Term. On Chrome you copy with ctrl+c and paste with ctrl+v, but in Beagle term you copy with ctrl+shift+c and paste with ctrl+shift+v, meaning that if I want to copy something in Chrome and paste it into Beagle Term I would first use ctrl+c and then ctrl+shift+v.
```ruby
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
```

[Video of it working](https://drive.google.com/file/d/1W_XgL-uXAwXyuA7x7YuOWgVFWfFJRDs9/view)

## Headless
A simple assignment that took a lot longer than it should have. Basically all that I needed to do was to create a simple graphical display of one the three variables, x, y, or z, which I did fairly quickly but then I ran straight into the brick wall of rc.local. The final step of the assignment was to make the program run without a physical connection to the computer so I tried to edit rc.local to make the program run whenever connected to power, but something on my pi was stopping that from happening. Eventually I ditched that and just used an SSH connection to run which worked perfectly. For the graph itself I just had to determine the general range of z which usually was between 11 and -11, and then convert that into heights which was displayed as a moving line on a sort of bar graph. 
```ruby
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
```


[Video of it working](https://drive.google.com/file/d/13DM5EzGyQQwg0XanCdZkBzn4OGdrrC4v/view)

## Hello Flask
A quick and easy assignment learning how to use Flask and set up a web server on my pi! A few short lines set up the app.py, and then ran the hello world function. Then any device on my internet typed in the pi's ip address and ran the function.
```ruby
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
     return "hello world!"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
```

[Video of it working](https://drive.google.com/file/d/1nUV2RZbNNgAsf7K5HblyD9K9FvmR7Tun/view)

## GPIO PINS - Flask
A slightly tricky assignment turning the Raspberry Pi into web server that can control two leds over the internet. On the main program, app.py, I first had to figure out how to create two buttons using the one POST method, which I did by first testing whether POST had occured, indicating a click of some button, and then testing the value of one of the buttons and thus determing which was clicked. Initially I only had it so that only one button could be on at a time, and you couldn't turn off both lights once one was on, because I repeatedly got an error called "local variable referenced before assignment" when I tried to store and then modify the value of the lights. I tried turning the variables into global variables and then nonlocal variables, but nothing was working before I eventually realized that a. global variables must be created and then stored with information and b. a gloabl variable outside of a function, must be reinitalized as a global variable inside of a function. Finally I could turn both lights on at the same time, but I couldn't turn them off. So, I created a secondary if statement after the inital button state tests to determine whether the light was already on when the button was pressed, and if so to turn off the light. In the html template, I created two buttons seperated by the messages referenced in app.py. Finally, I changed the background color and text color inside <style>.
	
```ruby
<style>
body {
  background-color: cyan;
  color: red;
}
</style>
<body>
{{msg1}}
<form method="POST">
     <button type="submit" name="submitBtn1" value="You Turned on the Green Light!">Click to Turn on/off the Green Light!</button>
     <br>{{msg2}}
     <br><button type="submit" name="submitBtn2" value="You Turned on the Red Light!">Click to Turn on/off the Red Light!</button>
</form>
</body>
```
```ruby
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
 ```
[Video of it working](https://drive.google.com/file/d/1gxTqLx5-orizdu3gGBTxr56LiICMIlUg/view)

## Pi Camera
A fun and easy introduction to the Pi Camera that unfourtanetly got sidetracked. After completing the code my interent went out for about 2 weeks, stopping me from finishing the assignment, but I could not be deterred and finally got it working! For the assignment itself, the first camera test was done simply with the import of "time" and "picamera." The second camera test was slightly more complicated, but easily solved using Python lists, moving between the items and repeating the picture taking structure with i in range. 

```ruby
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
```

![Pic1](https://github.com/CamdenBaucom/Engineering_4_Notebook/blob/main/Python/Pictures/pic1.jpg)
    
```ruby
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
```

![FilterPic0](https://github.com/CamdenBaucom/Engineering_4_Notebook/blob/main/Python/Pictures/filterpic0.jpg)
![FilterPic1](https://github.com/CamdenBaucom/Engineering_4_Notebook/blob/main/Python/Pictures/filterpic1.jpg)
![FilterPic2](https://github.com/CamdenBaucom/Engineering_4_Notebook/blob/main/Python/Pictures/filterpic2.jpg)
![FilterPic3](https://github.com/CamdenBaucom/Engineering_4_Notebook/blob/main/Python/Pictures/filterpic3.jpg)
![FilterPic4](https://github.com/CamdenBaucom/Engineering_4_Notebook/blob/main/Python/Pictures/filterpic4.jpg)


## Copypasta
Two offical Raspberry Pi sponsered assignments that were pretty straightforward but more difficult than expected on a Chromebook. The first assignment, an infared motion sensor that recorded when it detected a change in temperature, was pretty simple except that the file of what the video had captured wouldn't display from the terminal. So, I had to push it to GitHub, download it, and then, since it still wouldn't display, put it through a sketchy online video converter to make it a .mp4. The second assignment, a push button stop motion, was difficult because a. I didn't have a button, and b. I couldn't see what the camera was capturing (because it wouldn't display on the terminal) until the whole stop motion was done. So, I created a make shift button, by plugging one wire into ground and another into the input and then touching the wires together when I wanted to complete the circuit (aka push the button). I then taped my Raspberry Pi Camera to a coffee mug, and then used my phone to appoximate what the Camera was seeing, before finally filming the first couple moves of a chess game. It turned out pretty well, with the only downside being that my makeshift button had captured over 450 frames, when I had thought I had captured about 50.

[Video of the "intruder detector"](https://drive.google.com/file/d/1YXLLjRcdM6trrKUx9GfEQ7qMQNhIovOo/view)

[Video of the animation](https://drive.google.com/file/d/1cJ5scLkEBMyj2W6Qv-T-p-jMO55xEbqN/view)
