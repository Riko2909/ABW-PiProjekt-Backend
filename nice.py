import os
import time
import random as rnd


if os.name == 'nt':
      os.system('cls')
else:
      os.system('clear')


print('''

 888b     d888          d8b               888b     d888          d8b          888                    
 8888b   d8888          Y8P               8888b   d8888          Y8P          888                    
 88888b.d88888                            88888b.d88888                       888                    
 888Y88888P888  .d88b.  888 88888b.       888Y88888P888  .d88b.  888 .d8888b  888888 .d88b.  888d888 
 888 Y888P 888 d88""88b 888 888 "88b      888 Y888P 888 d88""88b 888 88K      888   d8P  Y8b 888P"   
 888  Y8P  888 888  888 888 888  888      888  Y8P  888 888  888 888 "Y8888b. 888   88888888 888     
 888   "   888 Y88..88P 888 888  888      888   "   888 Y88..88P 888      X88 Y88b. Y8b.     888     
 888       888  "Y88P"  888 888  888      888       888  "Y88P"  888  88888P'  "Y888 "Y8888  888     


''')

liste = []
listrange = 10

CLR =  "\x1B[0K"
UP  = f"\x1B[{listrange}A"

counter = 0

animatestring = "<=== Script wird Ausgeführt ===>"

def arrow():
      print(f"\x1B[12A")

      global counter

      counter = counter + 1
      
      if counter < len(animatestring) + 1:
            for i in range(counter):
                  print(f"{animatestring[i]}{CLR}", end='')
      
      print("\x1B[10B")

      if counter > 50:
            counter = 0


for i in range(1000):

      x = rnd.randrange(10000)
      
      liste.append(x)

      if len(liste) >= listrange:
            liste.pop(0)
            print(UP)
            for i in range(len(liste)):
                  print(f"{liste[i]}\t {liste[i]}\t {liste[i]}\t {liste[i]}\t {liste[i]}\t {liste[i]}\t {liste[i]}\t {liste[i]}\t {liste[i]}\t {CLR}")
            
            arrow()
      else:
            print(f"{x}\t {x}\t {x}\t {x}\t {x}\t {x}\t {x}\t {x}\t {x}\t ")

      time.sleep(0.1)
