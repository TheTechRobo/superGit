# TO UNDERSTAND RECURSION, SEE THE BOTTOM OF THIS FILE
"""
SUPERGIT
A simple, Tkinter-based Git client
Copyright (c) 2020 Ittussarom Retals Mail Ynohtna, licensed under the DBAD license.
Thanks for using!
"""

print("Launching supergit...")
# IMPORT MODULES
from tkinter import *
from tkinter import messagebox
from subprocess import Popen as run
from subprocess import PIPE as p
# IMPORT MODULES

# SET UP WINDOW
main = Tk()
main.title("superGit")
# SET UP WINDOW

# DEFINE FUNCTIONS FOR LATER USE
# GIT PULL
def pull(branch, origin):
    gitpull = run(["git", "pull", origin, branch], shell=False, stdout=p, stderr=p)
    gitPullOutput = gitpull.communicate()
    if gitPullOutput == "<enter thingy here>":
        pass
    else:
        pass
# GIT ADD
def add(file):
    gitadd = run(["git", "add", file], shell=False, stdout=p, stderr=p)
    gitaddData = gitadd.communicate()
    if gitaddData == "<insert>":
        pass
    else:
        pass
# MORE TO COME LATER!
# DEFINE FUNCTIONS FOR LATER USE

# CREATE WIDGETS
Label(main, text="underDevelopment").pack()
# CREATE WIDGETS

# TO UNDERSTAND RECURSION, SEE THE TOP OF THIS FILE