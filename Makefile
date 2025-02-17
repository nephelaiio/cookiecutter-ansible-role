.PHONY: install test

shell:
	DEVBOX_USE_VERSION=0.13.1 devbox shell

install:
	@poetry install --no-root

test: install
	poetry run pytest -s
