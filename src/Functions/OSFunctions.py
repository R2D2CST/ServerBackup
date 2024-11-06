# Native Python Libraries.
from tkinter import filedialog

# Third Party Libraries.

# Self Built Libraries.


def askPath(title) -> str:
    """
    Procedure returns the file path location chosen bye the user in the GUI.
        Args:
            title (str): title for the asking window for an existing file.
        Returns:
            file path (str): chosen file path.
        Raises: None
    """
    return filedialog.askdirectory(mustexist=True, title=title)
