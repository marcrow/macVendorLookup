import sys

def find_vendor(mac):
    file = "mac/"+mac[5]+".txt"
    with open(file,"r") as vendor_address:
        for line in vendor_address:
            tab = line.split("\t")
            if mac[:6] == tab[0]:
                return tab[1].replace("\n","")
    print "Vendor not found"
    return ""

if len(sys.argv) != 2:
    print "Usage python macVendorLookup.py mac-address"
    exit(-1)
print find_vendor(sys.argv[1])

