#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import RemoteController, UserSwitch
from functools import partial

class Topology1( Topo ):
    def __init__( self ):    
        # Initialize topology
        Topo.__init__( self )    
        
        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
            
        s1 = self.addSwitch('s1')

        self.addLink( host1, s1)        
        self.addLink( host2, s1)
        self.addLink( host3, s1)
        self.addLink( host4, s1)
        
        
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = Topology1()    
    
    net = Mininet(topo=topo, controller=partial(RemoteController,ip='127.0.0.1'), switch=UserSwitch)    
    net.start()
    
    h1, h2, h3, h4 = net.hosts
    h1.setIP("10.200.1.1/24")
    h1.setMAC("00:00:00:00:01:01")

    h2.setIP("10.200.1.2/24")
    h2.setMAC("00:00:00:00:01:02")

    h3.setIP("10.200.1.3/24")
    h3.setMAC("00:00:00:00:01:03")

    h4.setIP("10.200.1.4/24")
    h4.setMAC("00:00:00:00:01:04")

    
    CLI(net)
    net.stop()    
