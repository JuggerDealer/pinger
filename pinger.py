#A simple ping checker
#Made by JuggerDealer

from pythonping import ping
from os import system, name
import time

def clear(): 
    if name == 'nt': 
        _ = system('cls') 

print("    _                             _                     _                       ")
print("   (_)                           ( )                   (_)                      ")
print("    _ _   _  __ _  __ _  ___ _ __|/ ___           _ __  _ _ __   __ _  ___ _ __ ")
print("   | | | | |/ _` |/ _` |/ _ \ '__| / __|         | '_ \| | '_ \ / _` |/ _ \ '__|")
print("   | | |_| | (_| | (_| |  __/ |    \__ \         | |_) | | | | | (_| |  __/ |   ")
print("   | |\__,_|\__, |\__, |\___|_|    |___/         | .__/|_|_| |_|\__, |\___|_|   ")
print("  _/ |       __/ | __/ |                         | |             __/ |          ")
print(" |__/       |___/ |___/                          |_|            |___/           ")

answer = input("Start pinger ? (y/n)  --->  ")
if answer == "y":
	while answer == "y":
		response = ping("1.1.1.1", verbose=False, timeout=10, count=1)
		clear()
		print(" __     __                        _                  _     ")
		print(" \ \   / /                       (_)                (_)    ")
		print("  \ \_/ /__  _   _ _ __     _ __  _ _ __   __ _      _ ___ ")
		print("   \   / _ \| | | | '__|   | '_ \| | '_ \ / _` |    | / __|")
		print("    | | (_) | |_| | |      | |_) | | | | | (_| |    | \__ \           ----> " + str(response.rtt_avg_ms) + "ms")
		print("    |_|\___/ \__,_|_|      | .__/|_|_| |_|\__, |    |_|___/")
		print("                           | |             __/ |           ")
		print("                           |_|            |___/            ")
		if response.rtt_avg_ms == 10000:
			print("ERROR ! Request timed out. Check your internet connection.")
		time.sleep(0.5)
else:
	pass