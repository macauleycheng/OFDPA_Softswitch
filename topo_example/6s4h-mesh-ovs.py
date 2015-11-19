#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.node import RemoteController, OVSSwitch
from functools import partial
from mininet.link import Intf
from mininet.util import quietRun

"""
   H1 -- OF1 -- OF3 --OF5 -- H3
      /\  |      |     |   \/
   H2    OF2 -- OF4 --OF6 -- H4
"""
class Topo6s4hMesh( Topo ):
    def __init__( self ):    
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        s1 = self.addSwitch('s1111')
        s2 = self.addSwitch('s2222')
        s3 = self.addSwitch('s3333')
        s4 = self.addSwitch('s4444')
        s5 = self.addSwitch('s5555')
        s6 = self.addSwitch('S6666')

        self.addLink( h1, s1)
        self.addLink( h2, s1)
        self.addLink( h1, s2)
        self.addLink( h2, s2)
        self.addLink( s1, s2)
        self.addLink( s1, s3)
        self.addLink( s2, s4)
        self.addLink( s3, s4)
        self.addLink( s3, s5)
        self.addLink( s4, s6)
        self.addLink( s5, s6)
        self.addLink( h3, s5)
        self.addLink( h3, s6)
        self.addLink( h4, s5)
        self.addLink( h4, s6)
    
if __name__ == '__main__':
    setLogLevel( 'info' )

    topo = Topo6s4hMesh()    
    
    net = Mininet(topo=topo, controller=partial(RemoteController,ip='127.0.0.1'),
                 switch=OVSSwitch)
    net.start()
    
    #switch=net.switches[0]
    #print dir(net.switches[0])
    #print net.switches[0].name
    for s in net.switches:
        cmd = "ovs-vsctl set bridge "+s.name+" protocols=OpenFlow13"
        s.sendCmd(cmd)

    h1, h2, h3, h4 = net.hosts

    h1.setIP("10.200.1.1/24")
    h1.setMAC("00:00:00:00:01:01")
    h2.setIP("10.200.1.2/24")
    h2.setMAC("00:00:00:00:02:02")
    h3.setIP("10.200.1.3/24")
    h3.setMAC("00:00:00:00:03:03")
    h4.setIP("10.200.1.4/24")
    h4.setMAC("00:00:00:00:04:04")

    CLI(net)
    net.stop()    
