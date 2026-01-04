import os


def is_av_active():
    try:

        return os.system('sc query WinDefend | find "RUNNING"') == 0
    except:
        return False
