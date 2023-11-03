import datetime
import pandas as pd
import subprocess

try:
    import keyboard
except ImportError:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'keyboard'])
    import keyboard

print("Tryk på mellemrum for at gemme en tid. Luk programmet med ESC. Tiderne gemmes kun hvis du bruger ESC til at lukke programmet. \n")

filename = input("Hvilken fil skal tiderne gemmes i? (uden filendelse) \n")

print("\n Filen gemmes i {}. \n Tidtagning startet. Tryk mellemrum for at gemme tider.".format(filename + ".xlsx"))

times = []
unixtimes = []

def log_time():
    now = datetime.datetime.now()
    times.append(now)
    unixtimes.append(now.timestamp())

    print(f"\n Bil nr: {len(times)} | Tid gemt: {now}")

def on_spacebar(event):
    if event.name == 'space':
        log_time()

keyboard.on_press_key('space', on_spacebar)

while True:
    if keyboard.is_pressed('esc'):
        break

df = pd.DataFrame({'Dato og klokkeslet': times, "Unix timestamp": unixtimes})
df.to_excel(filename + ".xlsx", index=True)