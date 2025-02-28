from scapy.all import sniff  

def packet_callback(packet):
    if packet.haslayer("IP"):  # Check if packet has an IP layer
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto  # Protocol (TCP/UDP/ICMP)
        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {protocol}")

sniff(prn=packet_callback, store=False)

