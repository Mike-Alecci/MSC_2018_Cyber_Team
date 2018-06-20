import csv

class HackingDrones:
    """Trying to hack drones and cool stuff"""
    def __init__(self, known_ips):
        """The init method instantiates the known list of ips to track"""
        self.known_ips = known_ips
        self.matched_ips = dict()
        print("hi")
        print(self.identification())
        

    def read_files(self, file_name, seperator = ", "):
        """A generic read file generator to check bad file inputs and read line by line"""
        try:
            fp = open(file_name, 'rb') 
        except FileNotFoundError:
            raise FileNotFoundError ("Could not open {}".format(file_name))
        else:
            with fp:
                for line in fp:
                    st_line = str(line)
                    l = st_line.strip().split(seperator)
                    print(l)
                    yield l

    def identification(self):
        """This function takes the information from the generator and then attempts to identify if it is a known 
           drone IP"""
        read_network_ips = self.read_files("output-01.csv", seperator = ", ")
        for bssid, a, b, channel, d, e, f, g, h, i, j, k, l, name in read_network_ips:
            if bssid[0:8] in self.known_ips:
                self.matched_ips[bssid] = [channel, name]
        return self.matched_ips

def main():
    """This is where we run the program to check for known IPs"""
    known_ips = set("3C:1E:04")
    hacking_drones = HackingDrones(known_ips)

if __name__ == "__main__":
    main()
