import ipaddress

# Funktion zur Umwandlung der Subnetzmaske in binäre Form
def subnet_mask_to_binary(subnet_mask):
    binary = ''.join(format(int(x), '08b') for x in subnet_mask.split('.'))
    return binary

# Funktion zur Berechnung der Anzahl der Hosts
def calculate_hosts(subnet_mask):
    binary_mask = subnet_mask_to_binary(subnet_mask)
    host_bits = binary_mask.count('0')
    hosts = 2**host_bits - 2  # Zwei Adressen werden für Netzwerk und Broadcast reserviert
    return hosts

# Funktion zur Berechnung der Anzahl der Subnetze
def calculate_subnets(subnet_mask, original_mask='255.255.255.0'):
    # Umwandlung beider Masken in Binärform
    binary_original_mask = subnet_mask_to_binary(original_mask)
    binary_new_mask = subnet_mask_to_binary(subnet_mask)

    # Zählen der Anzahl der neuen Subnetzbits
    subnet_bits = binary_new_mask.count('1') - binary_original_mask.count('1')

    # Berechnung der Anzahl der Subnetze
    subnets = 2**subnet_bits
    return subnets

# Funktion zur Berechnung der Netzwerkadresse und der Broadcast-Adresse
def calculate_network_and_broadcast(ip, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
    return str(network.network_address), str(network.broadcast_address)

# Funktion zur Berechnung der ersten und letzten Hostadresse im Subnetz
def calculate_hosts_range(ip, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
    first_host = str(network.network_address + 1)
    last_host = str(network.broadcast_address - 1)
    return first_host, last_host

# Beispiel zur Berechnung der Subnetze und Hosts
if __name__ == "__main__":
    ip = "192.168.1.0"  # Beispiel IP-Adresse
    subnet_mask = "255.255.255.0"  # Beispiel Subnetzmaske

    # Berechnung der Anzahl der Hosts
    hosts = calculate_hosts(subnet_mask)
    print(f"Anzahl der Hosts im Subnetz: {hosts}")

    # Berechnung der Anzahl der Subnetze
    subnets = calculate_subnets(subnet_mask)
    print(f"Anzahl der Subnetze: {subnets}")

    # Berechnung der Netzwerkadresse und Broadcast-Adresse
    network_address, broadcast_address = calculate_network_and_broadcast(ip, subnet_mask)
    print(f"Netzwerkadresse: {network_address}")
    print(f"Broadcast-Adresse: {broadcast_address}")

    # Berechnung der ersten und letzten Hostadresse
    first_host, last_host = calculate_hosts_range(ip, subnet_mask)
    print(f"Erste Host-Adresse: {first_host}")
    print(f"Letzte Host-Adresse: {last_host}")
