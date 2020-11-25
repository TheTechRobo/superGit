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
from pyGit import *
# DEFINE FUNCTIONS FOR LATER USE

# CREATE WIDGETS
Label(main, text="Nothing to see here...").pack()
# CREATE WIDGETS

# START MAINLOOP
main.mainloop()
# START MAINLOOP

# TO UNDERSTAND RECURSION, SEE THE TOP OF THIS FILE
