import re
from subprocess import run, PIPE
def resolution():
    output = run(['xrandr'], stdout=PIPE).stdout.decode()
    result = re.search(r'current (\d+) x (\d+)', output)
    width, height = map(int, result.groups()) if result else (800, 600)
    return width,height