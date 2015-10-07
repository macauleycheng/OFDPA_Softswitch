# OFDPA_Softswitch
This ofsoftswich.sh help you download and build the ofsoftswitch.

Ofsoftswitch, https://github.com/CPqD/ofsoftswitch13.git, is a simple openflow switch.
It can use group chain, so it can simulate OFDPA group chain action.
Currently, the Openvswitch still not support it.

Notice that the ofsoftswitch doesn't have ofdpa limitation yet.
That means the flow or group you can put into this softswitch may not successfully install to real OFDPA switch.
Please use AOS_OF_Example or AOS_OF_Example to familiar with OFDPA pipeline.

This softswitch let you don't borrow a real switch to verify your application.

Later we will add OFDPA limitation on it.
