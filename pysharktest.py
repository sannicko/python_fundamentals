import pyshark

def count_ack_packets(pcap_file):
    # Open the pcap file for reading
    cap = pyshark.FileCapture(pcap_file)

    # Initialize a counter for ACK packets
    ack_count = 0

    # Iterate through each packet in the pcap file
    for packet in cap:
        #print(packet)
        print(packet.tcp.flags_ack)
        print(packet.tcp.flags_syn)
        # Check if the packet is a TCP packet and has the ACK flag set
        #if 'TCP' in packet:# and 'RST' in packet.tcp.flags:
        #if 'TCP' in packet: #and 'ACK' in packet.tcp.flags:  
            #ack_count += 1

    # Close the pcap file
    #cap.close()

    #return ack_count

if __name__ == '__main__':
    # Specify the path to your .pcap file
    pcap_file_path = "TCP.reflection_fall2023.pcap"

    # Call the function to count ACK packets
    ack_count = count_ack_packets(pcap_file_path)

    # Print the result
    print("Number of TCP packets with ACK flag:", ack_count)
