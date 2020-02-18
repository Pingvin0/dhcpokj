
excluded = [x[0].rstrip() for x in [i.split(";") for i in open("excluded.csv","r",encoding="latin2")]]
reserved = dict()
current = dict()
# Create dictionary linking mac addresses to ip addresses
for i in open("reserved.csv", "r", encoding="latin2"):
	i = i.rstrip().split(";")
	reserved[i[0]] = i[1]
for i in open("dhcp.csv", "r", encoding="latin2"):
	i = i.rstrip().split(";")
	current[i[0]] = i[1]

do = [i.rstrip().split(";") for i in open("test.csv", "r", encoding="latin2")]
addresses = ['192.168.0.'+str(i) for i in range(100,200)]

def findKeyByVal(valtofind, d=current):
	for i in d:
		val = current[i]
		key = i
		if val == valtofind:
			return key
for i in do:
	action=i[0]
	addr=i[1]
	if action == "request":
		if addr in current.keys():
			break;
		else:
			if addr in reserved.keys():
				togive = reserved[addr]
				if togive in current.values():
					break;
				else:
					current[addr] = togive
			else:
				i=0
				ip = addresses[i]
				while True:
					if ip in current.values() or ip in excluded or ip in reserved.values():
						if i > 99:
							break;
						i += 1
						ip = addresses[i]
					else:
						break;
							
				if i > 99:
					continue
				else:
					current[addr] = ip
				
				
				
	if action == "release":
		del current[findKeyByVal(addr)]

dhcp = open("dhcp_kesz.csv", "w")
for i in current:
	val = current[i]
	key = i
	strt = key + ";" + val + "\n"
	dhcp.write(strt)
dhcp.close()