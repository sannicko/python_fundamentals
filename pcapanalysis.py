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
            if 'TCP' in packet and packet.tcp.flags_syn == "1" and packet.tcp.flags_ack == '1':
                n +=1

        return n

    # TODO: 
    #   Task 2: Return n being:
    #       n = Number of packets with only RST flag
    def rst(self):
        n2 = 0

        try:
            # TODO: Implement me
            for packet in self.cap:
                if 'TCP' in packet and packet['TCP'].flags_raw_value == '4':
                    n2 += 1 
        except Exception as e:
            pass
        
        return n2



    # TODO: 
    #   Task 3: Return d,p, being:
    #       d = IP Address of the victim
    #       p = Port being attacked
    def victim_ip_port(self):
        d,p = 0,0

        # TODO: Implement me 

        return d,p


if __name__ == '__main__':
    pcap_analysis = MITMProject()
    ip,port = pcap_analysis.victim_ip_port()
    synack = pcap_analysis.syn_ack()
    rst = pcap_analysis.rst()
    print("IP and Port: ",ip,port)
    print("Number of SYN+ACK Packets : ", synack)
    print("Number of RST Packets : ", rst)

    
