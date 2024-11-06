# Native Python Libraries.

# Third Party Libraries.

# Self Built Libraries.
from Functions.OSFunctions import askPath


class main:
    # Main class procedure of the application in order to run the periodic backups.

    def __init__(self) -> None:
        """
        Procedure starts the main app work flow.
            Args: None
            Returns: None
            Raises: None
        """
        # 1.- We require the path we will generate the backups (input).
        # 2.- We require the saving directory (output).
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
        print("_____________________________________________________________")
        print("| WELCOME TO THE AUTO BACK UP BUILDER (VER 1.0.0)           |")
        print("_____________________________________________________________")
        pass

    pass


if __name__ == "__main__":
    main()
    input("Press Enter to end program...")
    pass
