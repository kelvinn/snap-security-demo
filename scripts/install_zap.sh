#!/bin/bash

echo Downloading ZAP from Amazon S3
wget http://cdn.kelvinism.com/files/ZAP_2.3.1_Linux.tar.gz

echo Untarring ZAP
tar -xpzf ZAP_2.3.1_Linux.tar.gz

echo Starting ZAP daemon
./ZAP_2.3.1/zap.sh -daemon & # Now fork into the background
