there_is_no_default_target:
	@echo "there is no default target, look at the makefile to see what targets you can build"
	@exit 1


###### project setup and building ######
setup: ../.env
	python -m pip install poetry
	python -m pip install black
	python -m pip install isort
	python -m pip install flake8
	if [[ ! -f ".env" ]]; then \
	  ln ../.env ./.env; \
	fi

format:
	isort .
	black --line-length 100 .

test: format test_*.py
	python -m poetry run python -m unittest test_*.py

build: pyproject.toml
	python -m poetry lock --no-update
	python -m poetry install

clean: __pycache__ poetry.lock
	rm -rf __pycache__
	rm poetry.lock


###### run discord bot ######
discord_bot: build discord_bot.py
	python -m poetry run python discord_bot.py
