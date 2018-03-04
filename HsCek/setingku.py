#!/usr/bin/env python
wallet = '0xed2e789f57b2478c393eac991a07906b6bd518b1'
worker = {	'1':{'pin':'13','targeths':'89'},
			'2':{'pin':'12','targeths':'80'},
			'3':{'pin':'13','targeths':'80'},
			'4':{'pin':'14','targeths':'80'},
			'5':{'pin':'15','targeths':'80'},
			'6':{'pin':'16','targeths':'80'},
			'7':{'pin':'17','targeths':'80'},
			'8':{'pin':'18','targeths':'80'}	
		 } #tambahkan saja, dimulai dari 0, format (pin dan target hs rate)
interval = 300 #cek berapa lama sekai, satuan detik, defautl 300/5menit
use_anonymous = True