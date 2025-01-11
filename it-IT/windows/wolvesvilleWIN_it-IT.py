# Fork of the bot made by RedScorpion
# VERSIONE ITALIANA

import pyautogui as gui
import win32api as win
import win32con
import numpy
import time

# CAMBIAMI
x = 1443
y = 1007

# y BACKUP used to restore y to a normal value
backup = y

# Tempo fisso da aspettare tra uno spostamento ed un altro
sleep = 0.05

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
            
# Funzione che trova i bottoni WATCH VIDEO e SPIN 
def findButton(x, y):
    tries = 1
    max_tries = 5
    while(True):
        win.SetCursorPos((x, y))
        try:
            if gui.pixelMatchesColor(x, y, (229, 229, 231)):
                x, y = offset(x, y)
                click(x, y)
                break
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
                print("[!!!] Tentativi esauriti, fermo lo script")
                return
            
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
    findButton(x, y) # WATCH VIDEO
    
    wait = numpy.random.randint(37, 45) + approx()
    print("[1/3] WATCH BUTTON... OK")
    print(f"[===] Attesa: {wait} secondi")
    time.sleep(wait)
    
    back(x, y) # BACK
    wait = numpy.random.randint(5, 10) + approx()
    print("[2/3] AD BUTTON... OK")
    print(f"[===] Attesa: {wait} secondi")
    time.sleep(wait)
    
    findButton(x, y) # SPIN
    print(f"[{3}/{3}] SPIN... OK")
    
    # ATTESA FINALE
    wait = numpy.random.randint(15, 20) + approx()
    print(f"[===] Attesa finale: {wait} secondi")
    time.sleep(wait) 
    print()
    
def countdown():
    startup = 5
    print("[@@@] SCRIPT REALIZZATO DA maiku ")
    print("[@@@] Wolvesville AD BOT WINDOWS versione 1.6.2")
    print("[@@@] Avvio dello script tra", startup, "secondi...")
    time.sleep(startup)
    print()

# Inizio del programma

ripetizioni = 1
countdown()
    
limite = 50 # IMPOSTA IL LIMITE DA TE DESIDERATO   

while ripetizioni < limite+1:
    print(f"[@@@] Ripetizione {ripetizioni}")
    run()
    ripetizioni += 1