# Installation script by Vip3r_Li0n

import os

print("This module is for installing Nethunter Kali Linux without root in termux.")
os.system("pkg update")
os.system("pkg upgrade -y")
print("It will take some time be patient.")
os.system("pkg install fish -y")
print("Enter into fish mode")
os.system("fish")
print("give permissions to phone storage 'press allow'")
os.system("termux-setup-storage")
os.system("pkg install wget -y")
print("Initializing Kali nethunter repo")
os.system("wget https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-project/raw/master/nethunter-rootless/install-nethunter-termux")
os.system("ls")
os.system("chmod +x install-nethunter-termux")
print("Downloading and installing kali linux in termux")
os.system("./install-nethunter-termux")
print("set password for VNC or start kex")
os.system("nethunter")
os.system("cat /etc/os-release | grep '\bNAME='")
os._exit(1)