from scapy.all import sniff
import threading

packet_data = []  # Shared list to store packet info

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        packet_data.append({"Source": src_ip, "Destination": dst_ip, "Protocol": protocol})

def start_sniffing():
    sniff(prn=packet_callback, store=False)

def run_sniffer_in_thread():
    thread = threading.Thread(target=start_sniffing, daemon=True)
    thread.start()
