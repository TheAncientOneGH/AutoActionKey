# [ About ]
#
# AutoActionKey v1.0
#
# for games that use annoying input methods that
# require you to single click every spec of dust
# on a planet in order to play. For example:
# cleaning up trash in Farmer's Dynasty 2. The
# devs really want my carpal tunnel syndrome to
# kick in at full effect..
#
# want to give people carpal tunnel syndrome.
#
# Embedded Python should work just fine for allowing
# this script to run isolated by itself.
#
# By default this is setup to spam E when you hold E
# down making cleaning up properties ingame so much
# better and less stress on your hands (and mouse).
#
# [ Installation ]
#
# Extract somewhere (ex: C:\AutoActionKey) then simply
# double click AutoActionKey.cmd file to run it. Press
# ctrl+shift+x to stop the script.
#
############# [ BEGIN CONFIG OPTIONS ] #############
#
# Whatever key you're listening for
# to use ctrl, shift, or alt, just add it to the
# key example: 'ctrl+e'
#
# This should be a different key than the game1
# action key. If set the same as the ACTION_KEY
# the script does some weird stuff and does not
# trigger properly. (This will be the key you
# press and hold for auto functionality)
#
# Default: f
#
MY_KEY = 'f'

# Key to press when MY_KEY is pressed
# Should be set to the real ingame action
# key
#
# Default: e
#
ACTION_KEY = 'e'

# Enable Key. Choose a key or key combo to
# enable/disable this while ingame.
# Enclose specials like ctrl, shift in
# angle brackets <> ex. <shift>
#
# Default: ctrl+q
#
E_KEY = '<ctrl>+q'

# Used to terminate/exit this script
# Enclose specials like ctrl, shift in
# angle brackets <> ex. <shift>
#
# Default: <ctrl>+<shift>+x
#
KILL_KEY = '<ctrl>+<shift>+x'

# Tweak as needed as it will heavily depend
# on each individual machine. This is the delay
# between KeyPress and KeyRelease that the script
# uses to emulate the action repeat. This will effect
# how quick each consecutive keypress occurs.
# 0.02 Slower - 0.002 Faster
#
# Default: 0.002
#
KEY_DELAY = 0.002

############## [ END CONFIG OPTIONS ] ##############
#
import os
import time
import keyboard as kb
from rich import print
from pynput import keyboard
from pynput.keyboard import Controller, GlobalHotKeys

controller = Controller()
listener = None
VER = "1.0"
SCR_E = True

def get_status():
    status = "[bold bright_red]Disabled[/bold bright_red]"
    if (SCR_E):
        status = "[bold bright_green]Enabled[/bold bright_green]"
    return status

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"[bold bright_yellow]AutoActionKey v{VER}[/bold bright_yellow]")
    print(" ")
    print("Script: " + get_status())
    print(f"Hold [bold bright_blue]{MY_KEY}[/bold bright_blue] to auto-repeat [bold yellow]{ACTION_KEY}[/bold yellow]")
    print(f"Press [bold bright_cyan]{E_KEY.replace('<','').replace('>','')}[/bold bright_cyan] to toggle script [bold bright_green]On[/bold bright_green]/[bold bright_red]Off[/bold bright_red]")
    print(f"Press [bold bright_red]{KILL_KEY.replace('<','').replace('>','')}[/bold bright_red] to exit\n")

def toggle_script():
    global SCR_E
    SCR_E = not SCR_E
    logo()

def kill_script():
    print("[bold red]Killing Script... Later![/bold red]")
    if listener is not None:
        listener.stop()
    os._exit(0)

def handle_auto_repeat(key):
    if not SCR_E:
        return
    _temp = kb.is_pressed(MY_KEY)
    while (_temp):
        controller.press(ACTION_KEY)
        time.sleep(KEY_DELAY)
        controller.release(ACTION_KEY)
        _temp = kb.is_pressed(MY_KEY)

def on_press(key):
    try:
        if SCR_E and kb.is_pressed(MY_KEY):
            handle_auto_repeat(key)
        else:
            pass
    except:
        pass

hotkeys = GlobalHotKeys({
    E_KEY: toggle_script,
    KILL_KEY: kill_script
})

with keyboard.Listener(on_press=on_press) as lis:
    logo()
    print("[bold green]Listener Started: Script Ready[/bold green]")
    listener = lis
    hotkeys.start()
    lis.join()
