#!/bin/bash


sudo vagrant up
ssh_config=$(sudo vagrant ssh-config | grep HostName)
regex="HostName\s(.+)"

if [[ $ssh_config =~ $regex ]]
then
  server_ip=${BASH_REMATCH[1]}
  export CUCUMBER_DEMO_SERVER_URL="http://$server_ip:8080"
fi
