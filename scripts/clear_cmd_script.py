import subprocess


def clearsystem(OS):
    if OS == "Windows":
        clear = subprocess.run("cls", text=True, shell=True)
        if clear.returncode != 0:
            subprocess.run("clear", shell=True, text=True)
    else:
        clear = subprocess.run("clear", text=True, shell=True)
        if clear.returncode != 0:
            subprocess.run("cls", shell=True, text=True)
