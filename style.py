""" Contains Styling Classes using Colorama import """

from colorama import Fore, Back, Style


class Sty:
    """
    Colorama commands are used to create style (Sty) classes that
    can be applied to the terminal text in a short hand format to
    reduce line sizes.
    """
    clr = Style.RESET_ALL  # Clear - Clears previously added Styling
    pos = Fore.GREEN  # Positive - Bright Green Text
    neg = Fore.RED  # Negative - Red Text
    neu = Fore.YELLOW  # Neutral = Yellow Text
    log = Fore.MAGENTA + Back.CYAN  # Logo - Magenta Text, Cyan BG
    hdr = Fore.MAGENTA  # Header - Magenta Text
    que = Fore.CYAN  # Question - Cyan Text
    cus = Fore.MAGENTA  # Custom - Magenta Text
    inv = Fore.BLACK + Back.WHITE  # Inverted - Black Text, White BG
