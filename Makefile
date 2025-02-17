.PHONY: install test

shell:
	DEVBOX_USE_VERSION=0.13.1 devbox shell

test:
	find ./ -mindepth 2 -name .venv -exec rm -rf {}; \
	pytest -s test/
