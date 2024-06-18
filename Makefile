.PHONY: install test

install:
	@type poetry >/dev/null || pip3 install poetry
	@poetry install --no-root

test: install
	poetry run pytest -s
