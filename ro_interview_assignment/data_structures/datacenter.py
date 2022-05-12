import re


class Datacenter:
    def __init__(self, name, cluster_list):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = cluster_list

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        cluster_to_be_removed = []
        for key, value in self.clusters.items():
            data_found = re.findall("^[A-Z]{3}-[0-9]{1,3}$", key)
            if len(data_found) == 0:
                cluster_to_be_removed.append(key)
        for i in cluster_to_be_removed:
            self.clusters.pop(i)
        return self.clusters
