import sys, time    #import system settings and time libraries

import RPi.GPIO as GPIO     #import the RPi GPIO library (and give it a namespace of "GPIO")

GPIO.setmode(GPIO.BOARD)    #set GPIO naming convention to "Board" convention rather than "BMC" convention

 pinOut = {'rPin':11, 'gPin':13, 'bPin':15}  #defineGPIO Pin outputs

#On/Off functions

def pinHigh(pin):
    GPIO.setup(pin, GPIO.OUT)   #set GPIO 'pin' to 'output' (rather than input)
    GPIO.output(pin, GPIO.HIGH) #set pin to "high" (on) - sending 3.3v ("low" is 0v - "off")

def pinLow(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  #set pin to "low" (off, sending 0v)

#LOGIC

flashCounter = 0    #incremental counter, + total number of flashes req'd
flashTotal = 10

print("Led Test Beginning... YEEEWW")

try:    #main logic exists within 'try, while, except, finally' loop

    while True:     #while program runs ie "always until cancelled"
        cmd = input("Hi! Wow! Let's make some LED's happen! Type a command! (red, blue, green) (on, off)")

        if cmd == "red on":
            pinLow(pinOut['rPin'])
            print("Woo! Red On!")

        elif cmd == "green on":
            pinLow(pinOut['gPin'])
            print("Yeah! Green On!")

        elif cmd == "blue on":
            pinLow(pinOut['bPin'])
            print("Yissss! Blue On!")

        elif cmd == "red off":
            pinHigh(pinOut['rPin'])
            print("Awh. Red Off.")

        elif cmd == "green off":
            pinHigh(pinOut['gPin'])
            print("Okay :( Green Off.")

        elif cmd == "blue off":
            pinHigh(pinOut['bPin'])
            print("Buh. Blue Off.")

        else:
            print("Invalid command :(")


    """
    while flashCounter < flashTotal:
        flashCounter += 1
        testOn()
        time.sleep(0.5)
        print("Flashed ", flashCounter, "times")
        testOff()
        time.sleep(0.5)

    print("Target reached:", flashTotal)
    """

except KeyboardInterrupt:
    print("CTRL-C pressed.")

#    except:
#        print("Other error or exception occurred!" #commented out as this will override error codes

finally:
    GPIO.cleanup() #resets all GPIO pins to inputs
    print("GPIO.cleanup() called. Yay!")

