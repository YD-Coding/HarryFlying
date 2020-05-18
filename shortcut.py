import sys
import os, winshell
from win32com.client import Dispatch


def createShortcut(path, target='', wDir='', icon=''):     
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    if icon == '':
        pass
    else:
        shortcut.IconLocation = icon
    shortcut.save()
desktop = winshell.desktop()
# path = os.path.join(desktop, "delete.lnk")
# target = r"C:\Users\yarin\output\delete.exe"
# wDir = r"C:\Users\yarin\output"
full_path = sys.argv[0]
path_basename = os.path.basename(full_path)
new_path = list(full_path.split("/"))
filename = new_path[len(new_path) - 1]
new_path.pop(len(new_path) - 1)
wDir = '/'.join(new_path)
f = filename.split(".")[0]

def shortcut_exists(f):
    if os.path.isfile(r"C:\Users\yarin\Desktop\{}".format(f + ".lnk")):
        return True
    return False


def check_if_exists(f):
    if not shortcut_exists(f):
        createShortcut(os.path.join(desktop, f + ".lnk"), full_path, wDir, icon='')
        print("shortcut created")
    else:
        print("shortcut already exsits")
    