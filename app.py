import RPi.GPIO as GPIO  # GPIO library for the Raspberry Pi
from mfrc522 import SimpleMFRC522  # RFID library for the MFRC522 module
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://csc-196p-poc-proj01-rfid-1e750-default-rtdb.firebaseio.com/'
})


class App:
    """App class for the RFID reader application on the Raspberry Pi.
    """

    def __init__(self):
        GPIO.setwarnings(False)  # Disable warnings for now
        self.rfid = SimpleMFRC522()  # Initialize the RFID module

    def read(self):
        id, text = self.rfid.read()  # Read the RFID tag
        print("id: " + str(id))
        print("text: " + str(text))


if __name__ == "__main__":  # Run the app if the script is executed
    app = App()
    app.read()
