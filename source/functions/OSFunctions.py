# Native Python Libraries.
from tkinter import filedialog

# Third Party Libraries.

# Self Built Libraries.


def askPath(title) -> str:
    """
    Procedure returns the file path location chosen bye the user in the GUI.
    Args:
        > title (str): title for the asking window for an existing file.
    Returns:
        > file path (str): chosen file path, if user cancels operation returns False.
    Raises: None
    """
    varPath: str = filedialog.askdirectory(mustexist=True, title=title)
    if varPath:
        return varPath
    else:
        return False


def askNumber() -> int:
    """
    Procedure ask the user for a round number to estimate the frequency of the backup and delay.
    Args: None
    Returns:
        > number (int): integer number.
    Raises: None
    """
    while True:
        number: str = input("Please enter a round number: ")
        try:
            number: int = int(number)
            return number
        except TypeError:
            print("Must be a round number (1, 2, 3 ...)")
            continue
    return number


def askYesNo() -> bool:
    """
    Procedure asks for a Yes or No question if answered yes returns True otherwise returns False.
    Args: None
    Returns: Yes (True) or No (False)
    Raises: None
    """
    while True:
        question: str = input("Please type (Y) for Yes or type (N) for No: ")
        if question.lower() == "y":
            return True
        elif question.lower() == "n":
            return False
        else:
            continue
    pass
