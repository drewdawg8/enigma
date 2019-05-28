import optparse
from socket import *



def connScan(tgtHost, tgtPort):
	tgtPort = int(tgtPort)
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('Hello world.')
		results = connSkt.recv(100)
		print('[+]%d/tcp open' % tgtPort)
		print('[+]' + str(results))
		connSkt.close()
	except:
		print('[-]%d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print('[-] Cannot Resolve %s: Unknown host' % tgtHost)
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('\n[*] Scan results for: ' + tgtName[0])
	except:
		print('\n[*] Scan results for: ' + tgtIP)
	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		print('\n[+] Scanning port ' + tgtPort)
		connScan(tgtHost, tgtPort)


def main():
	parser = optparse.OptionParser('usage: python port_scanner.py -H <target host> -p <target ports>')
	parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
	parser.add_option('-p', dest = 'tgtPorts', type = 'string', help = 'specify target ports seperated by commas')
	(options,args) = parser.parse_args()

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPorts).split(',')

	if tgtHost == None or tgtPorts[0] == None:
			print(parser.usage)
			exit(0)

	portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
	main()