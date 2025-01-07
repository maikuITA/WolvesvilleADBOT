# Fork of the bot made by RedScorpion
# VERSIONE ITALIANA

# consiglio di usare scrcpy con un telefono android (in alternativa Bluestacks)

import pyautogui as gui
import win32api as win
import win32con
import numpy
import time

# Funzione che clicca sul bottone "WATCH VIDEO"
def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
# Funzione che preme il tasto destro del mouse per chiudere gli ad
def back(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.01)
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

# Funzione che trova il tasto "WATCH VIDEO" o "SPIN"
def find_button():
    x = CAMBIAMI
    y = CAMBIAMI
    while(True):
        win.SetCursorPos((x, y))
        # (229, 229, 231) è la combinazione RGB del bianco dei bottoni
        if gui.pixelMatchesColor(x, y, (229, 229, 231)):
            #print("DEBUG: WATCH VIDEO!!", x, ",", y)
            click(x, y)
            break
        else:
            #print("DEBUG: WATCH VIDEO non trovato a ", x, ",", y)
            y = y - 1

def approx():
    ms = numpy.random.randint(1, 10)
    return ms/100

def run():
    find_button() # WATCH VIDEO
    
    w = numpy.random.randint(37, 49)
    w += approx()
    print("[1] WATCH VIDEO... OK {attesa:",w,"secondo}")
    time.sleep(w)
    
    back(CHANGEME, CHANGEME) # BACK
    w = numpy.random.randint(5, 14)
    w += approx()
    print("[2] AD... OK {attesa:",w,"secondo}")
    time.sleep(w + approx())
    
    find_button() # SPIN
    print("[3] SPIN... OK")
    w = numpy.random.randint(15, 20)
    w += approx()
    print("[4] Attesa finale... ",w,"secondi")
    time.sleep(w + approx()) # ATTESA FINALE
    print()

def countdown():
    startup = 5
    print("### SCRIPT REALIZZATO DA maiku ")
    print("### Wolvesville AD BOT 1.5")
    print("Avvio dello script tra", startup, "secondi...")
    time.sleep(startup)
    print()

# Inizio del programma

ripetizioni = 1
countdown()

print("Modalità SENZA numero limite di ripetizioni")
print() 

while True:
    print("[?] RIPETIZIONE NUMERO:", ripetizioni)
    run()
    ripetizioni += 1