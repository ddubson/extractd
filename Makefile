init:
	pip install -r requirements.txt

v-up:
	vagrant up

v-down:
	vagrant halt
	
run:
	python extractd/extractd.py --host $(host) --user $(user) --password $(pass)

test:
	nosetests