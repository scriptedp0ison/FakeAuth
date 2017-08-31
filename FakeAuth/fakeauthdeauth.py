import sys
import time
import subprocess
#import fakeauth
from colorama import Fore, Back

class FakeAccessPointAuthenticationDeauthentication:
	def __init__(self, client_mac, bssid, channel, packet_count, interface):
		self.client_mac = client_mac
		self.bssid = bssid
		self.channel = channel
		self.packet_count = packet_count
		self.interface = interface
		
	client_mac = None
	bssid = None
	channel = 0
	packet_count = 0
	interface = None
	
	
		
		
