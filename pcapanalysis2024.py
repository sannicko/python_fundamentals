# You may NOT alter the import list!!!!
import pyshark
import hashlib


class MITMException(Exception):
    """A class to throw if you come across incorrect syntax or other issues"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MITMProject(object):
    def __init__(self):
        self.cap = pyshark.FileCapture('TCP.reflection_fall2023.pcap')
        self.class_id = "CS60353257"

        # TODO: Change this to YOUR Georgia Tech ID!!!
        # This is your 9-digit Georgia Tech ID
        self.student_id = '903940438'

    def get_student_hash(self, value):
        return hashlib.sha256(self.student_id.encode('UTF-8') + self.class_id + value).hexdigest()

    # TODO: 
    #   Task 1: Return n being:
    #       n = Number of packets with only SYN+ACK flags
    def syn_ack(self):
        n = 0
        # TODO: Implement me 
        for packet in self.cap:
          if 'TCP' in packet:
            flags_int = int(packet.tcp.flags, 16)
            if flags_int & 0x12 == 0x12:
              n += 1            
        return n

    # TODO: 
    #   Task 2: Return n being:
    #       n = Number of packets with only RST flag
    def rst(self):
        n = 0
        # TODO: Implement me 
        for packet in self.cap:
          if 'TCP' in packet:
            flags_int = int(packet.tcp.flags, 16)
            if flags_int & 0x04:
              n += 1            
        return n

    # TODO: 
    #   Task 3: Return d,p, being:
    #       d = IP Address of the victim
    #       p = Port being attacked
    def victim_ip_port(self):
        d,p = '0.0.0.0', 0
        dstip=[]
        sreportlist=[]
        srcportlist=[]
        
        for packet in self.cap:
            if packet.eth.type == '0x0800':
                dstip.append(str(packet.ip.dst))
                if packet.ip.proto == '6':
                    sreportlist.append(int(packet.tcp.srcport))
                elif packet.ip.proto == '17' and packet.ip.flags_mf == '0':
                    srcportlist.append(int(packet.udp.srcport))
        
        if dstip and (sreportlist or srcportlist):
            d = max(set(dstip), key=dstip.count)
            p = max(sreportlist + srcportlist, key=(sreportlist + srcportlist).count)
        
        return d,p

if __name__ == '__main__':
    pcap_analysis = MITMProject()
    ip,port = pcap_analysis.victim_ip_port()
    synack = pcap_analysis.syn_ack()
    rst = pcap_analysis.rst()
    print("IP and Port: ",ip,port)
    print("Number of SYN+ACK Packets : ", synack)
    print("Number of RST Packets : ", rst)

    
