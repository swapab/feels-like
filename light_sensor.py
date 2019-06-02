#!/usr/local/bin/python

# from Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO
import time

__author__ = 'Swapnil'
__license__ = "GPL"
__maintainer__ = "swapab.space"

#GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
pin_to_circuit = 4 #7
adj=2.130620985
cap=0.000001
def rc_time (pin_to_circuit):
    count = 0
    print("rc_time")
    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
    starttime=time.time()
    endtime=time.time()
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        # print(GPIO.input(pin_to_circuit))
        # count += 1
        endtime=time.time()

    # return count
    return (endtime - starttime)

def calculate_resistance():
    return int(((rc_time(pin_to_circuit)/cap)*adj)/10000)

def print_resistance():
  #Catch when script is interupted, cleanup correctly
  try:
      # Main loop
      while True:
          result = calculate_resistance()
          #lcd.clear()
          #lcd.message('LDR Reading: \n {result}' )
          print(result)
          # print(rc_time(pin_to_circuit))
  except KeyboardInterrupt:
      pass
  finally:
      GPIO.cleanup()

#print_resistance()
