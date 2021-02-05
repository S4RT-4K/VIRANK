sleep 2
clear
apt install python
apt install figlet
apt install wget
apt install toilet -y
sleep 1
clear
toilet -f mono12 -F border:metal 'DONE!'
echo -e "\e[1;33mREQUIREMENTS INSTALLED, Run this with "python virank.py"\e[0m"
echo 

sleep 2
echo -e "\e[1;31mStarting script\e[0m"

sleep 2
python virank.py
