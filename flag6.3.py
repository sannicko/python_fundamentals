def dest_ip_port(self):
    d, p = None, None
    for packet in self.cap:
        if 'IP' in packet and 'TCP' in packet:
            destination_ip = packet.ip.dst
            source_port = int(packet.tcp.srcport)

            if source_port == 80:
                d, p = destination_ip, source_port
                return d, p  

    return d, p  
