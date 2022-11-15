from machine import Pin, PWM
import utime

#Defining LEDs and Pins
trigger = Pin(14, Pin.OUT)
echo = Pin(13, Pin.IN)

led = PWM(Pin(15))
led.freq(1000)

#Create a function that contains the code
def ultra():
#Pull trigger low to unactive, pause. Pull trigger high to send pulse, pause, then trigger low again.
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
#While loop checks for the echo pin
    while echo.value() == 0:
        signaloff = utime.ticks_us()
 #While loop checks if echo has been recieved
    while echo.value() == 1:
        signalon = utime.ticks_us()
 #create variable for the time taken for pulse to hit objects and return
    timepassed = signalon - signaloff
#multiply by speed of sound and divide by 2 to only find the distance to the object
    distance = (timepassed * 0.0330) / 2
#print distance
    print("The object can be seen from a distance of", distance, "cm")
#create specific ranges, within each range the brightness of LED differs (brighter if when distance is smaller)
    if distance < 5.000:
        for duty in range(65025):
            led.duty_u16(duty)
        utime.sleep(0.000001)
    elif 5.000 < distance < 10.000:
        for duty in range(65025):
            led.duty_u16(30000)
            utime.sleep(0.0000001)
    elif 10.000 < distance < 25.000:
        for duty in range(65025):
            led.duty_u16(20000)
            utime.sleep(0.0000001)
    elif 25.000 < distance < 40.000:
        for duty in range(65025):
            led.duty_u16(10000)
            utime.sleep(0.0000001)
    elif 40.000 < distance < 60.000:
        for duty in range(65025):
            led.duty_u16(2000)
            utime.sleep(0.0000001)
    else:
        for duty in range(65025):
            led.duty_u16(0)
            utime.sleep(0.00000001)
 #Run function continuosly
while True:
    print("loop")
    ultra()
    utime.sleep(0.005)
