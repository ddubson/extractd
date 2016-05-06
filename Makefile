init:
	pip install -r requirements.txt

run:
	python extractd/extractd.py --host $(host) --user $(user) --password $(pass)

test:
	nosetests