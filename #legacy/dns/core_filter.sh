#!/bin/bash

# EXEC EVERYDAY
# SETUP
rm -r "/tmp/dns/"
mkdir "/tmp/dns/"
cd "/tmp/dns/" || exit

# LISTS
echo -e "\n\n$(curl https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts)" >raw-records || exit
echo -e "\n\n$(curl https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Extension/GoodbyeAds-Xiaomi-Extension.txt)" >>raw-records || exit
echo -e "\n\n$(curl https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Extension/GoodbyeAds-Samsung-AdBlock.txt)" >>raw-records || exit

# CLEAN LISTS
curl -O https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/ALL-phishing-domains.tar.gz || exit
tar -xvzf ALL-phishing-domains.tar.gz
curl https://dbl.oisd.nl >oisd_dbl_full.txt || exit
curl -O https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist/master/ips/ips0.list || exit
echo -e "\n\n$(sed 's/^/0.0.0.0 /' ALL-phishing-domains.txt)" >raw-plainrecords
echo -e "\n\n$(sed 's/^/0.0.0.0 /' oisd_dbl_full.txt)" >>raw-plainrecords
echo -e "\n\n$(sed 's/^/0.0.0.0 /' ips0.list)" >>raw-plainrecords
echo -e "\n\n$(cat raw-plainrecords)" >>raw-records

# CLEAN
sed -i "/^0/!d" raw-records
sed -i "/^ *$/d" raw-records
sed -i "/#/d" raw-records
sort -u -o raw-records raw-records
sed -i "1,6d" raw-records

# OVERWRITE
mkdir "/srv/dns/"
cp raw-records "/srv/dns/"
