import csv
import os

class HackingDrones:
    """Trying to hack drones and cool stuff"""
    def __init__(self, known_ips):
        """The init method instantiates the known list of ips to track"""
        self.known_ips = known_ips
        self.matched_ips = dict()   #format for this dictionary is potential matches' {IP: [channel, name]}
        self.identification()
        #print(os.listdir)
        

    def read_files(self, file_name, seperator = ", "):
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
                        if len(l) == 14:
                            yield l
                    x += 1

    def identification(self):
        """This function takes the information from the generator and then attempts to identify if a 
           returned IP is a known drone IP, it then compiles a dictionary of matched IP's"""
        read_network_ips = self.read_files("output-01.csv", seperator = ", ")
        for bssid, first_time_seen, last_time_seen, channel, speed, privacy, cipher, authentication, power, beacons, IV, LAN, name, end in read_network_ips:
            if bssid[2:10] in self.known_ips:
                print("Match found at this IP: {}".format(bssid[2:]))
                self.matched_ips[bssid[2:]] = [channel, name]
        print("Here are all the drone IP's: {}".format(self.matched_ips))
        return self.matched_ips

def main():
    """This is where we run the program to check for known IPs"""
    known_ips = set(["3C:1E:04"])
    hacking_drones = HackingDrones(known_ips)

if __name__ == "__main__":
    main()