import os
import socket

print("""\033[1;34m
	            ⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⡶⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⢿⣷⣀⣀⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⢀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⣼⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡀⢹⠀⢻⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠘⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           Honeypot made by \033[1;31mAcky\n\n\n""")
print("\033[1;31m[ 1 ] FTP Server\n[ 2 ] SSH Server\n")
options = int(input("\033[1;34mOptions : \033[1;31m"))
if options == 1:
	port = int(input("\033[1;34mPort :\033[1;31m "))
	port = str(port)
	print('\033[1;34mListening to port \033[1;31m' + port + '\033[1;34m\n')
	ip = 'localhost'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = int(port)
	s.bind((ip, port))
	s.listen()
	addr, ip = s.accept()
	print('\033[1;34mAttacker found - \033[1;31m' + str(ip))
	addr.send("Connect to FTP Server Backup Admin\n".encode())
	while True:
		addr.send("ftp> ".encode())
		data = addr.recv(1024)
		if data == b'ls\n':
			print('\033[1;34mCommand executed - \033[1;31mls')
			addr.send(".\n".encode())
			addr.send("..\n".encode())
			addr.send("readme.txt\n".encode())
		elif data == b'ls -a\n':
			print('\033[1;34mCommand executed - \033[1;31mls')
			addr.send(".\n".encode())
			addr.send("..\n".encode())
			addr.send(".ssh\n".encode())
			addr.send("readme.txt\n".encode())
		elif data == b'ls -la\n':
			print('\033[1;34mCommand executed - \033[1;31mls')
			addr.send("""drwxr-xr-x  3 ftp ftp 4096 jan  6 17:06 .
drwxr-xr-x 22 ftp ftp 4096 jan  6 17:06 ..
-rw-r--r--  1 ftp ftp   11 jan  6 17:06 readme.txt
drwxr-xr-x  2 ftp ftp 4096 jan  6 17:06 .ssh
""".encode())
		elif data == b'get readme.txt\n':
			print('\033[1;34mCommand executed - \033[1;31mget readme.txt')
			addr.send("Permission denied\n".encode())
		elif data == b'cd .ssh\n':
			print('\033[1;34mCommand executed - \033[1;31mcd .ssh')
			addr.send("Permission denied\n".encode())
		else:
			print('\033[1;34mCommand executed - \033[1;31m' + str(data))
			addr.send("Command invalid\n".encode())
elif options == 2:
	port = int(input("\033[1;34mPort :\033[1;31m "))
	port = str(port)
	print('\033[1;34mListening to port \033[1;31m' + port + '\033[1;34m\n')
	ip = 'localhost'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = int(port)
	s.bind((ip, port))
	s.listen()
	addr, ip = s.accept()
	print('\033[1;34mAttacker found - \033[1;31m' + str(ip))
	addr.send("SSH Backup v1.0\n".encode())
	while True:
		addr.send("backup@localhost~# ".encode())
		recv = addr.recv(1024)
		if recv == b"ls -a\n":
			addr.send(".bashrc .ssh readme.txt admin.txt\n".encode())
			print('\033[1;34mCommand executed - \033[1;31mls -a')
		elif recv == b"ls -la\n":
			addr.send("""total 24
drwxr-xr-x  4 root root 4096 fev  6 05:00 .
drwxr-xr-x 22 root root 4096 fev  6 05:00 ..
-rw-r--r--  1 backup backup   35 fev  6 11:08 admin.txt
-rwxr-xr-x  2 backup backup 4096 fev  6 11:08 .bashrc
-rw-r--r--  1 backup backup   18 fev  6 11:08 readme.txt
drwxr-xr-x  2 root root 4096 fev  6 05:48 .ssh\n
""".encode())
			print('\033[1;34mCommand executed - \033[1;31m ls -la')
		elif recv == b"ls\n":
			addr.send("readme.txt admin.txt\n".encode())
			print('\033[1;34mCommand executed - \033[1;31m ls')
		elif recv == b"cat /proc/version\n":
			addr.send("Linux version 5.4.0-90-generic (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #101-Ubuntu SMP Tue Sep\n".encode())
			print('\033[1;34mCommand executed - \033[1;31m cat /proc/version')
		elif recv == b"cat admin.txt\n":
			addr.send("Hello, developers, please limit developer access, I don't want to deal with fights from my boss - Robson\n".encode())
			print('\033[1;34mCommand executed - \033[1;31m cat admin.txt')
		elif recv == b"cat readme.txt\n":
			addr.send("We are using a vulnerable version, please change - Clebson\n".encode())
			print('\033[1;34mCommand executed - \033[1;31m cat readme.txt')
		elif recv == b"find / -perm -4000 2>/dev/null\n":
			print('\033[1;34mCommand executed - \033[1;31m find / -perm -4000 2>/dev/null')
			addr.send("""/usr/bin/chfn
/usr/bin/ksu.mit
/usr/bin/mount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd\n
""".encode())
		elif recv == b"wget\n":
			addr.send("""wget: falta o URL
Uso: wget [OPÇÃO]... [URL]...

Tente "wget --help" para mais opções.\n
""".encode())
			print('\033[1;34mCommand executed - \033[1;31m wget')
		elif recv == b"netcat\n":
			addr.send("""usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
	  [-m minttl] [-O length] [-P proxy_username] [-p source_port]
	  [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit]
	  [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]]
	  [destination] [port]\n
""".encode())
			print('\033[1;34mCommand executed - \033[1;31m netcat')
		elif recv == b"curl\n":
			addr.send("curl: try 'curl --help' or 'curl --manual' for more information\n".encode())
			print('\033[1;34mCommand executed - \033[1;31m curl')
		else:
			addr.send("comando não encontrado\n".encode())
			print('\033[1;34mCommand executed - \033[1;31m' + " " + str(recv))