all:setup

setup:
	@echo ">>> Setting up virtualenv"
	virtualenv .venv && source .venv/bin/activate
	@echo ">>> Installing dependancies from requirements.txt"
	.venv/bin/pip install -r requirements.txt

deploy:
	@echo ">>> Deploying to heroku"
	@git push heroku master

tests:
	@nosetests

.PHONY: all setup tests deploy
