import socket
import sys
import select
import threading

def thread_task(conn, ip_client, port_client,i):
	print("thread craeted for {}:{}".format(ip_client,port_client))
	print("number of threads: {}".format(len(client_list)))
	is_active = True
	while is_active:
		msg =  conn.recv(2048)
		if "-quit-" in msg:
			conn.close()
			print("connected to {}:{} closed".format(ip_client,port_client))
			sys.exit()
		else:
			print("client #{} ({}:{}) says: {}".format(i,ip_client,port_client, msg))
			for c in client_list:
				if c != conn:
					c.send(b"client #{} ({}:{}) says: {}".format(i,ip_client,port_client, msg))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('server created')
IP_address = "127.0.0.1"
port = 5000
i = 0
try:
	server.bind((IP_address, port))
except:
	print('bind failed')
	sys.exit()
server.listen(100)
print('server is listening...')
client_list = []
while True:
	conn, addr = server.accept()
	client_list.append(conn)
	ip_client, port_client = str(addr[0]), str(addr[1])
	print("connected to : {}:{}".format(ip_client,port_client))
	conn.sendall(b"Hello {}:{} :) ".format(ip_client,port_client))
	try:
		i = i + 1
		th = threading.Thread(target=thread_task, args=(conn,ip_client,port_client,i,))
		th.start()
	except:
		print("thread did not start")
		continue

conn.close()
server.close()
