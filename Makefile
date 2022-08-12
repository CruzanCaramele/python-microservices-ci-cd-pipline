install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	black *.py src/*.py
lint:
	pylint --disable=R,C *.py src/*.py
test:
	python -m pytest -vv --cov=src test_*.py
build:
	#build container
deploy:
	#deploy
all: install format lint test build deploy