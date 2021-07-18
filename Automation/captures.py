import pyshark

def capture_web_traffic ():
    display_filter = "http.request"
    cap = pyshark.LiveCapture(interface="en0", display_filter=display_filter)
    for pkt in cap.sniff_continuously(packet_count=10):
        print("host: %s" % pkt['http'].host)
        print("agent: %s" % pkt['http'].user_agent)

def capture_saved_web_traffic():
    display_filter = "http.request"
    cap = pyshark.FileCapture("http.pcap", display_filter=display_filter)
    for pkt in cap:
        print("host: %s" % pkt['http'].host)
        print("agent: %s" % pkt['http'].user_agent)


def capture_saved_ftp_traffic():
    display_filter = "ftp"
    cap = pyshark.LiveCapture(interface="en0", display_filter=display_filter)
    for pkt in cap.sniff_continuously(packet_count=10):
        try:
            if pkt['ftp'].request_command and pkt['ftp'].request_arg:
                print("command: %s; arg: %s" % (pkt['ftp'].request_command, pkt['ftp'].request.arg))
            elif pkt['ftp'].response_code and pkt['ftp'].response_arg:
                print("code: %s; arg: %s" % (pkt['ftp'].response_code, pkt['ftp'].response_arg))
        except AttributeError:
            pass


capture_saved_ftp_traffic()
