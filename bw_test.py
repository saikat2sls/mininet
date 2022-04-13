#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.node import OVSController
import time
import os

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')

        # Add hosts
        host1 = self.addHost( 'CPE1' )
        host2 = self.addHost( 'CPE2' )
        host3 = self.addHost( 'CPE3' )
        host4 = self.addHost( 'CPE4' )
        host5 = self.addHost( 'CPE5' )
        host6 = self.addHost( 'CPE6' )
        host7 = self.addHost( 'CPE7' )
        host8 = self.addHost( 'CPE8' )
        host9 = self.addHost( 'ISP1' )

        # Add hops
        switch5 = self.addSwitch( 'RT1' )
        switch1 = self.addSwitch( 'GW1' )
        switch2 = self.addSwitch( 'GW2' )
        switch3 = self.addSwitch( 'GW3' )
        switch4 = self.addSwitch( 'GW4' )

        # Add links
        self.addLink( host9, switch5,cls=TCLink,bw=50 )
        self.addLink( host1, switch1,cls=TCLink,bw=10 )
        self.addLink( host2, switch1,cls=TCLink,bw=10 )
        self.addLink( host3, switch2,cls=TCLink,bw=10 )
        self.addLink( host4, switch2,cls=TCLink,bw=10 )
        self.addLink( host5, switch3,cls=TCLink,bw=10 )
        self.addLink( host6, switch3,cls=TCLink,bw=10 )
        self.addLink( host7, switch4,cls=TCLink,bw=5 )
        self.addLink( host8, switch4,cls=TCLink,bw=10 )
        self.addLink( switch1, switch5 )
        self.addLink( switch2, switch5 )
        self.addLink( switch3, switch5 )
        self.addLink( switch4, switch5 )
        # Python's range(N) generates 0..N-1

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=8)
    net = Mininet(topo = topo, controller = OVSController)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    h9, h1, h2, h3, h4, h5, h6, h7, h8 = net.get( 'ISP1', 'CPE1', 'CPE2', 'CPE3', 'CPE4',  'CPE5',  'CPE6',  'CPE7', 'CPE8' )

    #iperf Server
    h9.cmdPrint('iperf -s  > iperf_server_result &')
    print "Server strted"
    h7.cmdPrint('iperf -c ' + h9.IP() + ' -t 100 >> cpe1_result &')
    time.sleep(0.1)
    h7.cmdPrint('iperf -c ' + h9.IP() + ' -t 100 >> cpe1_result &')
    time.sleep(0.1)
    h7.cmdPrint('iperf -c ' + h9.IP() + ' -t 100 >> cpe1_result &')

    #iperf Client(s)
    for h in range(8):
        host = net.get('CPE%s' % (h + 1))
        print "CPE-" + str(h + 1) + ":" + host.IP()
        host.cmdPrint('iperf -c ' + h9.IP() + ' -t 100 >> cpe%d_result &' % (h+1))
        time.sleep(0.3)

    print "Testing bandwidth between ISP host and CPE"
    #net.iperf( (h1, h2) )
    time.sleep(115)
    
    for h in range(8):
        os.system("cat cpe%d_result >> cpe_final" %(h+1))
        os.system("rm -rf cpe%d_result" %(h+1))
        time.sleep(0.2)
    
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
