from gpiozero import LED, Button, Buzzer
from signal import pause
from time import sleep


Red = LED(17)
Yellow = LED(27)
Green = LED(22)
button = Button(14)
buzzer = Buzzer(15)
Blue =LED(18)
Orange= LED(21)

while True:
    if button.is_pressed:
        Orange.on()
        Blue.on()
        buzzer.on()
        Red.on()
        sleep(5)
        
        
        
        
    else:
        Orange.off()
        Blue.off()
        buzzer.off()
        
        Red.on()
        sleep(3)
        Red.off()
        sleep(1)
        print("Red is on")
            
        Yellow.on()
        sleep(3)
        Yellow.off()
        sleep(1)
        print("Yellow is on")
        
         
        Green.on()
        sleep(3)
        Green.off()
        sleep(1)
        print("green is on")
        
      
    

    

pause()
