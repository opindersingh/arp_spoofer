import scapy.all as scapy
arp_packet = scapy.ARP(op=2,pdst="192.168.225.249",hwdst="00-0C-29-52-47-B6",psrc="192.168.225.230")
scapy.ls(arp_packet)
print(arp_packet.summary())
print(arp_packet.show())
