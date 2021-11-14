import nmap3
from elevate import elevate


def process_input(nmap):
    result = {}
    targets = []
    with open("nmap-auto-targets.txt") as f:
        _targets = f.readlines()
    for target in _targets:
        choice,tgt = target.split(",")
        choice = int(choice)
        if choice == 0:
            print("Trying OS Detection:")
            result = nmap.nmap_os_detection(tgt)
            print(result[0].items())
        elif choice == 1:
            print("Trying Version Detection:")
            result = nmap.nmap_version_detection(tgt)
            print(result[0].items())
        elif choice == 2:
            print("Trying Null Scan:")
            result = nmap.nmap_stealth_scan(tgt, "", "-sN")
            print(result)

    return True


def main():
    nmap = nmap3.Nmap()
    process_input(nmap)


if __name__ == '__main__':
    main()
