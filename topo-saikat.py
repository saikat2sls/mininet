"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host



         ISP1 
          |
         (RT1)
     /   /     \   \
   GW1  GW2   GW3  GW4    
    |   |      |     |  
 CPE1   CPE3   CPE5  CPE7
   CPE2   CPE4  CPE6   CPE8

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        host1 = self.addHost( 'CPE1' )
        host2 = self.addHost( 'CPE2' )
        host3 = self.addHost( 'CPE3' )
        host4 = self.addHost( 'CPE4' )
        host5 = self.addHost( 'CPE5' )
        host6 = self.addHost( 'CPE6' )
        host7 = self.addHost( 'CPE7' )
        host8 = self.addHost( 'CPE8' )
        host9 = self.addHost( 'ISP1' )




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
        self.addLink( host7, switch4,cls=TCLink,bw=0 )
        self.addLink( host8, switch4,cls=TCLink,bw=0 )
        self.addLink( switch1, switch5 )
        self.addLink( switch2, switch5 )
        self.addLink( switch3, switch5 )
        self.addLink( switch4, switch5 )



topos = { 'mytopo': ( lambda: MyTopo() ) }
