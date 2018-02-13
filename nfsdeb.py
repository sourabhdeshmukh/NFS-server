import os
import socket
import fileinput

def install():
    os.system('sudo apt -y install nfs-kernel-server')

def bakup():
    os.system('sudo cp /etc/exports /etc/exports.bkp')
    os.system('sudo cp /etc/idmapd.conf /etc/idmapd-conf.bkp')

def config():
    file1 = open("/etc/idmapd.conf", 'w+')
    s = 'Domain ='
    s1 = socket.getfqdn()
    s2 = s1 + s2
    s3 = str('')
    for line in fileinput.input(file1):
        if s3 in line:
            file1.write(line.replace(s3, s2))
    file1.close()

    file2 = open("/etc/exports", 'w+')
    s4 = '\home'
    s5 = str(s4+"   "+s1+"(rw,sync)")
    file2.write(s5)
    file2.close()

def serviceStart():
    os.system('sudo systemctl restart nfs-server')

install()
bakup()
config()
firewalld()
serviceStart()
