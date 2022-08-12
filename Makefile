install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	black *.py lib/*.py
lint:
	#pylint
test:
	#tests
deploy:
	#deploy
all: install lint test deploy