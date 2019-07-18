#!/bin/bash
sudo apt-get update
sudo add-apt-repository -y ppa:tsl0922/ttyd-dev
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y git ttyd software-properties-common build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
curl -sL https://deb.nodesource.com/setup_11.x -o nodesource_setup.sh
chmod +x nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs python3.7 npm
npm install -g serverless serverless-python-requirements
wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
mkdir -p /root/labs/ && cd /root/labs/
