from scapy.all import *
import sys
from datetime import datetime
import socket

# Figure out the IP address of the first non-lo interface
localIPAddr = socket.gethostbyname(socket.gethostname())

# Ports to listen for
# The line below listens for selected ports, the commented out line
# listens for all ports
tcpPorts = [80, 443, 3389, 3306, 1433, 5900, 445, 135]

# Filters do not work too well on VM interfaces, so we will build a filter
# lfilters are python functions that apply to each packet

'''
If a filter function returns True, that means the packet
met whatever conditions were specified.  If the packet did
not meet specified conditions, then we return False.
'''


def build_lfilter(pkt):
    # Exclude packets that come from this machine
#    if IP in pkt:
#        if pkt[IP].src == localIPAddr:
#            return False

    if TCP in pkt and pkt[TCP].dport in tcpPorts:
        return True
    else:
        return False


'''
This function outputs basic information about the packet.

If you wanted to do something more than print to the screen
(like write to a log or send an e-mail, you could do that
here instead.
'''


def parsePacket(pkt):
    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M')
    if IP in pkt:
        sourceAddr = pkt[IP].src
        destAddr = pkt[IP].dst
    else:
        print('[{0}] Packet not an IP packet'.format(currentTime))
        return

    if TCP in pkt:
        sourcePort = pkt[TCP].sport
        destPort = pkt[TCP].dport
        print('[{0}] [TCP] {1}:{2} -> {3}:{4}'.format(currentTime, sourceAddr, sourcePort, destAddr, destPort))
    return


while True:
    '''
    prn is called to process each packet
    count = 0 means sniff an unlimited number of packets
    '''
    try:
        sniffer = sniff(lfilter=build_lfilter, count=0, prn=parsePacket)
        # If we Ctrl-C, then exit
        sys.exit()
    except socket.error:
        print('This script must be run as root / Administrator.  Exiting...')
        sys.exit()