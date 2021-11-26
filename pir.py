import RPi.GPIO as GPIO
import time
import os

import json
import requests 

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

GPIO.setmode(GPIO.BCM)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
voltageMax = 5
# Create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)

R = 20 # R
G = 21 # G
B = 16 # B

def init_LED():
  GPIO.setup(G, GPIO.OUT)
  GPIO.setup(R, GPIO.OUT)
  GPIO.setup(B, GPIO.OUT)


def clear():
  GPIO.output(R, GPIO.LOW)
  GPIO.output(G, GPIO.LOW)
  GPIO.output(B, GPIO.LOW)

init_LED()

def payload_translator(key):
  if(key):
    return GPIO.HIGH
  else:
    return GPIO.LOW

def clear():
  GPIO.output(R, GPIO.LOW)
  GPIO.output(G, GPIO.LOW)
  GPIO.output(B, GPIO.LOW)

def luxColor_translator(value):

  clear()

  if value > 50:
    GPIO.output(R, GPIO.HIGH)

  if value > 160:
    GPIO.output(G, GPIO.HIGH)

  if value > 260:
    GPIO.output(B, GPIO.HIGH)
  

package = { "voltage" : 0 }
headers = {'content-type': 'application/json'}

os.system('clear')
print('''
   ______   __         ______         _______   ________   ______    ______   ________ 
  /      \ /  |       /      \       /       \ /        | /      \  /      \ /        |
 /$$$$$$  |$$ |      /$$$$$$  |      $$$$$$$  |$$$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$$$$$/ 
 $$ |__$$ |$$ |      $$ |  $$/       $$ |__$$ |$$ |__    $$ |__$$ |$$ |  $$/    $$ |   
 $$    $$ |$$ |      $$ |            $$    $$< $$    |   $$    $$ |$$ |         $$ |   
 $$$$$$$$ |$$ |      $$ |   __       $$$$$$$  |$$$$$/    $$$$$$$$ |$$ |   __    $$ |   
 $$ |  $$ |$$ |_____ $$ \__/  |      $$ |  $$ |$$ |_____ $$ |  $$ |$$ \__/  |   $$ |   
 $$ |  $$ |$$       |$$    $$/       $$ |  $$ |$$       |$$ |  $$ |$$    $$/    $$ |   
 $$/   $$/ $$$$$$$$/  $$$$$$/        $$/   $$/ $$$$$$$$/ $$/   $$/  $$$$$$/     $$/  

 Amazing Light Control Reactive
 ABW-Projekt von Riko Gerdes (02.11.2021) 


''')



liste = []
listrange = 10

CLR =  "\x1B[0K"
UP  = f"\x1B[{listrange}A"

counter = 0

animatestring = "<=== Script wird Ausgeführt ===>"

def arrow():
      print(f"\x1B[{listrange + 3}A")

      global counter

      counter = counter + 1
      
      if counter < len(animatestring) + 1:
            for i in range(counter):
                  print(f"{animatestring[i]}{CLR}", end='')
      
      print(f"\x1B[{listrange + 1}B")

      if counter > 50:
            counter = 0

print(f"Color RED\t| Color GREEN\t| Color BLUE\t| Lichtwert\n----------------+---------------+---------------+-------------------")
try:
    while True:

        package["voltage"] = chan0.voltage * 100

        try:
            payload = requests.post('http://localhost:3001', data=json.dumps(package), headers=headers, timeout=40).json()
            
            # print(payload)

            if len(payload['settings']) < 1:
              print("Empty Payload...")
            else:
              # print(f"Received Payload: {payload['settings']}")
              x = (f"{CLR}{payload['settings']['colorwheel']['r']}\t\t| {payload['settings']['colorwheel']['g']}\t\t| {payload['settings']['colorwheel']['b']}\t\t| {package['voltage']} ")

              liste.append(x)


              if len(liste) >= listrange:
                liste.pop(0)
                print(UP)
                for i in range(len(liste)):
                  print(liste[i])
                arrow()
              else:
                print(x)

              if payload['settings']['manualState'] is True:
                GPIO.output(R, payload_translator(payload['settings']['colorwheel']['r']))
                GPIO.output(G, payload_translator(payload['settings']['colorwheel']['g']))
                GPIO.output(B, payload_translator(payload['settings']['colorwheel']['b']))
              else:
                luxColor_translator(package["voltage"])

            time.sleep(0.5)
        except Exception as exeption:
            x = (f"{CLR}-\t\t| -\t\t| -\t\t| {package['voltage']} {CLR}")

            liste.append(x)

            if len(liste) >= listrange:
              liste.pop(0)
              print(UP)
              for i in range(len(liste)):
                print(liste[i])
              arrow()
            else:
              print(x)

            luxColor_translator(package["voltage"])
            time.sleep(0.1)



except KeyboardInterrupt:
  print("\n")
  GPIO.cleanup()

