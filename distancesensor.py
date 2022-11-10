from machine import Pin, PWM
import utime
trigger = Pin(14, Pin.OUT)
echo = Pin(13, Pin.IN)

led = PWM(Pin(15))
led.freq(1000)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0330) / 2
    print("The object can be seen from a distance of", distance, "cm")
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
while True:
    print("loop")
    ultra()
    utime.sleep(0.005)
