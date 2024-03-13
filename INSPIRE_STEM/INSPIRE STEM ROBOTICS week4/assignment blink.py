from machine import Pin
from utime import sleep

print("Hello, ESP32!")

red_led = Pin(15, Pin.OUT)
blue_led = Pin(13, Pin.OUT)
green_led = Pin(12, Pin.OUT)
buzzer = Pin(2, Pin.OUT)

blue_led.on()
sleep(2)
blue_led.off()                
      
red_led.on()
sleep(2)
red_led.off()

green_led.on()
sleep(2)
green_led.off()   

for x in range(0,5):
  buzzer.on()
  sleep(5)
  buzzer.off()  

