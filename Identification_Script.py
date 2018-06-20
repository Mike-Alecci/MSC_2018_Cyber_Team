class HackingDrones:
    """Trying to hack drones and cool stuff"""
    def __init__(self, known_ips):
        """The init method instantiates the known list of ips to track"""
        known_ips = known_ips

    def read_files(self, file_name, seperator = ", "):
        """A generic read file generator to check bad file inputs and read line by line"""
        try:
            fp = open(file_name, 'r')
        except FileNotFoundError:
            raise FileNotFoundError ("Could not open {}".format(file_name))
        else:
            with fp:
                for line in fp:
                    l = line.strip().split(seperator)
                        yield l.strip()

    def identification(self):
        """This function takes the information from the generator and then attempts to identify if it is a known 
           drone IP"""
        read_network_ips = self.read_files("students.txt", seperator = ", ")
        for line in read_network_ips:
            bssid = line[0]
            channel = line[3]
            name = line[13]

        return None