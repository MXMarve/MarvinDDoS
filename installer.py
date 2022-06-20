import os
import time
import threading

def install():
    os.system("sudo apt install python3.9 > nul")
    os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py > nul")
    os.system("python3.9 get-pip.py > nul")
    os.system("sudo rm get-pip.py > nul")

if __name__ == "__main__":
  t1 = threading.Thread(target=install)

try:
    os.system("python3.9 --version > nul")
except:
    t1.start() 
    print("Installing Requirements...")
    t1.join()
    input("Install Complete. Press Enter to Continue")
    time.sleep(1)
    exit()
