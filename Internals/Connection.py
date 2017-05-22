import threading
import socket
#7000 - 8000

class PortScan:
    def __init__(self, host = "localhost"):
        self.host = host
    
    def Start(self):
        threads = []
        output = {}
        ports = []
        
        print("Scanning ports 7000-8000 on {}...".format(self.HostIP))
        
        for x in range(7000, 8000):
            t=threading.Thread(target=self.Connect, args=(self.HostIP, x, output))
            threads.append(t)

        for y in range(0, len(threads), int(len(threads)/100)):
            for x in range(y,int(y+len(threads)/100)):
                threads[x].start()

            for x in range(y,int(y+len(threads)/100)):
                threads[x].join()


        for x in range(7000, 8000):
            if not output[x]==None:
                ports.append(output[x])
        
        return ports
    
    def Connect(self, IP, x, output):
        PortScan=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PortScan.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        PortScan.settimeout(.1)
        try:
            PortScan.connect((IP, x))
            output[x]=str(x)
        except:
            output[x]=None

