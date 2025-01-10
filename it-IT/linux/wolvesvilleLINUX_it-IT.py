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
    
def countdown():
    startup = 5
    print("[@@@] SCRIPT REALIZZATO DA maiku ")
    print("[@@@] Wolvesville AD BOT LINUX versione 1.6.2")
    print("[@@@] Avvio dello script tra", startup, "secondi...")
    time.sleep(startup)
    print()    
    
# Funzione che trova i bottoni WATCH VIDEO e SPIN 
def findButton(x, y):
    tries = 1
    max_tries = 5
    while(True):
        try:
            if gui.pixelMatchesColor(x, y, (229, 229, 231)):
                return x, y
            elif y < backup/2:
                raise Exception
            else:
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

# Click sinistro e destro del mouse

m = PyMouse()
def leftClick(x, y):
    m.click(x, y, 1)
    
def rightClick(x, y):
    m.click(x, y, 2)
    
# Aggiungo dei ms casuali ai tempi di attesa
def approx():
    ms = numpy.random.randint(133, 931)
    return ms/1000
    
def offset(x, y):
    # Offset della y
    y -= numpy.random.randint(3, 8)
    
    # Offset della x
    if numpy.random.randint(1, 11) % 2 == 0: # Scelgo a caso se andare a destra o a sinistra
        x += numpy.random.randint(5, 20)
    else:
        x -= numpy.random.randint(5, 20)  

    return x, y 
    
def run():
    # WATCH VIDEO
    bx, by = findButton(x, y)
    bx, by = offset(bx, by)
    leftClick(bx, by)
    wait = numpy.random.randint(35, 40) + approx()
    print("[1/3] WATCH BUTTON... OK")
    print(f"[===] Attesa: {wait} secondi")
    time.sleep(wait)
    
    # CHIUSURA AD 
    rightClick(bx, by) 
    wait = numpy.random.randint(5, 8) + approx()
    print("[2/3] AD BUTTON... OK")
    print(f"[===] Attesa: {wait} secondi")
    time.sleep(wait)
    
    # SPIN
    bx, by = findButton(x, y)
    bx, by = offset(bx, by)
    leftClick(bx, by)  
    print(f"[{3}/{3}] SPIN... OK")
    
    # ATTESA FINALE
    wait = numpy.random.randint(13, 18) + approx()
    print(f"[===] Attesa finale: {wait} secondi")
    time.sleep(wait) 
    print()

##########################################################################################

countdown()

# Variabile che conta a quante ripetizioni si trova il programma
ripetizioni = 1

# Limite al numero di ripetizioni
limite = 100

while(ripetizioni < limite + 1):
    print(f"[@@@] Ripetizione {ripetizioni}")
    run()
    ripetizioni += 1

xlib.XCloseDisplay(display)