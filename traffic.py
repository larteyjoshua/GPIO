from gpiozero import LED, Button
from signal import pause
from time import sleep


Red = LED(17)
Yellow = LED(27)
Green = LED(22)
button = Button(2)

def delay():
    Red.on
    Yellow.on
    Green.on
    sleep(5)
button.when_pressed = delay

def traffic():
    while True:
        Red.on()
        sleep(3)
        Red.off()
        sleep(1)
            
        Yellow.on()
        sleep(3)
        Yellow.off()
        sleep(1)
            
        Green.on()
        sleep(3)
        Green.off()
        sleep(1)


button.when_released= traffic

    


pause()