install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	#format code
lint:
	#pylint
test:
	#tests
deploy:
	#deploy
all: install lint test deploy