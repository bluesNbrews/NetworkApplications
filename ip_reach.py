import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

	for ip in list:
		ip = ip.rstrip("\n")