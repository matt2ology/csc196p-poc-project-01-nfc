import math
import sys
from firebase_admin import credentials  # Firebase Admin SDK credentials
from firebase_admin import db  # Firebase Realtime Database
from mfrc522 import SimpleMFRC522  # RFID library for the MFRC522 module

import firebase_admin  # Firebase Admin SDK for Python
import os  # Operating system library for file path manipulation
import RPi.GPIO as GPIO  # GPIO library for the Raspberry Pi
import time  # Time library for sleep function and time manipulation


class Firebase:
    """Firebase class for the RFID reader application on the Raspberry Pi.
    """

    def __init__(self):
        # Initialize Firebase Admin SDK with service account credentials
        self.cred = credentials.Certificate(
            os.path.normpath(
                os.path.join(
                    os.path.dirname(__file__),
                    'firebaseServiceAccountKey.json')
            )
        )  # Service account credentials for the Firebase project in JSON
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://csc-196p-poc-proj01-rfid-1e750-default-rtdb.firebaseio.com/'
        })  # Initialize the Firebase Realtime Database

    def write(self, id: int, text: str) -> None:
        """Write the RFID tag ID and text to the Firebase Realtime Database.

        Args:
            id (int): _description_
            text (str): _description_
        """
        db.reference(str(text)).set({
            'id': id,
            # Human-readable timestamp for the current date and time
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        })

    def clear_all_data_from_database(self) -> None:
        """Clear all data from the Firebase Realtime Database.
        """
        db.reference().delete()

    def check_if_database_is_empty(self) -> bool:
        """Check if the Firebase Realtime Database is empty.

        Returns:
            bool: True if the database is empty, False otherwise.
        """
        return db.reference().get() is None


class RfidTags:

    def __init__(self):
        self.rfid_card_id_type: str = "Card"
        self.rfid_card_id: int = 623143366549
        self.rfid_card_is_scanned: bool = False
        self.rfid_key_fob_id_type: str = "Key Fob"
        self.rfid_key_fob_id: int = 1020731053017
        self.rfid_key_fob_is_scanned: bool = False

    def get_rfid_key_fob_id(self) -> int:
        return self.rfid_key_fob_id

    def get_rfid_card_id(self) -> int:
        return self.rfid_card_id

    def get_rfid_key_fob_type(self) -> str:
        return self.rfid_key_fob_id_type

    def get_rfid_card_type(self) -> str:
        return self.rfid_card_id_type

    def is_rfid_key_fob_scanned(self) -> bool:
        return self.rfid_key_fob_is_scanned

    def is_rfid_card_scanned(self) -> bool:
        return self.rfid_card_is_scanned


class TerminalTextColorsAndStyles:
    """A class that contains terminal text colors and styles."""
    # Cyan text with default background and bold
    fgCyan_bgDefault_bold: str = "\033[36;49;1m"
    # Red text with default background and bold
    fgRed_bgDefault_bold: str = "\033[31;49;1m"
    # White text with default background and bold
    fgWhite_bgDefault_bold: str = "\033[37;49;1m"
    # White text with green background and bold
    fgWhite_bgGreen_bold: str = "\033[37;42;1m"
    # White text with red background and bold
    fgWhite_bgRed_bold: str = "\033[37;41;1m"
    green: str = "\033[92m"  # Green text
    red: str = "\033[91m"  # Red text
    reset: str = "\033[0m"  # Reset text color and style
    yellow: str = "\033[93m"  # Yellow text
    bold: str = "\033[39;49;1m"  # Bold text


