from data_structures.datacenter import Datacenter
from data_structures.network_collection import NetworkCollection
from data_structures.entry import Entry
import requests
import time

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    for i in range(1, max_retries+1):
        try:
            get_ip = requests.get(url, verify=False, timeout=delay_between_retries)
        except requests.exceptions.RequestException as error:
            print(error)
        finally:
            if get_ip.status_code == 200:
                data = get_ip.json()
                break
            else:
                data = "Something didn't work well!"
                time.sleep(delay_between_retries)
    return data


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value) for key, value in data.items()
    ]

    new_clusters = {}
    for item in datacenters:
        new_cluster = item.remove_invalid_clusters()
        new_clusters.update(new_cluster)
        print("New cluster has been added : ", new_cluster)
    print(new_clusters)

    ips = [
        NetworkCollection(key, value) for item in new_clusters.values() for key, value in item['networks'].items()
    ]

    new_networks = {}
    for item in ips:
        new_network = item.remove_invalid_records()
        new_networks.update(new_network)
    print(new_networks)

    entries = []

    for key, value in new_networks.items():
        for i in range(len(value)):
            address = value[i]['address']
            available = value[i]['available']
            last_used = value[i]['last_used']
            entries.append(Entry(address, available, last_used))

    for item in entries:
        result = item.get_results()
    print(result)




if __name__ == '__main__':
    main()
