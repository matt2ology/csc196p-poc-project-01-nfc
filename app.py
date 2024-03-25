import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
rfid = SimpleMFRC522()

while True:
    id, text = rfid.read()
    print("id: " + str(id))
    print("text: " + str(text))
