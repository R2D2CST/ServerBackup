# Native Python Libraries.

# Third Party Libraries.

# Self Built Libraries.
from Functions.OSFunctions import askPath, askNumber
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
        # We start the application and print our app header.
        self.header()
        self.instructions()

        # 1.- We require the path we will generate the backups (input).
        self.backupOrigin()

        # 2.- We require the saving directory (output).
        self.backupDestination()

        # 3.- We require the frequency we will be building the backup.
        # 4.- We ask for a delay if needed on for the backups.
        # 5.- We start the main loop until the user cancels the backup self building.
        # a.- We copy the file path contents.
        # b.- We paste the file contents into the destination selected by the user.
        # c.- We compress the recently created backup file into a smaller size file.
        # d.- We delete the temporal uncompressed file path.
        # e.- We end the loop if user press escape key.

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

    def calculateFrequency(self) -> None:
        """
        Method asks for a frequency and delay time for the system backup procedure.
        Args: None
        Returns: None
        Raises: None
        """
        while True:

            print("Please enter the backup frequency in hours (h)")
            self.frequency = askNumber()
            print("Please enter the initial delay in hours (h)\nIf None please type 0")
            self.delay = askNumber()

            if self.frequency != None and self.delay != None:
                break
        pass

    def askConfirmation(self) -> None:
        """
        Method asks user for confirmation if configuration is correct, otherwise asks to setup configuration as required.
        Args: None
        Returns: None
        Raises: None
        """

        pass

    pass


if __name__ == "__main__":
    main()
    input("Press Enter to end program...")
    pass
