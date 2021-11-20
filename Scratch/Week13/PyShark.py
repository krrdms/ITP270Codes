import pyshark


def capture_dns():
    display_filter = "src port 53"
    cap = pyshark.LiveCapture(interface="en0", bpf_filter=display_filter)
    for pkt in cap.sniff_continuously(packet_count=50):
        print("dns qry name: %s" % pkt.dns.qry_name)
        print("dns response: %s" % pkt.dns.a)
        print()


def capture_web():
    display_filter = "http.request"
    cap = pyshark.LiveCapture(interface="en0", display_filter=display_filter)
    for pkt in cap.sniff_continuously(packet_count=50):
        print("host: %s" % pkt['http'].host)
        print("browser: %s" % pkt['http'].user_agent)
        print()


def user_prompt():
    print("Enter 1 for live HTTP")
    print("Enter 2 for live DNS")
    return int(input("enter choice:"))


def process_user_prompt(choice):
    if choice == 1:
        capture_web()
    elif choice == 2:
        capture_dns()
    else:
        print("invalid selection")
        return False
    return True


def main():
    while process_user_prompt(user_prompt()):
        print()
        continue


if __name__ == '__main__':
    main()
