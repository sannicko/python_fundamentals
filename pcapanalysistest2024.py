import pyshark

class MITMProject:
    def __init__(self, pcap_file):
        self.cap = pyshark.FileCapture(pcap_file)

class PacketAnalyzer:
    def __init__(self, pcap_file):
        self.cap = pyshark.FileCapture(pcap_file)

    def syn_ack(self):
      n = 0
      for packet in self.cap:
          #print(packet) #print for debbug
          #print(packet.ip.src) #print for debbug
          #print(packet.ip.dst) #print for debbug
          print(packet.tcp.dstport) #print destionation ports
          #print(packet.tcp.flags_syn.int_value) #default mode
          #print(packet.ip) #print for debbug
          if 'TCP' in packet:
            flags_int = int(packet.tcp.flags, 16)
            if flags_int & 0x12 == 0x12:  # Check if both SYN and ACK flags are set
              n += 1            
      return n
    

if __name__ == '__main__':
    pcap_analysis = MITMProject("TCP.reflection_fall2023.pcap")  
    packet_analyzer = PacketAnalyzer("TCP.reflection_fall2023.pcap")
    synack = packet_analyzer.syn_ack()
    print("Number of SYN+ACK Packets: ", synack)
#    rst = pcap_analysis.rst()
#    print("IP and Port: ",ip,port)
#    print("Number of RST Packets : ", rst)
