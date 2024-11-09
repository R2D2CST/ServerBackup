# Native Python Libraries.
from datetime import datetime

# Third Party Libraries.

# Self Built Libraries.


def timeStamp() -> str:
    """
    Procedure returns the actual date in year-month-day hour:minute:second format.
    Args: None
    Returns:
        > timeStamp (str): actual date time with hours and minutes.
    Raises: None
    """
    return datetime.now().strftime(format="%Y-%m-%d_%H-%M")
