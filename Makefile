install:
	 pip install --upgrade pip &&\
	 	pip install -r requirements.txt

lint: 
	black *.py

test:
	# testing code

build:
	# build code

deploy: 
	# deploy code