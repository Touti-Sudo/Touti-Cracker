import sys
import time
import pyfiglet
from colorama import Fore, Style


def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

