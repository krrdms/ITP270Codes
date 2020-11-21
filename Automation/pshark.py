import pyshark

def capture_web_traffic ():
    display_filter = "http.request"
    cap = pyshark.LiveCapture(interface="en0", display_filter=display_filter)
    for pkt in cap.sniff_continuously(packet_count=10):
        print("host: %s" % pkt['http'].host)
        print("agent: %s" % pkt['http'].user_agent)

def capture_dns_traffic():
    bpf_filter = "src port 53"
    cap = pyshark.LiveCapture(interface="en0", bpf_filter=bpf_filter)
    for pkt in cap.sniff_continuously(packet_count=5):
        print("dns qry name: %s" % pkt.dns.qry_name)
        print("dns dns resp addr: %s" % pkt.dns.a)

#capture_web_traffic()
#capture_dns_traffic()


def capture_web_traffic_saved ():
    display_filter = "http.request"
    cap = pyshark.FileCapture("http.pcap", display_filter=display_filter)
    for pkt in cap:
        print("host: %s" % pkt['http'].host)
        print("agent: %s" % pkt['http'].user_agent)
    cap.close()


def capture_ftp_traffic_saved ():
    display_filter = "ftp"
    cap = pyshark.FileCapture("ftp.pcap", display_filter=display_filter)
    for pkt in cap:
        try:
            if pkt['ftp'].response_code and pkt['ftp'].response_arg:
                print("code: %s" % pkt['ftp'].response_code)
                print("argument: %s" % pkt['ftp'].response_arg)
                print(pkt['ftp'])
            elif pkt['ftp'].request_command and pkt['ftp'].request_arg:
                print("command: %s" % pkt['ftp'].request_command)
                print("argument: %s" % pkt['ftp'].request_arg)
                print(pkt['ftp'])
        except AttributeError:
            pass
    cap.close()

def capture_dns_traffic_saved():
    display_filter = "dns"
    cap = pyshark.FileCapture("dns-bpf.pcap", display_filter=display_filter)
    for pkt in cap:
        if pkt.dns.qry_name:
            print("dns qry name: %s" % pkt.dns.qry_name)
        if pkt.dns:
            print("dns dns resp addr: %s" % pkt.dns)


#capture_web_traffic_saved()
#capture_ftp_traffic_saved()
capture_dns_traffic_saved()
