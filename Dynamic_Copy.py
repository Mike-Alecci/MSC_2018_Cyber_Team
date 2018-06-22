import csv
import os

class Dynamic_Copy:
    """Generates a dynamic copy of Deauth_Template.txt specific to each drone's network connection."""
    def __init__(self, channel, bssid, station):
        """The init method populates the [] variables with the matches from the WiFi scan."""
        self.channel = channel
        self.bssid = bssid
        self.station = station

    def generate(self, template_file, new_file, seperator = ","):
        """Copies information from the template file, overwrites placeholders and creates a new script."""
        try:
            open(template_file, 'rb')
        except FileNotFoundError:
            raise FileNotFoundError ("Could not open {}".format(template_file))
        else:
            with open(template_file, 'rb') as file:
                data = file.read()
            data = data.replace('[CH]', self.channel)
            data = data.replace('[BSSID]', self.bssid)
            data = data.replace('[STATION]', self.station)
            with open(new_file, 'w+') as file:
                file.write(data)
        
        



        


