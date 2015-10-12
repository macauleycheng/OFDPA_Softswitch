#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.node import RemoteController, UserSwitch
from functools import partial
from mininet.link import Intf
from mininet.util import quietRun

class Topo1s2h( Topo ):
    def __init__( self ):    
        # Initialize topology
        Topo.__init__( self )    
        
        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')

        self.addLink( h1, s1)        
        self.addLink( h2, s1)

          
def checkIntf( intf ):
    "Make sure intf exists and is not configured."
    if ( ' %s:' % intf ) not in quietRun( 'ip link show' ):
        error( 'Error:', intf, 'does not exist!\n' )
        exit( 1 )
    #ips = re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun( 'ifconfig ' + intf ) )
    #if ips:
    #    error( 'Error:', intf, 'has an IP address,'
    #           'and is probably in use!\n' )
    #    exit( 1 )

    
if __name__ == '__main__':
    setLogLevel( 'info' )

    checkIntf('eth1')
    checkIntf('eth2')

    topo = Topo1s2h()    
    
    net = Mininet(topo=topo, controller=partial(RemoteController,ip='127.0.0.1'), switch=UserSwitch)    
    net.start()

    switch=net.switches[0]
    Intf('eth1', node=switch)
    Intf('eth2', node=switch)

    h1, h2 = net.hosts
    h1.setIP("10.200.1.1/24")
    h1.setMAC("00:00:00:00:01:01")
    h2.setIP("10.200.1.2/24")
    h2.setMAC("00:00:00:00:02:02")




    CLI(net)
    net.stop()    
