import threading
import time
from pynput.keyboard import Controller, KeyCode, Listener

czyklika = False
przelacznik = KeyCode(char='.')
klawa = Controller()

def macro():
    while True:
        if czyklika:
            klawa.press('d')
            time.sleep(1)
            klawa.release('d')
            time.sleep(1)
            klawa.press('a')
            time.sleep(1)
            klawa.release('a')
        time.sleep(3)

def zmiana(klucz):
    if klucz == przelacznik:
        global czyklika
        czyklika = not czyklika

click_thread = threading.Thread(target=macro)
click_thread.start()

with Listener(on_press=zmiana) as listener:
    listener.join()