import nmap3
import json

targets = ["192.168.64.1","192.168.65.1","192.168.65.24","192.168.65.34","almost.hckbl.net","192.168.65.0/24"]


def nmap_os_scan(target):
    nmap = nmap3.Nmap()
    return nmap.nmap_os_detection(target)


def nmap_version_scan(target):
    nmap = nmap3.Nmap()
    return nmap.nmap_version_detection(target)


def nmap_subnet_scan(target):
    nmap = nmap3.Nmap()
    return nmap.nmap_subnet_scan(target)


def nmap_syn_scan(target):
    nmap = nmap3.NmapScanTechniques()
    return nmap.nmap_syn_scan(target)


def nmap_null_scan(target):
    nmap = nmap3.Nmap()
    return nmap.scan_command(target, "", "-sN")


def nmap_udp_scan(target):
    nmap = nmap3.NmapScanTechniques()
    return nmap.nmap_udp_scan(target)


def print_menu():
    command = int(input("select 1 for nmap OS scan, 2 for nmap Version scan, 3 for nmap subnet scan, 4 for SYN scan" +
                        " 5 for NULL scan, 6 for UDP scan"))
    pos = 0

    for target in targets:
        print(pos, target)
        pos += 1

    tgt = int(input("enter the number associated with the chosen target "))

    if command == 1:
        output = nmap_os_scan(targets[tgt])
    elif command == 2:
        output = nmap_version_scan(targets[tgt])
    elif command == 3:
        output = nmap_subnet_scan(targets[tgt]).items()
    elif command == 4:
        output = nmap_syn_scan(targets[tgt]).items()
    elif command == 5:
        output = nmap_null_scan(targets[tgt]).items()
    elif command == 6:
        output = nmap_udp_scan(targets[tgt]).items()
    else:
        output = None

    print(output)


if __name__ == "__main__":
    # execute only if run as a script
    print_menu()
