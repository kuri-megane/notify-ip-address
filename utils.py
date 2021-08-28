from netifaces import interfaces, ifaddresses, AF_INET


def get_ip_address():
    addresses = []
    for ifaceName in interfaces():
        addresses.append([i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])])
    return addresses


if __name__ == '__main__':
    print(get_ip_address())
