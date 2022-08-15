termux-setup-storage
pkg install python -y
pkg install git -y
git clone https://github.com/Sajmonpcgamer/sparklyai
cd sparklyai-main/client
python -m pip install -r ./requirements.txt
python .
