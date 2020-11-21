import socket

port_list = {21:"FTP", 22:"SSH", 23:"Telnet",
             25:"SMTP", 80:"HTTP", 110:"POP",
             143: "IMAP", 443:"HTTPS", 445:"Windows Domain",
             587:"Sendmail", 3306:"MySQL", 3389:"MS Remote Desktop",
             5900:"VNC Remote Desktop"}

targets = ["192.168.65.49"]

def grab_banner(soc):
    soc.sendall('Hello\r\n'.encode())
    response = soc.recv(1024)
    print(f'[*] banner: {response}')

def connect_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.connect((ip, port))
            print(f'[*] {port} / tcp open - {port_list.get(port)}')
            grab_banner(soc)
    except socket.error as err:
        print(f'[*] {port} / tcp closed - {err}')

def main():
    for target in targets:
        print(f'[+] scanning {target}')
        for port in port_list.keys():
            connect_port(target, port)


if __name__ == '__main__':
    main()
