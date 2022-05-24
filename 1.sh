cd /root/openvpn && sudo chmod +x openvpn-install.sh && sudo chmod +x requirement.sh && sudo chmod +x ./shadow.sh && sudo chmod +x ./status.sh && sudo ./requirement.sh
cd /root/openvpn && sudo ./openvpn-install.sh && sudo ./shadow.sh
echo "[Unit]
Description=Job that runs your user script

[Service]
ExecStart=nohup python3 -u app.py &> ./app.out &
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target" >> /etc/systemd/system/mehti.service
sudo systemctl daemon-reload
sudo systemctl enable mehti.service
sudo systemctl start mehti.service
