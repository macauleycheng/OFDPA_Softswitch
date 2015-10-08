#!/bin/bash
#Ubunut 14.04+ Reference:
#http://tocai.dia.uniroma3.it/compunet-wiki/index.php/Installing_and_setting_up_OpenFlow_tools

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install cmake libpcap-dev libxerces-c2-dev libpcre3-dev flex bison pkg-config autoconf libtool libboost-dev build-essential unzip git -y

#Downgrade Bison:

wget -nc http://de.archive.ubuntu.com/ubuntu/pool/main/b/bison/bison_2.5.dfsg-2.1_amd64.deb \
         http://de.archive.ubuntu.com/ubuntu/pool/main/b/bison/libbison-dev_2.5.dfsg-2.1_amd64.deb
sudo dpkg -i bison_2.5.dfsg-2.1_amd64.deb libbison-dev_2.5.dfsg-2.1_amd64.deb
rm bison_2.5.dfsg-2.1_amd64.deb libbison-dev_2.5.dfsg-2.1_amd64.deb

#Install Nbee:
wget -nc http://www.nbee.org/download/nbeesrc-jan-10-2013.zip
unzip nbeesrc-jan-10-2013.zip
cd nbeesrc-jan-10-2013/src
cmake .
make
sudo cp ../bin/libn*.so /usr/local/lib
sudo ldconfig
sudo cp -R ../include/* /usr/include/
cd ../..


#add ofsoftswitch13
#git clone https://github.com/CPqD/ofsoftswitch13.git
cd ofsoftswitch13
#sudo chmod +x boot.sh soexpand.pl
sudo ./boot.sh
sudo ./configure
sudo make install
cd ..

#add aos-dpctl
git clone https://github.com/macauleycheng/aos-dpctl.git
cd aos-dpctl
sudo ./boot.sh
sudo ./configure
sudo make
cd ..

