cd /root/openvpn && sudo chmod +x openvpn-install.sh && sudo chmod +x requirement.sh && sudo chmod +x ./shadow.sh && sudo chmod +x ./status.sh && sudo ./requirement.sh
cd /root/openvpn && sudo ./openvpn-install.sh && sudo ./shadow.sh && nohup python3 -u app.py &> ./app.out &
cat <(crontab -l) <(echo "crontab -e @reboot cd openvpn && nohup python3 -u app.py &> ./app.out &") | crontab -
