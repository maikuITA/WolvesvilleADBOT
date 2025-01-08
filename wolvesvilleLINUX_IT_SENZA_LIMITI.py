# Fork of the bot made by RedScorpion
# VERSIONE ITALIANA

from ctypes import *
from pymouse import PyMouse
import pyautogui as gui
import numpy
import time

xlib = cdll.LoadLibrary('libX11.so.6')

# Display size (width, height)
xmax = 1366
ymax = 768

# CHANGEME
x = 1039
y = 756

# y BACKUP used to restore y to a normal value
backup = y

# Tempo fisso da aspettare tra uno spostamento ed un altro
sleep = 0.05

# Displays
display = xlib.XOpenDisplay(None)
root = xlib.XDefaultRootWindow(display)

def setPos(x, y):
    xlib.XWarpPointer(display,None,root,0,0,0,0,x,y)
    
def countdown():
    startup = 5
    print("### SCRIPT REALIZZATO DA maiku ")
    print("### Wolvesville AD BOT LINUX VERSION")
    print("Avvio dello script tra", startup, "secondi...")
    time.sleep(startup)
    print()    
    
def findButton(x, y):
    while(True):
        try:
            if gui.pixelMatchesColor(x, y, (229, 229, 231)):
                #print("DEBUG: WATCH VIDEO!!", x, ",", y)
                return x, y
            elif y < 400:
                raise Exception
            else:
                #print("DEBUG: WATCH VIDEO non trovato a ", x, ",", y)
                y = y - 2
        except:
            print("[!] Non ho trovato il bottone, aspetto 10 secondi e riprovo...")
            y = backup
            time.sleep(10)

m = PyMouse()
def leftClick(x, y):
    m.click(x, y, 1)
    
def rightClick(x, y):
    m.click(x, y, 2)
    
def approx():
    ms = numpy.random.randint(133, 931)
    return ms/1000
    
def run():
    bx, by = findButton(x, y)
    leftClick(bx, by) # WATCH VIDEO
    w = numpy.random.randint(37, 49)
    w += approx()
    print("[1] WATCH BUTTON... OK {attesa:",w,"secondi}")
    time.sleep(w)
    
    rightClick(bx, by) # CHIUSURA AD 
    w = numpy.random.randint(5, 14)
    w += approx()
    print("[2] AD... OK {attesa:",w,"secondi}")
    time.sleep(w)
    
    bx, by = findButton(x, y)
    leftClick(bx, by) # SPIN 
    print("[3] SPIN... OK")
    w = numpy.random.randint(15, 20)
    w += approx()
    print("[4] Attesa finale:",w,"secondi")
    time.sleep(w) # attesa finale della ricompensa + scarto
    print()

##########################################################################################

countdown()
ripetizioni = 1
while(True):
    print("[?] RIPETIZIONE NUMERO:", ripetizioni)
    run()
    ripetizioni += 1

xlib.XCloseDisplay(display)