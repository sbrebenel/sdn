from ipaddress import IPv4Address, IPv4Network


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.raw_entry_list = raw_entry_list

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        accepted_ips = []
        networks = {}
        for i in range(len(self.raw_entry_list)):
            try:
                if IPv4Address(self.raw_entry_list[i]['address']) in \
                        IPv4Network(self.ipv4_network):
                    accepted_ips.append(self.raw_entry_list[i])
            except ValueError:
                pass
        networks[self.ipv4_network] = accepted_ips
        return networks

    entries = []

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
