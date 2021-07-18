from pylibpcap.pcap import sniff


for plen, t, buf in sniff("en0", filters="port 53", count=-1, promisc=1, out_file="pcap.pcap"):
    print("[+]: Payload len=", plen)
    print("[+]: Time", t)
    print("[+]: Payload", buf)