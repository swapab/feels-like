#!/usr/bin/env python

from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
from light_sensor import calculate_resistance
import RPi.GPIO as GPIO
import time

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19,
                               d4=13, d5=6, d6=5, d7=11,
                                                      cols=16, lines=2)
lcd.clear()

# display text on LCD display \n = new line
lcd.message('Welcome Sweetie Pi\n' + str(time.strftime("%d-%m-%y @ %H:%M")))
sleep(3)

# scroll text off display
for x in range(0, 16):
   lcd.move_right()
   sleep(.1)
   sleep(.5)

# scroll text on display
for x in range(0, 16):
   lcd.move_left()
   sleep(.1)

sun_storm = 50
sunny = 150
bright = 300
evening = 450
dark = 500

def display_resistance():
  #Catch when script is interupted, cleanup correctly
  try:
      # Main loop
      while True:
          result = calculate_resistance()
          lcd.clear()
          lcd.message('  Feels Like: \n ')
          if(result <= sun_storm):
              lcd.message(' Sun Storm !!!')
          elif(result > sun_storm and result <= sunny):
              lcd.message('Bright Sunny Day')
          elif(result > sunny and result <= bright):
              lcd.message('Sunny with clouds')
          elif(result > bright and result <= evening):
              lcd.message(' Evening ')
          elif(result > evening and result <= dark):
              lcd.message(' Dark')
          elif(result > dark):
              lcd.message(' Bat-Man ')
          else:
            lcd.message(str(result))
          print(result)
  except KeyboardInterrupt:
      pass
  finally:
      lcd.clear()
      lcd.message(' Good Bye \nSee you later')
      GPIO.cleanup()

display_resistance()
