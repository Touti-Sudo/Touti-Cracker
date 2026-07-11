import os
import platform
import subprocess


def is_av_active():
    systemtype = platform.system()

    if systemtype == "Windows":
        try:
            return os.system('sc query WinDefend | find "RUNNING"') == 0
        except Exception:
            return False

    elif systemtype == "Linux":
        try:
            for service in ("clamav-daemon", "clamav-freshclam"):
                result = subprocess.run(
                    ["systemctl", "is-active", "--quiet", service]
                )
                if result.returncode == 0:
                    return True
            return False
        except Exception:
            return False

    elif systemtype == "Darwin":
        try:
            result = subprocess.run(
                ["pgrep", "-x", "XProtectService"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return result.returncode == 0
        except Exception:
            return False

    return False
