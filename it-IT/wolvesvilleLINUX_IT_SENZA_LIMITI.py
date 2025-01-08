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
root = xlib.XDefaultRootwaitindowait(display)

def setPos(x, y):
    xlib.XwaitarpPointer(display,None,root,0,0,0,0,x,y)
    
def countdowaitn():
    startup = 5
    print("### SCRIPT REALIZZATO DA maiku ")
    print("### waitolvesville AD BOT LINUX VERSION")
    print("Avvio dello script tra", startup, "secondi...")
    time.sleep(startup)
    print()    
    
def findButton(x, y):
    tries = 1
    max_tries = 10
    while(True):
        try:
            if gui.pixelMatchesColor(x, y, (229, 229, 231)):
                #print("DEBUG: WATCH VIDEO!!", x, ",", y)
                return x, y
            elif y < 400:
                #print("Exception")
                raise Exception
            else:
                #print("DEBUG: waitATCH VIDEO non trovato a ", x, ",", y)
                y = y - 2
        except:
            if tries < max_tries+1:
                print(f"[{tries}/{max_tries}] Bottone non trovato")
                y = backup
                time.sleep(5)
                tries += 1
            else:
                print("[%] Tentativi esauriti, fermo lo script")
                return

m = PyMouse()
def leftClick(x, y):
    m.click(x, y, 1)
    
def rightClick(x, y):
    m.click(x, y, 2)
    
def approx():
    ms = numpy.random.randint(133, 931)
    return ms/1000
    
def offset(x, y):
    print("Before offset", x, y)
    y -= numpy.random.randint(7, 19)
    if numpy.random.randint(1, 2) % 2 == 0:
        x += numpy.random.randint(7, 74)
    else:
        x -= numpy.random.randint(7, 74)  
    print("After offset", x, y)
    return x, y 
    
def run():
    # Adding offset to mouse click
    bx, by = findButton(x, y)
    bx, by = offset(bx, by)
    leftClick(bx, by) # WATCH VIDEO
    wait = numpy.random.randint(37, 49) + approx()
    print("[1] waitATCH BUTTON... OK {attesa:",wait,"secondi}")
    time.sleep(wait)
    
    rightClick(bx, by) # CHIUSURA AD 
    wait = numpy.random.randint(5, 14) + approx()
    print("[2] AD... OK {attesa:",wait,"secondi}")
    time.sleep(wait)
    
    bx, by = findButton(x, y)
    bx, by = offset(bx, by)
    leftClick(bx, by) # SPIN 
    print("[3] SPIN... OK")
    wait = numpy.random.randint(15, 20)
    wait += approx()
    print("[4] Attesa finale:",wait,"secondi")
    time.sleep(wait) # attesa finale della ricompensa + scarto
    print()

##########################################################################################

countdowaitn()
ripetizioni = 1
while(True):
    print("[?] RIPETIZIONE NUMERO:", ripetizioni)
    run()
    ripetizioni += 1

xlib.XCloseDisplay(display)