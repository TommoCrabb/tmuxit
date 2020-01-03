#!/usr/bin/env python3
'''
This script takes a command as input and runs it in a tmux window.
It is mostly aimed at making it easier to launch graphical apps
from the command line, without having them take over the terminal.
'''
from subprocess import run
from sys import argv
from shutil import which

def fatal(msg):
    '''Print an error message and exit'''
    print("FATAL ERROR:", msg, "EXITING", sep="\n")

def tmux_init(go=0,sesh="run"):
    '''Start a tmux session named "sesh" if it doesn't already
    exist. Exit if the session fails to start.'''
    x = run(["tmux", "has-session", "-t", sesh])
    if x.returncode == 1:
        if go == 1:
            fatal("Failed to start tmux session.")
        run(["tmux", "new-session", "-d", "-s", sesh])
        tmux_init(go=1)

sesh = "run"

# Exit if can't find tmux
if which("tmux") == None:
    fatal("Unable to find tmux on your system.")

tmux_init(sesh) # Start tmux session

# Run command in new tmux window.
c = ["tmux","new-window","-t",sesh,]
c.extend(argv[1:])
run(c)
