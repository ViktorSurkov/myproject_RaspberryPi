# Imports
import webiopi
GPIO = webiopi.GPIO

PWM=27


# Called by WebIOPi at script loading
def setup():
    GPIO.setFunction(PWM, GPIO.PWM);
    GPIO.pwmWriteAngle(PWM, 0)

# Called by WebIOPi at server shutdown
def destroy():
    webiopi.debug('Blink script - Desrtoy');
    GPIO.setFunction(PWM,GPIO.IN);