class App:
    """App class for the RFID reader application on the Raspberry Pi.
    """

    def __init__(self):
        GPIO.setwarnings(False)  # RuntimeWarning: channel already in use
        self.rfid = SimpleMFRC522()  # Initialize the RFID module
        self.firebase = Firebase()  # Initialize the Firebase module
        self.firebase.clear_all_data_from_database()
        self.text = TerminalTextColorsAndStyles()  # Text colors and styles
        self.rfid_tags = RfidTags()
        self._rfid_key_fob_timestamp: float = None
        self._rfid_card_timestamp: float = None
        self.time_difference: float = None

    def reset(self) -> None:
        """Reset the RFID reader application.
        """
        self.firebase.clear_all_data_from_database()
        self.rfid_tags.rfid_key_fob_is_scanned = False
        self.rfid_tags.rfid_card_is_scanned = False
        self._rfid_key_fob_timestamp = None
        self._rfid_card_timestamp = None
        self.time_difference = None

    def run(self) -> None:
        """There are two RFID tags in the game: the RFID key fob and the RFID card.
        First to scan the RFID key fob wins the game.
        The game logs both the RFID key fob and RFID card scans to Firebase.
        If a tag has been already scanned, it will not be scanned again.
        and calculates the time difference between the two scans.
        After two scans, ask the user if they want to play again.
        if yes, reset the game and start over.
        if no, exit the game.
        """
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        print(self.text.fgWhite_bgGreen_bold + "GO!" + self.text.reset)

        while True:
            try:
                id, rfid_text = self.rfid.read()  # Read the RFID tag
                print(f"ID: {id}")

                if id == self.rfid_tags.get_rfid_key_fob_id() and not self.rfid_tags.is_rfid_key_fob_scanned():
                    self.rfid_tags.rfid_key_fob_is_scanned = True
                    self._rfid_key_fob_timestamp = time.time()
                    print(self._rfid_key_fob_timestamp)
                    self.firebase.write(
                        id, self.rfid_tags.get_rfid_key_fob_type())
                    print(self.text.fgWhite_bgDefault_bold +
                          "RFID Key Fob scanned!" + self.text.reset)
                elif id == self.rfid_tags.get_rfid_card_id() and not self.rfid_tags.is_rfid_card_scanned():
                    self.rfid_tags.rfid_card_is_scanned = True
                    self._rfid_card_timestamp = time.time()
                    print(self._rfid_card_timestamp)
                    self.firebase.write(
                        id, self.rfid_tags.get_rfid_card_type())
                    print(self.text.fgWhite_bgDefault_bold +
                          "RFID Card scanned!" + self.text.reset)
                else:
                    print(self.text.yellow +
                          "RFID tag already scanned!" + self.text.reset)

                if self.rfid_tags.is_rfid_key_fob_scanned() and self.rfid_tags.is_rfid_card_scanned():
                    print(self.text.fgWhite_bgDefault_bold +
                          "Both RFID tags have been scanned!" + self.text.reset)
                    time_difference = math.fabs(
                        self._rfid_key_fob_timestamp - self._rfid_card_timestamp
                    )  # Calculate the time difference between the two scans

                    # print who got scanned first
                    if self._rfid_key_fob_timestamp < self._rfid_card_timestamp:
                        print(self.text.fgWhite_bgGreen_bold +
                              "RFID Key Fob was scanned first!" + self.text.reset)
                    else:
                        print(self.text.fgWhite_bgGreen_bold +
                              "RFID Card was scanned first!" + self.text.reset)

                    print(self.text.fgWhite_bgDefault_bold +
                          f"Time difference: {time_difference:.2f} seconds" +
                          self.text.reset)
                    break

            except KeyboardInterrupt:
                GPIO.cleanup()
                break


if __name__ == "__main__":  # Run the app if the script is executed
    app = App()
    app.run()
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            app.reset()
            app.run()
        elif play_again.lower() == 'n':
            print(TerminalTextColorsAndStyles().green + "Thanks for playing" +
                  TerminalTextColorsAndStyles().reset)
            app.reset()
            sys.exit()
        else:
            print(
                "Invalid input" + ". " + "Please enter " +
                TerminalTextColorsAndStyles().green + "Yes "
                + TerminalTextColorsAndStyles().reset +
                "(y)" + " or " + TerminalTextColorsAndStyles().red + "No " +
                TerminalTextColorsAndStyles().reset + "(n): "
            )
