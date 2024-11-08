# Native Python Libraries.
from threading import Thread, Event
import time
import os
import zipfile

# Third Party Libraries.
from tqdm import tqdm

# Self Built Libraries.
from Functions.OSFunctions import askPath, askNumber, askYesNo, makeBackup
from Functions.TimeFunctions import timeStamp


class main:
    # Main class procedure of the application in order to run the periodic backups.

    def __init__(self) -> None:
        """
        Procedure starts the main app work flow.
            Args: None
            Returns: None
            Raises: None
        """

        self.eventThread = Event()

        # We start the application and print our app header.
        self.header()
        self.instructions()

        # We initiate the settings loop.
        self.initialProcedure()

        # We run the backup loop.
        self.activityLoop()

        pass

    @staticmethod
    def header() -> None:
        """Method prints the header"""
        print()
        print("_____________________________________________________________")
        print("| WELCOME TO THE AUTO BACK UP BUILDER (VER 1.0.0)           |")
        print("_____________________________________________________________")
        print()
        pass

    @staticmethod
    def instructions() -> None:
        """Method prints user instructions."""
        print(
            "\nWelcome to the automatic backup generator. Program is designed as follows:\n1.- It will ask you the file path ypu want to automatically backup.\n2.- It will ask for the destination where you desire to store the backup.\n3.- It will ask on what frequency do you want to make a backup file.\n4.- It will ask if you want to over write each backup or stack each backup.\nAl last if you desire to terminate the program at any moment just press Escape key [Esc].\n"
        )
        input("Press Enter to continue ...")
        pass

    def daemonEscapeFunction(self):
        input("Press Enter key to end backup.")
        self.eventThread.set()
        pass

    def backupOrigin(self) -> None:
        """
        Method asks for the path file where to copy its content and build a backup point.
        Args: None
        Returns: None
        Raises: None
        """
        print("Please select the folder to backup automatically:")
        self.pathToBackup = askPath(title="Select Folder Path To Back Up")
        pass

    def backupDestination(self) -> None:
        """
        Method asks for the path file where to store the back up.
        Args: None
        Returns: None
        Raises: None
        """
        print("Please select the folder where to store the backup:")
        self.outputPath = askPath(title="Select Path Where To Save The Backup")
        pass

    def askFrequency(self) -> None:
        """
        Method asks for a frequency and delay time for the system backup procedure.
        Args: None
        Returns: None
        Raises: None
        """
        while True:

            print("Please enter the backup frequency in hours (h)")
            self.frequency = (
                askNumber()
            )  # We convert hours into minutes and into seconds.
            print("Please enter the initial delay in hours (h)\nIf None please type 0")
            self.delay = (
                askNumber()
            )  # 60*60* We convert hours into minutes and into seconds.

            if self.frequency != None and self.delay != None:
                break
        pass

    def askOverwriteBackup(self) -> None:
        """
        Method asks if user wants to over write the stored files or wants to store a time line backup.
        Args:None
        Returns: None
        Raises: None
        """

        print(
            "Would you like to over write the backup files or build a time line backup (mind backup file size)"
        )
        self.overwrite = askYesNo()
        pass

    def initialProcedure(self) -> None:
        """
        Method describes the procedure to set the preference settings for the users desired backup.
        Args: None
        Returns: None
        Raises: None
        """
        # 1.- We require the path we will generate the backups (input).
        self.backupOrigin()

        # 2.- We require the saving directory (output).
        self.backupDestination()

        # 3.- We require the frequency we will be building the backup.
        # 4.- We ask for a delay if needed on for the backups.
        self.askFrequency()

        # 5.- We ask the user if he desires to overwrite the backup files.
        self.askOverwriteBackup()

        # 6.-We confirm all settings are properly enabled.
        self.askConfirmation()
        pass

    def askConfirmation(self) -> None:
        """
        Method asks user for confirmation if configuration is correct, otherwise asks to setup configuration as required.
        Args: None
        Returns: None
        Raises: None
        """

        print("Are the following settings correct?")
        print(f"> Frequency {self.frequency} h")
        print(f"> Delay {self.delay} h")
        print(f"> Back up origin path: {self.backupOrigin}")
        print(f"> Back up destination path: {self.backupDestination}")
        print(f"> Overwrite backups: {self.overwrite}")

        if not askYesNo():
            self.initialProcedure()

        pass

    def makeBackup(self) -> bool:
        """
        Function recibes a origin directory path and a destination where to store the backup files. Then it makes a copy of given files and compress them into a smaller size (deleting the non temporal compressed files).
        This function will overwrite the back up files otherwise it's told False.
        Args:
            > origin (str): origin file path to make a backup.
            > destination (str): destination the backup will be stored.
            > overwriting (str): True so it overwrites the previous back up. False to not overwrite the last backup and and a time stamp in the created backup.
        Returns:
            > True if backup was successful, False otherwise.
        Raises: None
        """
        # Repeat thread until escape sequence is made.
        while not self.eventThread.is_set():

            # We get the number of files we are about to copy.
            if not os.path.isdir(self.backupOrigin):
                raise f"Error backup origin is not a valid path: {self.backupOrigin}"
            if not os.path.isdir(self.backupDestination):
                raise f"Error backup destination is not a valid path: {self.backupDestination}"

            # We estimate the total amount of files we are going to backup.
            fileList = [
                f
                for f in os.listdir(self.backupOrigin)
                if os.path.isfile(os.path.join(self.backupOrigin, f))
            ]
            fileCount = len(fileList)
            if fileCount == 0:
                print(f"No files in origin path to make a backup: {self.backupOrigin}")
                return False

            if not self.overwrite:
                backupFileName = f"backup {timeStamp()}.zip"
            else:
                backupFileName = "backup.zip"

            backupFilePath = os.path.join(self.backupDestination, backupFileName)

            with zipfile.ZipFile(backupFilePath, "w") as backupZip:
                # We initiate the progress bar with the number of files to copy.
                for file in tqdm(
                    fileList,
                    desc="Backup Progress",
                    unit="file",
                    colour="green",
                ):
                    filePath = os.path.join(self.backupOrigin, file)
                    backupZip.write(filePath, arcname=file)

            print("backup successful.")

            # We wait until the frequency is fulfilled.
            time.sleep(self.frequency)

    def activityLoop(self) -> None:
        """
        Method establishes the threading logic so one process ocurres while the second one is listening to the user command to stop the program.
        Args: None
        Returns: None
        Raises: None
        """

        backupThread = Thread(target=self.makeBackup, daemon=False)
        terminateThread = Thread(target=self.daemonEscapeFunction, daemon=False)

        time.sleep(self.delay)
        backupThread.start()
        terminateThread.start()

        terminateThread.join()
        backupThread.join()

        pass

    pass


if __name__ == "__main__":
    main()
    input("Press Enter to end program...")
    pass
