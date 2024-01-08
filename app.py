import socket
import struct
import textwrap



def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}\nSource: {}\nProtocol: {}\nData: {}'.format(
            dest_mac, src_mac,eth_proto, data)
            )
        print("=============================================================")
        

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[:14]

#It should be return AA:BB:CC:DD:EE
def get_mac_addr(addr) :
    bytes_str = map('{:02x}'.format, addr)
    return ':'.join(bytes_str).upper()

main()
     

