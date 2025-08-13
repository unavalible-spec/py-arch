import time
import random
from colorama import Fore
import os
import playsound
import subprocess
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(random.uniform(2.1, 5.32))
print("Importing modules..")
time.sleep(0.2)
try:
    import art
    print(Fore.WHITE + "imported art")
except:
    print(Fore.YELLOW + "Failed to import art" + Fore.RESET)

time.sleep(0.63)
try:
    import requests
    print(Fore.WHITE + "imported requests")
except:
    print(Fore.YELLOW + "Failed to import requests" + Fore.RESET)
time.sleep(0.11)
try:
    import shutil
    print(Fore.WHITE + "imported shutil")
except:
    print(Fore.YELLOW + "Failed to import shutil" + Fore.RESET)
time.sleep(0.974)
try:
    import json
    print(Fore.WHITE + "imported json")
except:
    print(Fore.YELLOW + "Failed to import json" + Fore.RESET)
    
time.sleep(0.11)
try:
    import playsound
    print(Fore.WHITE + "imported playsound")
except:
    print(Fore.YELLOW + "Failed to import playsound" + Fore.RESET)
time.sleep(1.52)
try:
    playsound.playsound("beep.wav")
except:
    subprocess.Popen(["termux-media-player", "play", "beep_fixed.wav"])

print(f"Finished importing, total time: {0.2 + 0.63 + 0.11 + 0.974 + 1.52} seconds")