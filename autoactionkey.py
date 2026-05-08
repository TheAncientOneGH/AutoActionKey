# [ About ]
#
# AutoActionKey v1.3
#
# for games that use annoying input methods that
# require you to single click every spec of dust
# on a planet in order to play. For example:
# cleaning up trash in Farmer's Dynasty 2. The
# devs really want my carpal tunnel syndrome to
# kick in at full effect..
#
# Embedded Python should work just fine for allowing
# this script to run isolated by itself.
#
# By default this is setup to spam E when you hold E
# down making cleaning up properties ingame so much
# better and less stress on your hands (and keyboard).
#
# [ Installation ]
#
# Extract somewhere (ex: C:\AutoActionKey) then simply
# double click AutoActionKey.cmd file to run it. Press
# ctrl+shift+x to stop the script.
#
############# [ BEGIN CONFIG OPTIONS ] #############
#
# Whatever key you're listening for to use ctrl, shift,
# or alt, just add it to the key example: 'ctrl+e'
# Enclose specials like ctrl, shift in angle brackets
# <> ex. <shift>
#
# This should be a different key than the game action
# key. If set the same as the ACTION_KEY the script
# does some weird stuff and does not trigger properly.
# (This key you press and hold for auto functionality)
#
# Default: f
#
MY_KEY = 'f'

# Key to press when MY_KEY is pressed Should be set to
# the real ingame action key
#
# Default: e
#
ACTION_KEY = 'e'

# Enable Key. Choose a key or key combo to enable/disable
# this while ingame. Enclose specials like ctrl, shift in
# angle brackets <> ex. <shift>
#
# Default: ctrl+q
#
E_KEY = '<ctrl>+q'

# Used to terminate/exit this script. Enclose specials like
# ctrl, shift in angle brackets <> ex. <shift>
#
# Default: <ctrl>+<shift>+x
#
KILL_KEY = '<ctrl>+<shift>+x'

# Used to display some useless stats, because why not?
#
# Default: i
#
STAT_KEY = 'i'

# Tweak as needed as it will heavily depend on each
# individual machine. This is the delay between
# KeyPress and KeyRelease that the script uses to
# emulate the action repeat. This will effect how
# quick each consecutive keypress occurs.
# 0.02 Slower - 0.002 Faster
#
# Default: 0.06
#
KEY_DELAY = 0.006

############## [ END CONFIG OPTIONS ] ##############
#
import os
import sys
import subprocess

def imPackage(package, version):
    try:
        import package
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package + "==" + version, '--no-warn-script-location'])
    return

imPackage('keyboard', '0.13.5')
imPackage('rich', '15.0.0')
import time
import random
import keyboard as kb
from rich import print
imPackage('pynput', '1.8.1')
from pynput import keyboard
from pynput.keyboard import Controller, GlobalHotKeys

controller = Controller()
listener = None
VER = "1.2"
SCR_E = True
MY_KEY_TOTAL = 0
ACTION_KEY_TOTAL = 0
thefunlist = [
    'And Fanny\'s your aunt',
    'Job\'s a good\'un',
    'Bish bash bosh',
    'Easy peasy',
    'Hey presto',
    'Et voilà',
    'There you go',
    'Simple as that',
    'Job done',
    'And that’s that',
    'Sorted',
    'Done and dusted',
    'In the bag',
    'Happy days',
    'Bob\'s your uncle and Fanny\'s your aunt',
    'Dirty Deeds Done Dirt Cheap',
    'Stick a fork in it, it\'s done'
]

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
    print(f"Press [bold bright_yellow]{STAT_KEY}[/bold bright_yellow] for Useless Stats")
    print(f"Press [bold bright_red]{KILL_KEY.replace('<','').replace('>','')}[/bold bright_red] to exit\n")

def stats():
    logo()
    if (MY_KEY_TOTAL < 1):
        justforlaughs = random.choice(['What miracle were you expecting?', 'alakaz ... *pow*, err, nope...\n\nI really tried, but, even I cannot pull stats from my arse...', 'Congrats! Your stats are [bold cyan]0[/bold cyan]! You ARE the laziest AUTO key user ever..'])
        print(f'[bold bright_yellow]{justforlaughs}[/bold bright_yellow]\n\n[bold bright_red]Might need to use the script to aquire stats...[/bold bright_red]')
    else:
        randFun = random.choice(thefunlist)
        print("[bold bright_cyan]- [bold bright_yellow]Useless Stats[/bold bright_yellow] -[/bold bright_cyan]")
        print(" ")
        if (MY_KEY_TOTAL > 1):
            _x = "s."
        else:
            _x = "."
        print(f"You pressed [bold bright_blue]{MY_KEY}[/bold bright_blue] [bold yellow]{MY_KEY_TOTAL}[/bold yellow] time{_x}")
        print(f"AutoActionKey saved your hands and keyboard by running [bold bright_red]{ACTION_KEY}[/bold bright_red] [bold yellow]{ACTION_KEY_TOTAL - MY_KEY_TOTAL}[/bold yellow] times")
        print(" ")
        print(randFun)

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
    global MY_KEY_TOTAL, ACTION_KEY_TOTAL
    if not SCR_E:
        return
    MY_KEY_TOTAL += 1;
    _temp = kb.is_pressed(MY_KEY)
    while (_temp):
        ACTION_KEY_TOTAL += 1
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
    KILL_KEY: kill_script,
    STAT_KEY: stats
})

with keyboard.Listener(on_press=on_press) as lis:
    logo()
    print("[bold green]Listener Started: Script Ready[/bold green]")
    listener = lis
    hotkeys.start()
    lis.join()
