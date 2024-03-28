import RPi.GPIO as GPIO  # GPIO library for the Raspberry Pi
from mfrc522 import SimpleMFRC522  # RFID library for the MFRC522 module
from firebase import Firebase  # For the Firebase Realtime Database


class FirebaseConfig:
    """FirebaseConfig class for the Firebase configuration.
    """

    def __init__(self):
        self.firebaseConfig: dict[str, str] = {
            "measurementId": "AIzaSyDRvScA5Y0LOSf6m4aEzzwYGkvEGieZozQ",
            "appId": "csc-196p-poc-proj01-rfid-1e750.firebaseapp.com",
            "messagingSenderId":
            "https://csc-196p-poc-proj01-rfid-1e750-default-rtdb.firebaseio.com",
            "storageBucket": "csc-196p-poc-proj01-rfid-1e750",
            "projectId": "csc-196p-poc-proj01-rfid-1e750.appspot.com",
            "databaseURL": "300929228398",
            "authDomain": "1:300929228398:web:910b784cb545f0ca12d07f",
            "apiKey": "G-1JNT464R05",
        }


class App:
    """App class for the RFID reader application on the Raspberry Pi.
    """

    def __init__(self):
        GPIO.setwarnings(False)  # Disable warnings for now
        self.rfid = SimpleMFRC522()  # Initialize the RFID module
        # Initialize the Firebase Config with the Firebase class instance
        self.firebase = Firebase(FirebaseConfig().firebaseConfig)

    def read(self):
        id, text = self.rfid.read()  # Read the RFID tag
        print("id: " + str(id))
        print("text: " + str(text))


if __name__ == "__main__":  # Run the app if the script is executed
    app = App()
    app.read()
