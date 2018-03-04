# CekHs
Cek Hash Rate for ethereum mining rig, auto reset machine if dropping hash rate.


HS Rate ceker, and auto restart mahine miner, ethermine pool.
Requir :
1. Rasp Pi 3
2. Relay Modul
3. Install Python
4. Ethermine pool

Step :
1. Assemble your HW req
2. Setup install

download extract dir "HsCek"

open "setingku.py"
wallet : ....
typing or insert your eth wallet

worker : ...
rig number, pin of relay and target of hs rate.

open in terminal pi, type "crontab -e" enter, in last row insert this:
"@reboot sudo python /home/yout/directory/cekHashRate.py"
if done, "ctrl+x"
#reboot


More info : fb,twt,ig @idmahbub
thanks,,, www.wicsolution.com