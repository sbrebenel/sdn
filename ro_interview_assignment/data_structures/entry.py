import ipaddress


class Entry:

    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    list_test = []

    def get_results(self):
        self.list_test.append(self.address)
        return sorted(self.list_test, key=ipaddress.IPv4Address)
