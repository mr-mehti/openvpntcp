sudo chmod +x /root/openvpn/openvpn-install.sh && sudo chmod +x /root/openvpn/requirement.sh && sudo chmod +x /root/openvpn/shadow.sh && sudo chmod +x /root/openvpn/status.sh && sudo /root/openvpn/requirement.sh
sudo /root/openvpn/openvpn-install.sh && sudo /root/openvpn/shadow.sh
echo "[Unit]
Description=Job that runs your user script

[Service]
ExecStart=nohup python3 -u /root/openvpn/app.py &> ./app.out &
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target" >> /etc/systemd/system/mehti.service
sudo systemctl daemon-reload
sudo systemctl enable mehti.service
sudo systemctl start mehti.service
