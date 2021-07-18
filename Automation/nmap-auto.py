import nmap3

def nmap_os_scan(target):
    nmap = nmap3.Nmap()
    return nmap.nmap_os_detection(target)

def nmap_version_scan(target):
    nmap = nmap3.Nmap()
    return nmap.nmap_version_detection(target)

def nmap_null_scan(target):
    nmap = nmap3.Nmap()
    return nmap.scan_command(target, "", "-sN")

result = nmap_null_scan("192.168.65.24").items()

print(result)
