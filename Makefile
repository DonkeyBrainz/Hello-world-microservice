install:
	# upgrade pip and install requirements
	 pip install --upgrade pip &&\
	 	pip install -r requirements.txt

lint: 
	# linting with pylint
	pylint --disable=R,C *.py
	
format:
	# format code with black
	black *.py

test:
	# test code with pytest
	python -m pytest -vv --cov=lib tests

build:
	# build container
	docker build -t deploy-helloworld-microservice .

run:
	# run docker
	docker run -p 127.0.0.1:8080:8080 3c46cadff8c4

deploy: 
	# deploy code

all:
	# do all things