import datetime
import pandas as pd
import subprocess
import time
import threading

try:
    import keyboard
except ImportError:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'keyboard'])
    import keyboard

print("Tryk på mellemrum for at gemme en tid. Luk programmet med ESC. Tiderne gemmes kun hvis du bruger ESC til at lukke programmet. \n")

filename = input("Hvilken fil skal tiderne gemmes i? (uden filendelse) \n")

print("\n Filen gemmes i {}. \n Tidtagning startet. Tryk mellemrum for at gemme tider og enter for at slette den sidste tid.".format(filename + ".xlsx"))

times = []
unixtimes = []
key_pressed = False

def log_time():
    now = datetime.datetime.now()
    times.append(now)
    unixtimes.append(now.timestamp())
    print(f"\n Antal tider: {len(times)} | Tid gemt: {now}")

def reset_key_pressed():
    global key_pressed
    key_pressed = False

def on_any_key(event):
    global key_pressed
    if key_pressed:
        return
    if event.name == 'space':
        log_time()
        key_pressed = True
        threading.Timer(0.1, reset_key_pressed).start()
    elif event.name == 'delete' or event.name == 'backspace':
        if times and unixtimes:
            times.pop()
            unixtimes.pop()
            print(f"\n Antal tider: {len(times)} | Sidste tid slettet")
        key_pressed = True
        threading.Timer(0.1, reset_key_pressed).start()

keyboard.on_press(on_any_key)

while True:
    if keyboard.is_pressed('esc'):
        break

df = pd.DataFrame({'Dato og klokkeslet': times, "Unix timestamp": unixtimes})
df.to_excel(filename + ".xlsx", index=False)

