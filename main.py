
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


for i in do:
    action=i[0]
    addr=i[1]
    togive = None
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
            else
                
    if action == "release":
        print("rel")