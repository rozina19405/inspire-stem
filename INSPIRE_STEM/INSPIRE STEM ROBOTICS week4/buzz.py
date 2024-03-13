from machine import Pin
from time import sleep
buzzer = Pin (16, Pin.OUT)

for x in range(0,5):
  buzzer.on()
  sleep(5)
  buzzer.off()  