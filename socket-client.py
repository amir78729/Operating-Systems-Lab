import socket
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "127.0.0.1"
port = 5000
try:
	server.connect((IP_address, port))
except:
	print("failed")
	sys.exit()


while True:
	socket_list = [sys.stdin, server]
	read_socket, xx, xxx = select.select(socket_list, [], [])
	for sock in read_socket:
		if sock == server:
			msg = sock.recv(2048)
			print(msg)
		else:
			# print("type -QUIT- to quit")
			print('enter something: ')
			msg = sys.stdin.readline()
			server.send(msg)
sys.exit()
server.close()
