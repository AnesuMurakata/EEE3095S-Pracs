#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Anesu Murakata>
Student Number: <MRKANE001>
Prac: <Prac 1>
Date: <1/8/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

#GPIO port number lists
sequenceList =list(product([0,1], repeat=3))
inputList = [29, 31]       #input port numbers
outputList = [11, 13, 15]   #output port numbers

def main():
	print("Executing Program")
	counter = 0 #counter variable for progression in bit counter 
	sleep(1)
	func = GPIO.gpio_function(31)
	print(func)
	func2 = GPIO.gpio_function(33)
	print(func2)
	
	while(True):
		#if decrement button is pressed
		if GPIO.event_detected(31):  #listen for event(button press) on port 31
			counter = counter-1
			if counter == -1:
				counter=7    #implement wrap around if it gets to 0
			print(sequenceList[counter])
			GPIO.output(outputList, sequenceList[counter])    #display counter value on LED's
			sleep(.1)
			print("Decrement button is working")	
			
		#if increment button is pressed
		if GPIO.event_detected(29):   #listen for event(button press) on port 29
			counter = counter+1
			if counter == 8:
				counter=0   #implement wrap around if it gets to 7
			print(sequenceList[counter])
			GPIO.output(outputList, sequenceList[counter])    #display counter value on LED's
			sleep(.1)
			print("Increment button is working")
		sleep(1)

# Only run the functions if 
if __name__ == "__main__":
	# Make sure the GPIO is stopped correctly
	try:
		#initialising mode out of main loop so it does not iterate	
		GPIO.setmode(GPIO.BOARD)
		
		 #list of GPIO set to output
		GPIO.setup(outputList, GPIO.OUT, initial=GPIO.LOW)
	
		#List of GPIO set to input
		GPIO.setup(inputList, GPIO.IN)
		GPIO.setup(inputList, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
		#add edge detection and debouncing, out of loop to avoid error 
		GPIO.add_event_detect(29, GPIO.RISING, bouncetime=200)
		GPIO.add_event_detect(31, GPIO.RISING, bouncetime=200)

	while (True):
		main()
	except KeyboardInterrupt:
		print("Exiting gracefully")
	    # Turn off your GPIOs here
	        GPIO.cleanup()
	except Exception as e:
		GPIO.cleanup()
		print("Some other error occurred")
		print(e.message)