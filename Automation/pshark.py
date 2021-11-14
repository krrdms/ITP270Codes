import pyshark
from elevate import elevate


def capture_web_traffic ():
    display_filter = "http.request"
    cap = pyshark.LiveCapture(interface="en0", display_filter=display_filter)
    for pkt in cap.sniff_continuously(packet_count=10):
        print("host: %s" % pkt['http'].host)
        print("agent: %s" % pkt['http'].user_agent)
        print()


def capture_dns_traffic():
    bpf_filter = "src port 53"
    cap = pyshark.LiveCapture(interface="en0", bpf_filter=bpf_filter)
    for pkt in cap.sniff_continuously(packet_count=5):
        print("dns qry name: %s" % pkt.dns.qry_name)
        print("dns dns resp addr: %s" % pkt.dns.a)
        print()


def capture_web_traffic_saved ():
    display_filter = "http.request"
    cap = pyshark.FileCapture("http.pcap", display_filter=display_filter)
    for pkt in cap:
        print("pkt: %s" % pkt['http'])
        print()
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
                print()
            elif pkt['ftp'].request_command and pkt['ftp'].request_arg:
                print("command: %s" % pkt['ftp'].request_command)
                print("argument: %s" % pkt['ftp'].request_arg)
                print(pkt['ftp'])
                print()
        except AttributeError:
            print()
            pass
    cap.close()


def capture_dns_traffic_saved():
    display_filter = "dns"
    cap = pyshark.FileCapture("dns-bpf.pcap", display_filter=display_filter)
    for pkt in cap:
        try:
            if pkt.dns.qry_name:
                print("dns qry name: %s" % pkt.dns.qry_name)
            if pkt.dns:
                print("dns dns resp addr: %s" % pkt.dns)
        except AttributeError:
            continue


def user_prompt():
    print("Enter 0. to look at live HTTP traffic")
    print("Enter 1. to look at live DNS traffic")
    print("Enter 2. to look at captured HTTP traffic")
    print("Enter 3. to look at captured FTP traffic")
    print("Enter 4. to look at captured DNS traffic")
    return int(input("Enter Choice: "))


def process_user_input(choice):
    if choice == 0: capture_web_traffic()
    elif choice == 1: capture_dns_traffic()
    elif choice == 2: capture_web_traffic_saved()
    elif choice == 3: capture_ftp_traffic_saved()
    elif choice == 4: capture_dns_traffic_saved()
    else:
        print("invalid entry... exit")
        return False
    return True


def main():
    while process_user_input(user_prompt()):
        print()
        continue


if __name__ == '__main__':
    main()

