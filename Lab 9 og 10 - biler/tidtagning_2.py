import datetime
import pandas as pd
import subprocess
import threading

try:
    import keyboard
except ImportError:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'keyboard'])
    import keyboard

print("Tryk på mellemrum for at gemme en tid. Luk programmet med ESC. Tiderne gemmes kun hvis du bruger ESC til at lukke programmet. \n")

filename = input("Hvilken fil skal tiderne gemmes i? (uden filendelse) \n")

print("\n Filen gemmes i {}. \n Tidtagning startet. Tryk mellemrum for at gemme tider og enter for at slette den sidste tid.".format(filename + ".xlsx"))

unixtime = 0
delta_times = []
key_pressed = False

def log_time():
    global time
    global unixtime
    now = datetime.datetime.now()
    unixtime = now.timestamp()

def reset_key_pressed():
    global key_pressed
    key_pressed = False

def on_any_key(event):
    global key_pressed
    if key_pressed:
        now = datetime.datetime.now()
        delta_times.append(now.timestamp() - unixtime)
        print(f"\n Antal tider: {int(len(delta_times))} | Tid gemt: {delta_times[-1]}")
        key_pressed = False
        return
    if event.name == 'space':
        log_time()
        key_pressed = True
    elif event.name == 'delete' or event.name == 'backspace':
        if delta_times:
            delta_times.pop()
            print(f"\nSidste tid slettet | Antal tider: {len(delta_times)}")
        key_pressed = True
        threading.Timer(0.1, reset_key_pressed).start()

keyboard.on_press(on_any_key)

while True:
    if keyboard.is_pressed('esc'):
        break

print(delta_times)

df = pd.DataFrame({'Delta_times': delta_times})
df.to_excel(filename + ".xlsx", index=False)

