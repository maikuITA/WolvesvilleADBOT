# Fork of the bot made by RedScorpion
# ENGLISH VERSION

# scrcpy is recommended (Bluestacks is a valid alternative)

import pyautogui as gui
import win32api as win
import win32con
import numpy
import time

# Function that clicks on "WATCH VIDEO"
def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
# Function to click the back button (RIGHT CLICK in scrcpy)
def back(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.01)
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

# Function that finds "WATCH VIDEO" or "SPIN" button
def find_button():
    x = CHANGEME
    y = CHANGEME
    while(True):
        win.SetCursorPos((x, y))
        # (229, 229, 231) is the RGB code of the WATCH VIDEO and SPIN buttons
        if gui.pixelMatchesColor(x, y, (229, 229, 231)):
            #print("DEBUG: WATCH VIDEO!!", x, ",", y)
            click(x, y)
            break
        else:
            #print("DEBUG: WATCH VIDEO not found on ", x, ",", y)
            y = y - 1

def run():
    find_button() # WATCH VIDEO
    
    w = numpy.random.randint(37, 49)
    print("[1] WATCH VIDEO -> OK {wait:",w,"seconds}")
    time.sleep(w)
    
    back(1437, 1006) # BACK
    w = numpy.random.randint(5, 14)
    print("[2] AD -> OK {wait:",w,"seconds}")
    time.sleep(w)
    
    find_button() # SPIN
    print("[3] SPIN -> OK")
    w = numpy.random.randint(15, 20)
    print("[4] Final wait:",w,"seconds")
    time.sleep(w) # FINAL WAIT
    print()

def countdown():
    startup = 5
    print("### SCRIPT MADE BY maiku ")
    print("### Wolvesville AD BOT 1.4")
    print("Script will start in", startup, "seconds...")
    time.sleep(startup)
    print()

##############################################################################

reps = 1
countdown()
    
limit = 30 # CUSTOMIZABLE

print("Limited mode")
print("limit:", limit)
print()    

while reps < limit+1:
    print("[?] REP number:", reps)
    run()
    reps += 1