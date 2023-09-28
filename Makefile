.PHONY: install test

install:
	@type poetry >/dev/null || pip3 install poetry
	@poetry install

test: install
	poetry run pytest -s
