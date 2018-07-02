#!/usr/bin/env python
import subprocess
import csv
import os
import time

class HackingDrones:
    """Trying to hack drones and cool stuff. This automates the process using the aircrack modules"""
    def __init__(self, known_ips, dirc = os.getcwd()):
        """The init method instantiates the known list of ips to track. It also runs the full automation process."""
        self.known_ips = known_ips
        self.matched_ips = dict()   #Format for this dictionary is potential matches' {IP: [channel, name]}
        self.start()		    #This functions results in a outputted csv file of network information 
        self.identification()
        os.chdir(dirc)

    def run_bash(self, cmd):
        """This function allows the python script to execute bash commands"""
        subprocess.call("{}".format(cmd), shell=True)
        
    def start(self):
        """This method scans for Wifi networks and outputs them as a csv file to the desktop.
	   The user only has to enact the Keyboard interrupt to stop the scanning when desired."""
        self.run_bash("echo Disconnecting from wifi networks")
        time.sleep(1)
        self.run_bash("airmon-ng")
        time.sleep(1)
        self.run_bash("echo Enabling Monitor Mode")
        time.sleep(1)
        self.run_bash("airmon-ng start wlan0mon")
        self.run_bash("echo Scanning for local network, hit the Keyboard Interrupt 'ctrl+C' to stop scanning")
        time.sleep(1)
        try:
	        self.run_bash("airodump-ng wlan0 -w output --output-format csv")
        except KeyboardInterrupt:
	        self.run_bash("killall airodump-ng")
    
    def read_files(self, file_name, expected_num_values, seperator = ", "):
        """A generic read file generator to check bad file inputs and read line by line"""
        try:
            fp = open(file_name, 'rb') 
        except FileNotFoundError: 
            raise FileNotFoundError ("Could not open {}".format(file_name))
        else:
            with fp:
                x = 0
                for line in fp:
                    if x > 1:
                        st_line = str(line)
                        l = st_line.strip().split(seperator)
                        if len(l) == expected_num_values:
                            yield l
                    x += 1

    def identification(self):
        """This function takes the information from the generator and then attempts to identify if a 
        returned IP is a known drone IP, it then compiles a dictionary of matched IP's"""
        read_network_ips = self.read_files("output-01.csv", 14, seperator = ", ")
        for bssid, first_time_seen, last_time_seen, channel, speed, privacy, cipher, authentication,\
            power, beacons, IV, LAN, en, name in read_network_ips:
            if bssid[:8] in self.known_ips:
                print("Match found at this IP: {}".format(bssid))
                self.matched_ips[bssid] = [channel.strip(), name]
        print("Here are all the drone IP's: {}".format(self.matched_ips))
        return self.matched_ips

    def clean_up(self, file_name):
        """This function deletes the scan results and other output files to prepare for the next 
        run-through of the script."""
        try:
            os.path.isfile(file_name)
        except:
            raise FileNotFoundError ("Could not find {}".format(file_name))
        os.remove(file_name)
        return print("Scan results cleared.")

def main():
    """This is where we run the program to check for known IPs"""
    known_ips = set(["18:64:72", "3C:1E:04", "00:27:22"])
    hacking_drones = HackingDrones(known_ips)

if __name__ == "__main__":
    main()
