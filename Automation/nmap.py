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


def get_all_vals(var):
    if type(var) is list:
        for dvar in var:
            for key, value in dvar.items():
                if type(value) is dict:
                    get_all_vals(value)
                else:
                    print(key,":", value)
    else:
        print(var)


def print_menu():
    command = int(input("select 1 for nmap OS scan, 2 for nmap Version scan, 3 for nmap subnet scan"))
    pos=0
    for target in targets:
        print(pos, target)
        pos+=1

    tgt = int(input("enter the number associated with the chosen target "))

    if command == 1:
        output = nmap_os_scan(targets[tgt])
    elif command == 2:
        output = nmap_version_scan(targets[tgt])
    elif command == 3:
        output = nmap_subnet_scan(targets[tgt])
    else:
        output = None

    print(get_all_vals(output))


if __name__ == "__main__":
    # execute only if run as a script
    print_menu()