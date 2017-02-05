from machine import Pin
from time import sleep_ms as delay
from machine import ADC

#IP: 10.75.126.117
# Senha: twtw


# Mudar o led que pisca
# Piscar dois leds 
# Piscar os 3 leds
# Piscar cinco leds
# Piscar todos os leds

def blink():
    
    
    led = Pin(15, Pin.OUT)#  led 1
    led1 = Pin(14, Pin.OUT)# led 4
    led2 = Pin(16, Pin.OUT)# led 8
    led3 = Pin(13, Pin.OUT)# led 2
    led4 = Pin(12, Pin.OUT)# led 3
    led5 = Pin(5, Pin.OUT)# led 7
    led6 = Pin(4, Pin.OUT) #led 6
    led7 = Pin(0, Pin.OUT) #led 5
    pot = ADC(0)
    

    while True:
        a=pot.read()
        led.high()
        delay(a)
        led.low()

        
        led3.high()
        delay(a)
        led3.low()
        
        
        led4.high()
        delay(a)
        led4.low()
        
        
        led1.high()
        delay(a)
        led1.low()
        
        
        led7.high()
        delay(a)
        led7.low()
        
        
        led6.high()
        delay(a)
        led6.low()
        
        
        led5.high()
        delay(a)
        led5.low()
        
        
        led2.high()
        delay(a)
        led2.low()