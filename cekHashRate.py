import requests
import setingku as seting
import RPi.GPIO as GPIO
import sched, time
def restart(relay):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(relay, GPIO.OUT)
	GPIO.output(relay,1)
	time.sleep(5)
	GPIO.output(relay,0)
	time.sleep(2)
	time.sleep(5)
	GPIO.output(relay,1)
	time.sleep(5)
	GPIO.output(relay,0)
	time.sleep(0.1)
	GPIO.cleanup()
    	return

def cekHs():	
	r = requests.get('https://api.ethermine.org/miner/'+seting.wallet+'/workers')
	data = r.json()
	rig = 1
	for each in data['data']:
	    print 'HS Sekarang = ',each['currentHashrate'],', Worker = ',each['worker'],', Pin relay =',seting.worker[str(rig)]['pin'] #debug
	    if (each['currentHashrate'] > float(10)) and (each['currentHashrate'] < float(seting.worker[str(rig)]['targeths'])):
	    	relay = int(seting.worker[str(rig)]['pin'])
	    	restart(relay)
	    	print 'Hs pusing minta restart, Nomor rig = ', rig, ', Target hs =', seting.worker[str(rig)]['targeths']
	    else:
	    	print 'Hs sehat, Nomor rig = ', rig, ', Taret HS =',seting.worker[str(rig)]['targeths']
	    rig += 1
	    pass

#jadwal cek berdasarkan detik
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print "Pantau hs rig ..."
    cekHs()
    s.enter(seting.interval, 1, do_something, (sc,))

s.enter(seting.interval, 1, do_something, (s,))
s.run()
