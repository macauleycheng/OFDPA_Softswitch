#!/bin/bash
ofdatapath -i eth1,eth2 --datapath-id=000000111111 --no-local-port punix:/home/manager/ofdp &
ofprotocol unix:/home/manager/ofdp tcp:127.0.0.1:6633
