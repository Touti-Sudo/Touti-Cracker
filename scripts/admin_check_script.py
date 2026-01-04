import ctypes
import os


def is_admin(OS):
    if OS == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    elif OS == "Linux":
        return os.geteuid() == 0
    elif OS == "Darwin":
        try:
            return os.getuid() == 0
        except:
            return False
