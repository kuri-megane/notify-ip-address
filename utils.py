from netifaces import interfaces, ifaddresses, AF_INET
import subprocess


def get_local_ip_address():
    addresses = []
    for ifaceName in interfaces():
        addresses.append([i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])])
    return addresses


def get_disk_usage():
    cmd_df = 'df -H /'
    ret = subprocess.run(args=cmd_df.split(' '), check=True, capture_output=True)

    return ret.stdout.decode()


if __name__ == '__main__':
    print(get_local_ip_address())
    print(get_disk_usage())
