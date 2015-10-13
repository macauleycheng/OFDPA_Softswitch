#!/bin/bash
sudo ofdatapath -i eth1,eth2 --datapath-id=000000111111 punix:/home/manager/ofdp &
sudo ofprotocol unix:/home/manager/ofdp tcp:127.0.0.1:6633
