from machine import Pin, I2C
import ssd1306

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
buzzer = Pin(17, Pin.OUT)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('ROZINA AND SYNTHIA', 10, 10)      
oled.show()

for x in range(0,5):
  buzzer.on()
  sleep(5)
  buzzer.off()  