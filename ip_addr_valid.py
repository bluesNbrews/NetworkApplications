import sys

#Checking octets
def ip_addr_valid(list):

	for ip in list:
		ip = ip.rstrip("\n")
		octet_list = ip.split('.') 

