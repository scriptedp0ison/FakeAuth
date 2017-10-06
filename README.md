# Attention:
There has been an issue with how to use this framework for attacking networks. This issue will be updated this weekend

# Updates
* Adding files for MAC Spoofing and MAC checking
* Adding a bash script for dependencies (you need to chmod u+rwx)
* If you have any other issues, feel free to comment. I will help

# FakeAuth
FakeAuthentication Network Attack framework written in python3, and made with poison

# Network Injection
Inject wireless Deauthentication frames from wireless access points within a certain basic service set, or within an extended service set to capture a 4 way handshake, and perform local based dictionary based attacks against the .cap file.

# Mac Spoofing (Coming in future update)
Spoof your wireless network cards media access control address, when performinng arbituary network attacks, to mask your presence (slightly)

# Media Access Control Address Checking
Check the current state of your media access control address by importing system defined plugins such as fakeauth/network/check/mac_address to get status information about wether or not your MAC address is properly masked or not

# Feautures
* Fake Authentication attacks against WEP (Wired Equivalent Privacy) related IEEE (Institute of Electrical and Electronics Engineers) 802.11 wifi protocols in order to attacks vulnerable networks 
* Inject Deauthentication packets across a network to capture a 4 way handshake.
* Inject Deauthentication frames across a network to kick off a single device or all devices
* Time based deauthentication attacks. Allow target to reconnect after every x seconds/minutes and deauthenticate 3 times
* Fake Authentication attacks, fake network authentication on "stubborn" access points
